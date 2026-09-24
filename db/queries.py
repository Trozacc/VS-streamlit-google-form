"""
Database query functions.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from db.connection import get_engine


# Table name from existing database
SOURCE_TABLE = "old.incubulator_13"


@st.cache_data(ttl=300)
def fetch_session_dates() -> list[str]:
    """Return available live session dates from attendance table."""
    engine = get_engine()
    if engine is None:
        return []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DISTINCT session_date FROM attendance ORDER BY session_date"))
        return [row[0].strftime("%Y-%m-%d") if row[0] else "" for row in result]


@st.cache_data(ttl=300)
def fetch_colleges() -> list[str]:
    """Return all college names from source table."""
    engine = get_engine()
    if engine is None:
        return []
    query = f"""
        SELECT DISTINCT college_name 
        FROM {SOURCE_TABLE} 
        WHERE college_name IS NOT NULL
        ORDER BY college_name
    """
    df = pd.read_sql(query, engine)
    return df["college_name"].tolist()


@st.cache_data(ttl=300)
def fetch_students_by_college(college: str) -> list[dict[str, str]]:
    """Return list of student dicts for the given college. Each dict has keys: 'name', 'stream'."""
    engine = get_engine()
    if engine is None:
        return []
    query = f"""
        SELECT DISTINCT full_name, subject_area_abbreviation as stream
        FROM {SOURCE_TABLE}
        WHERE college_name = %(college)s
          AND full_name IS NOT NULL
        ORDER BY full_name
    """
    df = pd.read_sql(query, engine, params={"college": college})
    return [{"name": row["full_name"], "stream": row["stream"]} for _, row in df.iterrows()]


def create_attendance_table() -> None:
    """
    Create the attendance table in the database.
    """
    engine = get_engine()
    if engine is None:
        raise RuntimeError("Database engine not available")
    
    sql = """
    CREATE TABLE IF NOT EXISTS old.student_attendence (
        student_id VARCHAR(50),
        student_name VARCHAR(255),
        email VARCHAR(255),
        session_id VARCHAR(50),
        session_name VARCHAR(255),
        session_date DATE,
        duration_in_sec INTEGER,
        attendance VARCHAR(50),
        source_system VARCHAR(100)
    );
    """
    with engine.begin() as conn:
        conn.execute(text(sql))


def insert_attendance_record(
    student_id: str,
    student_name: str,
    email: str,
    session_id: str,
    session_name: str,
    session_date: str,
    duration_in_sec: int,
    attendance: str,
    source_system: str
) -> None:
    """
    Insert an attendance record into the database.
    """
    engine = get_engine()
    if engine is None:
        raise RuntimeError("Database engine not available")
    
    sql = """
    INSERT INTO attendance (
        student_id, student_name, email, session_id, session_name,
        session_date, duration_in_sec, attendance, source_system
    ) VALUES (
        :student_id, :student_name, :email, :session_id, :session_name,
        :session_date, :duration_in_sec, :attendance, :source_system
    );
    """
    params = {
        "student_id": student_id,
        "student_name": student_name,
        "email": email,
        "session_id": session_id,
        "session_name": session_name,
        "session_date": session_date,
        "duration_in_sec": duration_in_sec,
        "attendance": attendance,
        "source_system": source_system
    }
    with engine.begin() as conn:
        conn.execute(text(sql), params)