"""
Storage module — writes attendance records to PostgreSQL.
"""

import streamlit as st
from datetime import datetime
from db.connection import get_engine
from db.queries import _ensure_attendance_schema, ATTENDANCE_TABLE
from utils.helper_functions import get_ist_timestamp


def _parse_session_date(date_str: str) -> str:
    """Parse various date string formats and return YYYY-MM-DD string."""
    if not date_str:
        return datetime.now().strftime("%Y-%m-%d")
    # Try common formats
    formats = [
        "%d %B, %Y",      # "10 September, 2026"
        "%Y-%m-%d",       # "2026-09-10"
        "%d/%m/%Y",       # "10/09/2026"
        "%d-%m-%Y",       # "10-09-2026"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    # Fallback: return as-is (let DB handle or raise)
    return date_str


def store_attendance(
    session_date: str,
    college: str,
    attendance_records: list[dict],
) -> bool:
    """
    Store attendance records to the PostgreSQL database (batch insert).
    """
    try:
        # Ensure schema exists (migration)
        if not _ensure_attendance_schema():
            raise RuntimeError("Database schema not ready")

        parsed_date = _parse_session_date(session_date)
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Database engine not available")

        timestamp = get_ist_timestamp()

        # Build all rows for batch insert
        rows = []
        for record in attendance_records:
            student_name = record["name"]
            stream = record.get("stream", "NA")
            status = record["status"]

            rows.append({
                "timestamp": timestamp,
                "date_of_live_session": parsed_date,
                "college_name": college,
                "name_of_student": student_name,
                "subject_area_abbrevation": stream,
                "attendence_status": status
            })

        # Batch insert in single transaction
        from sqlalchemy import text
        sql = f"""
        INSERT INTO {ATTENDANCE_TABLE} (
            "Timestamp", "Date_of_live_secssion", "College_name", "Name_of_student", "subject_area_abbrevation", "attendence_status"
        ) VALUES (
            :timestamp, :date_of_live_session, :college_name, :name_of_student, :subject_area_abbrevation, :attendence_status
        )
        """
        with engine.begin() as conn:
            conn.execute(text(sql), rows)

        return True

    except Exception as e:
        st.error(f"❌ Failed to store attendance: {e}")
        return False
