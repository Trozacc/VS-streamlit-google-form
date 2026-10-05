"""
Database query functions.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.connection import get_engine
from datetime import datetime


# Table name - use the existing typo table name
SOURCE_TABLE = 'public."Incubator 13"'
ATTENDANCE_TABLE = "public.student_attendence"
SESSION_TABLE = 'public."Inc13_Session_names.xlsx - Sheet1"'


def _ensure_attendance_schema() -> bool:
    """Ensure the attendance table exists with correct schema and unique constraint."""
    engine = get_engine()
    if engine is None:
        return False
    try:
        with engine.begin() as conn:
            # Create attendance table if not exists (only the typo table)
            conn.execute(text(f"""
                CREATE TABLE IF NOT EXISTS {ATTENDANCE_TABLE} (
                    "Timestamp" TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    "Date_of_live_secssion" DATE,
                    "College_name" VARCHAR(255),
                    "Name_of_student" VARCHAR(255) NOT NULL,
                    "subject_area_abbrevation" VARCHAR(100),
                    "attendence_status" VARCHAR(10)
                );
            """))
            # Add unique constraint to prevent duplicates (one record per student per college per date)
            # Use DO block to handle "already exists" gracefully
            conn.execute(text(f"""
                DO $$
                BEGIN
                    ALTER TABLE {ATTENDANCE_TABLE}
                    ADD CONSTRAINT uq_student_college_date 
                    UNIQUE ("Date_of_live_secssion", "College_name", "Name_of_student");
                EXCEPTION WHEN duplicate_table THEN
                    -- Constraint already exists, ignore
                END $$;
            """))
            # Create indexes
            conn.execute(text(f"""
                CREATE INDEX IF NOT EXISTS idx_{ATTENDANCE_TABLE.split('.')[-1]}_session_date 
                ON {ATTENDANCE_TABLE}("Date_of_live_secssion");
            """))
            conn.execute(text(f"""
                CREATE INDEX IF NOT EXISTS idx_{ATTENDANCE_TABLE.split('.')[-1]}_student_name 
                ON {ATTENDANCE_TABLE}("Name_of_student");
            """))
            conn.execute(text(f"""
                CREATE INDEX IF NOT EXISTS idx_{ATTENDANCE_TABLE.split('.')[-1]}_college 
                ON {ATTENDANCE_TABLE}("College_name");
            """))
        return True
    except SQLAlchemyError:
        return False


@st.cache_data(ttl=300)
def fetch_session_dates() -> list[str]:
    """Return available live session dates from session table."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        with engine.connect() as conn:
            # Parse dates from session table (format: "DD-Mon" -> "DD Month, YYYY")
            result = conn.execute(text(f'SELECT DISTINCT "Date" FROM {SESSION_TABLE} ORDER BY "Date"'))
            dates = []
            for row in result:
                date_str = row[0]
                if date_str:
                    try:
                        # Parse "DD-Mon" format (e.g., "10-Sep")
                        dt = datetime.strptime(date_str, "%d-%b")
                        # Use current year
                        dt = dt.replace(year=datetime.now().year)
                        dates.append(dt.strftime("%d %B, %Y"))
                    except ValueError:
                        # Skip invalid dates
                        continue
            return dates
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=300)
def fetch_colleges() -> list[str]:
    """Return all college names from source table (Incubator 13)."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f"""
            SELECT TRIM(college_name) as college_name
            FROM {SOURCE_TABLE}
            WHERE college_name IS NOT NULL AND TRIM(college_name) <> ''
            GROUP BY TRIM(college_name)
            ORDER BY college_name
        """
        df = pd.read_sql(query, engine)
        return df["college_name"].tolist()
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=300)
def fetch_students_by_college(college: str) -> list[dict[str, str]]:
    """Return list of student dicts for the given college from Incubator 13."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f"""
            SELECT DISTINCT TRIM(full_name) as full_name, 
                   COALESCE(NULLIF(TRIM(abbreviation), ''), 'NA') as stream
            FROM {SOURCE_TABLE}
            WHERE TRIM(college_name) = %(college)s
              AND TRIM(full_name) <> ''
            ORDER BY full_name
        """
        df = pd.read_sql(query, engine, params={"college": college})
        return [{"name": row["full_name"], "stream": row["stream"]} for _, row in df.iterrows()]
    except SQLAlchemyError:
        return []


def insert_attendance_record(
    timestamp: str,
    date_of_live_session: str,
    college_name: str,
    name_of_student: str,
    subject_area_abbrevation: str,
    attendence_status: str
) -> None:
    """
    Insert an attendance record into the database.
    """
    engine = get_engine()
    if engine is None:
        raise RuntimeError("Database engine not available")
    
    sql = f"""
    INSERT INTO {ATTENDANCE_TABLE} (
        "Timestamp", "Date_of_live_secssion", "College_name", "Name_of_student", "subject_area_abbrevation", "attendence_status"
    ) VALUES (
        :timestamp, :date_of_live_session, :college_name, :name_of_student, :subject_area_abbrevation, :attendence_status
    );
    """
    params = {
        "timestamp": timestamp,
        "date_of_live_session": date_of_live_session,
        "college_name": college_name,
        "name_of_student": name_of_student,
        "subject_area_abbrevation": subject_area_abbrevation,
        "attendence_status": attendence_status
    }
    with engine.begin() as conn:
        conn.execute(text(sql), params)


def upsert_attendance_record(
    timestamp: str,
    date_of_live_session: str,
    college_name: str,
    name_of_student: str,
    subject_area_abbrevation: str,
    attendence_status: str
) -> bool:
    """
    Insert or update attendance record (ON CONFLICT DO UPDATE).
    Returns True if inserted new, False if updated existing.
    """
    engine = get_engine()
    if engine is None:
        raise RuntimeError("Database engine not available")
    
    sql = f"""
    INSERT INTO {ATTENDANCE_TABLE} (
        "Timestamp", "Date_of_live_secssion", "College_name", "Name_of_student", "subject_area_abbrevation", "attendence_status"
    ) VALUES (
        :timestamp, :date_of_live_session, :college_name, :name_of_student, :subject_area_abbrevation, :attendence_status
    )
    ON CONFLICT ("Date_of_live_secssion", "College_name", "Name_of_student")
    DO UPDATE SET
        "Timestamp" = EXCLUDED."Timestamp",
        "subject_area_abbrevation" = EXCLUDED."subject_area_abbrevation",
        "attendence_status" = EXCLUDED."attendence_status";
    """
    params = {
        "timestamp": timestamp,
        "date_of_live_session": date_of_live_session,
        "college_name": college_name,
        "name_of_student": name_of_student,
        "subject_area_abbrevation": subject_area_abbrevation,
        "attendence_status": attendence_status
    }
    with engine.begin() as conn:
        conn.execute(text(sql), params)
    return True