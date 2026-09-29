"""
Database query functions.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.connection import get_engine
from data.placeholder_data import SESSION_DATES, COLLEGES, STUDENTS_BY_COLLEGE


# Table name - use the existing typo table name
SOURCE_TABLE = 'public."Incubator 13"'
ATTENDANCE_TABLE = "public.student_attendence"


def _ensure_attendance_schema() -> bool:
    """Ensure the attendance table exists with correct schema."""
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
    """Return available live session dates from attendance table."""
    engine = get_engine()
    if engine is None:
        return SESSION_DATES
    try:
        _ensure_attendance_schema()
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT DISTINCT \"Date_of_live_secssion\" FROM {ATTENDANCE_TABLE} ORDER BY \"Date_of_live_secssion\""))
            dates = [row[0].strftime("%d %B, %Y") if row[0] else "" for row in result]
            if not dates:
                return SESSION_DATES
            return dates
    except SQLAlchemyError:
        return SESSION_DATES


@st.cache_data(ttl=300)
def fetch_colleges() -> list[str]:
    """Return all college names from source table."""
    engine = get_engine()
    if engine is None:
        return COLLEGES
    try:
        query = f"""
            SELECT DISTINCT TRIM(college_name) as college_name
            FROM {SOURCE_TABLE}
            WHERE college_name IS NOT NULL AND TRIM(college_name) <> ''
            ORDER BY college_name
        """
        df = pd.read_sql(query, engine)
        return df["college_name"].tolist()
    except SQLAlchemyError:
        return COLLEGES


@st.cache_data(ttl=300)
def fetch_students_by_college(college: str) -> list[dict[str, str]]:
    """Return list of student dicts for the given college. Each dict has keys: 'name', 'stream'."""
    engine = get_engine()
    if engine is None:
        return STUDENTS_BY_COLLEGE.get(college, [])
    try:
        query = f"""
            SELECT DISTINCT TRIM(full_name) as full_name, 
                   COALESCE(NULLIF(TRIM(subject_area_abbreviation), ''), 'NA') as stream
            FROM {SOURCE_TABLE}
            WHERE TRIM(college_name) = %(college)s
              AND TRIM(full_name) <> ''
            ORDER BY full_name
        """
        df = pd.read_sql(query, engine, params={"college": college})
        return [{"name": row["full_name"], "stream": row["stream"]} for _, row in df.iterrows()]
    except SQLAlchemyError:
        return STUDENTS_BY_COLLEGE.get(college, [])


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