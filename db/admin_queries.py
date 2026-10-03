"""
Admin dashboard query functions.
Reads from public.student_attendence table for monitoring dashboard.
"""

import streamlit as st
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.connection import get_engine


# Table name - same as used by the attendance form
ATTENDANCE_TABLE = "public.student_attendence"


@st.cache_data(ttl=60)
def fetch_attendance_data(
    date_filter: str = None,
    date_range_start: str = None,
    date_range_end: str = None,
    stream_filter: str = None,
    student_filter: str = None,
    status_filter: str = None,
    college_filter: str = None,
) -> pd.DataFrame:
    """
    Fetch attendance records with optional filters.
    Returns a DataFrame with columns matching the student_attendence table.
    """
    engine = get_engine()
    if engine is None:
        return pd.DataFrame()

    try:
        # Build WHERE clause dynamically
        conditions = []
        params = {}

        if date_filter:
            conditions.append('"Date_of_live_secssion" = %(date_filter)s')
            params["date_filter"] = date_filter

        if date_range_start and date_range_end:
            conditions.append('"Date_of_live_secssion" BETWEEN %(range_start)s AND %(range_end)s')
            params["range_start"] = date_range_start
            params["range_end"] = date_range_end

        if stream_filter and stream_filter != "All":
            conditions.append('"subject_area_abbrevation" = %(stream_filter)s')
            params["stream_filter"] = stream_filter

        if student_filter and student_filter != "All":
            conditions.append('"Name_of_student" = %(student_filter)s')
            params["student_filter"] = student_filter

        if status_filter and status_filter != "All":
            conditions.append('"attendence_status" = %(status_filter)s')
            params["status_filter"] = status_filter

        if college_filter and college_filter != "All":
            conditions.append('"College_name" = %(college_filter)s')
            params["college_filter"] = college_filter

        where_clause = "WHERE " + " AND ".join(conditions) if conditions else ""

        query = f"""
            SELECT 
                "Timestamp",
                "Date_of_live_secssion",
                "College_name",
                "Name_of_student",
                "subject_area_abbrevation",
                "attendence_status"
            FROM {ATTENDANCE_TABLE}
            {where_clause}
            ORDER BY "Date_of_live_secssion" DESC, "Timestamp" DESC
        """

        df = pd.read_sql(query, engine, params=params)
        return df

    except SQLAlchemyError as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()


@st.cache_data(ttl=60)
def fetch_available_dates() -> list:
    """Fetch distinct dates from attendance table for filter dropdown."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f'SELECT DISTINCT "Date_of_live_secssion" FROM {ATTENDANCE_TABLE} ORDER BY "Date_of_live_secssion" DESC'
        df = pd.read_sql(query, engine)
        return [row[0] for row in df.itertuples(index=False)]
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=60)
def fetch_available_streams() -> list:
    """Fetch distinct streams/batches from attendance table."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f'SELECT DISTINCT "subject_area_abbrevation" FROM {ATTENDANCE_TABLE} WHERE "subject_area_abbrevation" IS NOT NULL ORDER BY "subject_area_abbrevation"'
        df = pd.read_sql(query, engine)
        return [row[0] for row in df.itertuples(index=False)]
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=60)
def fetch_available_students() -> list:
    """Fetch distinct student names from attendance table."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f'SELECT DISTINCT "Name_of_student" FROM {ATTENDANCE_TABLE} ORDER BY "Name_of_student"'
        df = pd.read_sql(query, engine)
        return [row[0] for row in df.itertuples(index=False)]
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=60)
def fetch_available_statuses() -> list:
    """Fetch distinct attendance statuses from attendance table."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f'SELECT DISTINCT "attendence_status" FROM {ATTENDANCE_TABLE} WHERE "attendence_status" IS NOT NULL ORDER BY "attendence_status"'
        df = pd.read_sql(query, engine)
        return [row[0] for row in df.itertuples(index=False)]
    except SQLAlchemyError:
        return []


@st.cache_data(ttl=60)
def fetch_available_colleges() -> list:
    """Fetch distinct colleges from attendance table."""
    engine = get_engine()
    if engine is None:
        return []
    try:
        query = f'SELECT DISTINCT "College_name" FROM {ATTENDANCE_TABLE} WHERE "College_name" IS NOT NULL ORDER BY "College_name"'
        df = pd.read_sql(query, engine)
        return [row[0] for row in df.itertuples(index=False)]
    except SQLAlchemyError:
        return []


