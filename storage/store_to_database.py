"""
Storage module — writes attendance records to PostgreSQL.
"""

import pandas as pd
import streamlit as st
from db.connection import get_engine
from utils.helper_functions import get_ist_timestamp


def store_attendance(
    session_date: str,
    college: str,
    attendance_records: list[dict],
) -> bool:
    """
    Store attendance records to the PostgreSQL database using pandas to_sql.

    Parameters
    ----------
    session_date : str
        The date of the live session.
    college : str
        The college name.
    attendance_records : list[dict]
        List of dicts with keys: 'name', 'stream', 'status' (Present/Absent).

    Returns
    -------
    bool
        True if storage succeeded, False otherwise.
    """
    try:
        timestamp = get_ist_timestamp()

        rows = []
        for record in attendance_records:
            student_name = record["name"]
            student_id = student_name.lower().replace(" ", "_")
            session_id = f"{college}_{session_date}".replace(" ", "_").replace(",", "")
            session_name = f"Live Session {session_date}"
            
            rows.append({
                "student_id": student_id,
                "student_name": student_name,
                "email": "",
                "session_id": session_id,
                "session_name": session_name,
                "session_date": session_date,
                "duration_in_sec": 0,
                "attendance": record["status"],
                "source_system": "Vigyan Shaala App",
                "timestamp": timestamp,
                "college": college,
            })

        df = pd.DataFrame(rows)
        engine = get_engine()
        
        if engine is None:
            raise RuntimeError("Database engine not available")

        df.to_sql(
            "student_attendence",
            engine,
            schema="old",
            if_exists="append",
            index=False,
            method="multi"
        )

        return True

    except Exception as e:
        st.error(f"❌ Failed to store attendance: {e}")
        return False