def calculate_kpis(df: pd.DataFrame) -> dict:
    """
    Calculate KPI metrics from attendance DataFrame.
    """
    if df.empty:
        return {
            "total_students": 0,
            "present_today": 0,
            "absent_today": 0,
            "attendance_pct": 0.0,
            "total_records": 0,
            "total_days": 0,
        }

    # Total unique students
    total_students = df["Name_of_student"].nunique()

    # Today's date (most recent date in data)
    today = df["Date_of_live_secssion"].max() if not df.empty else None

    if today is not None:
        today_df = df[df["Date_of_live_secssion"] == today]
        present_today = len(today_df[today_df["attendence_status"] == "Present"])
        absent_today = len(today_df[today_df["attendence_status"] == "Absent"])
    else:
        present_today = 0
        absent_today = 0

    # Attendance % = Present / Total Students * 100
    total_marked_today = present_today + absent_today
    attendance_pct = (present_today / total_students * 100) if total_students > 0 else 0.0

    # Total attendance records
    total_records = len(df)

    # Total distinct attendance days
    total_days = df["Date_of_live_secssion"].nunique()

    return {
        "total_students": int(total_students),
        "present_today": int(present_today),
        "absent_today": int(absent_today),
        "attendance_pct": round(attendance_pct, 1),
        "total_records": int(total_records),
        "total_days": int(total_days),
    }


def get_todays_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """Get attendance breakdown for today (most recent date)."""
    if df.empty:
        return pd.DataFrame()

    today = df["Date_of_live_secssion"].max()
    today_df = df[df["Date_of_live_secssion"] == today].copy()

    status_counts = today_df["attendence_status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]

    return status_counts


def get_attendance_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Get attendance percentage trend by date."""
    if df.empty:
        return pd.DataFrame()

    trend = df.groupby("Date_of_live_secssion").agg(
        total=("Name_of_student", "count"),
        present=("attendence_status", lambda x: (x == "Present").sum())
    ).reset_index()

    trend["attendance_pct"] = (trend["present"] / trend["total"] * 100).round(1)
    trend = trend.sort_values("Date_of_live_secssion")

    return trend


def get_stream_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Get attendance analysis by stream/batch."""
    if df.empty:
        return pd.DataFrame()

    stream_stats = df.groupby("subject_area_abbrevation").agg(
        total=("Name_of_student", "count"),
        present=("attendence_status", lambda x: (x == "Present").sum())
    ).reset_index()

    stream_stats["absent"] = stream_stats["total"] - stream_stats["present"]
    stream_stats["attendance_pct"] = (stream_stats["present"] / stream_stats["total"] * 100).round(1)
    stream_stats = stream_stats.rename(columns={"subject_area_abbrevation": "Stream"})
    stream_stats = stream_stats.sort_values("attendance_pct")

    return stream_stats


def get_college_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Get attendance analysis by college."""
    if df.empty:
        return pd.DataFrame()

    college_stats = df.groupby("College_name").agg(
        total=("Name_of_student", "count"),
        present=("attendence_status", lambda x: (x == "Present").sum())
    ).reset_index()

    college_stats["absent"] = college_stats["total"] - college_stats["present"]
    college_stats["attendance_pct"] = (college_stats["present"] / college_stats["total"] * 100).round(1)
    college_stats = college_stats.rename(columns={"College_name": "College"})
    college_stats = college_stats.sort_values("attendance_pct")

    return college_stats


def get_student_overview(df: pd.DataFrame) -> pd.DataFrame:
    """Get student-level attendance overview."""
    if df.empty:
        return pd.DataFrame()

    student_stats = df.groupby(["Name_of_student", "subject_area_abbrevation"]).agg(
        present=("attendence_status", lambda x: (x == "Present").sum()),
        absent=("attendence_status", lambda x: (x == "Absent").sum()),
        total_days=("Date_of_live_secssion", "nunique")
    ).reset_index()

    student_stats["attendance_pct"] = (student_stats["present"] / (student_stats["present"] + student_stats["absent"]) * 100).round(1)
    student_stats = student_stats.rename(columns={
        "Name_of_student": "Student Name",
        "subject_area_abbrevation": "Stream / Batch"
    })
    student_stats = student_stats.sort_values("attendance_pct")

    return student_stats


def get_students_needing_attention(df: pd.DataFrame, threshold_pct: float = 70.0) -> pd.DataFrame:
    """Get students with attendance below threshold."""
    student_overview = get_student_overview(df)
    if student_overview.empty:
        return pd.DataFrame()

    attention = student_overview[student_overview["attendance_pct"] < threshold_pct].copy()
    return attention


def get_recent_records(df: pd.DataFrame, limit: int = 50) -> pd.DataFrame:
    """Get most recent attendance records."""
    if df.empty:
        return pd.DataFrame()

    recent = df.head(limit).copy()
    recent = recent.rename(columns={
        "Name_of_student": "Student Name",
        "subject_area_abbrevation": "Stream / Batch",
        "Date_of_live_secssion": "Date",
        "attendence_status": "Status",
        "Timestamp": "Submission Time"
    })
    # College name column
    if "College_name" in recent.columns:
        recent = recent.rename(columns={"College_name": "College"})

    # Select only columns that exist
    display_cols = ["Student Name", "Stream / Batch", "Date", "Status", "Submission Time"]
    if "College" in recent.columns:
        display_cols.insert(0, "College")

    return recent[display_cols]