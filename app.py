"""
Vigyan Shaala — NEW BATCH August 2026: Attendance
Main Streamlit application — Optimized for One-Page non-scrollable viewport.
"""

import streamlit as st
from ui.style import inject_styles
from ui.header import render_header
from db.queries import fetch_session_dates, fetch_colleges, fetch_students_by_college
from storage.store_to_database import store_attendance
from utils.helper_functions import validate_attendance

# ─── Page Configuration ───────────────────────────────────────
st.set_page_config(
    page_title="Vigyan Shaala — Attendance",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Inject Custom Styles ────────────────────────────────────
inject_styles()

# ─── Render Header (logo + title) ────────────────────────────
render_header()

# ─── Session State Initialization ────────────────────────────
if "current_section" not in st.session_state:
    st.session_state.current_section = 1
if "selected_date" not in st.session_state:
    st.session_state.selected_date = None
if "selected_college" not in st.session_state:
    st.session_state.selected_college = None
if "attendance" not in st.session_state:
    st.session_state.attendance = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False


# ═══════════════════════════════════════════════════════════════
# SECTION INDICATOR
# ═══════════════════════════════════════════════════════════════
def render_section_indicator(active: int):
    """Render the compact step indicator dots."""
    dots = ""
    for i in range(1, 3):
        cls = "section-dot active" if i == active else "section-dot"
        dots += f'<div class="{cls}"></div>'
    st.markdown(f'<div class="section-indicator">{dots}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECTION 1 — Date & College Selection
# ═══════════════════════════════════════════════════════════════
def render_section_1():
    render_section_indicator(1)

    st.markdown(
        """
        <div class="form-card">
            <div class="form-card-header">📋 Session Details</div>
            <div class="form-card-description">
                Select the live session date and college name to open the attendance roster.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Date dropdown
    dates = fetch_session_dates()
    selected_date = st.selectbox(
        "Date of the Live Session *",
        options=[""] + dates,
        index=0 if not st.session_state.selected_date else ([""] + dates).index(st.session_state.selected_date) if st.session_state.selected_date in ([""] + dates) else 0,
        key="date_select",
    )

    # College dropdown
    colleges = fetch_colleges()
    selected_college = st.selectbox(
        "Select College Name *",
        options=[""] + colleges,
        index=0 if not st.session_state.selected_college else ([""] + colleges).index(st.session_state.selected_college) if st.session_state.selected_college in ([""] + colleges) else 0,
        key="college_select",
    )

    # Next button
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("Next  →", key="btn_next", use_container_width=True, type="primary"):
            if not selected_date:
                st.error("⚠️ Please select a session date.")
            elif not selected_college:
                st.error("⚠️ Please select a college name.")
            else:
                st.session_state.selected_date = selected_date
                st.session_state.selected_college = selected_college
                st.session_state.attendance = {}
                st.session_state.current_section = 2
                st.rerun()


# ═══════════════════════════════════════════════════════════════
# SECTION 2 — Attendance Grid (Single-Page View with Scrollable List)
# ═══════════════════════════════════════════════════════════════
def render_section_2():
    render_section_indicator(2)

    college = st.session_state.selected_college
    session_date = st.session_state.selected_date
    students = fetch_students_by_college(college)

    # ── College header bar ────────────────────────────────────
    st.markdown(
        f"""
        <div class="college-header">
            <div class="college-name">🏫 {college} &nbsp;<span style="color:#8B949E; font-size:0.8rem; font-weight:400;">({session_date})</span></div>
            <div class="student-count">{len(students)} Student{"s" if len(students) != 1 else ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── No students case ──────────────────────────────────────
    if not students:
        st.markdown(
            """
            <div class="form-card" style="text-align:center; padding:1.5rem;">
                <div class="form-card-header" style="justify-content:center;">🚫 No Students Found</div>
                <div class="form-card-description">
                    No student roster records found for this college yet.<br>
                    Data will load once PostgreSQL is connected.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("← Back", key="btn_back_empty", type="secondary"):
            st.session_state.current_section = 1
            st.rerun()
        return

    # ── Quick actions bar ─────────────────────────────────────
    qa_col1, qa_col2, qa_col3 = st.columns(3)
    with qa_col1:
        if st.button("✅ All Present", key="btn_all_present", use_container_width=True):
            for s in students:
                st.session_state.attendance[s["name"]] = "Present"
            st.rerun()
    with qa_col2:
        if st.button("❌ All Absent", key="btn_all_absent", use_container_width=True):
            for s in students:
                st.session_state.attendance[s["name"]] = "Absent"
            st.rerun()
    with qa_col3:
        if st.button("🔄 Reset", key="btn_reset", use_container_width=True):
            st.session_state.attendance = {}
            st.rerun()

    # ── Table Column Headers ──────────────────────────────────
    st.markdown(
        """
        <div class="attendance-header-bar">
            <div>#</div>
            <div>Student Name</div>
            <div>Stream</div>
            <div style="text-align:center;">Status</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Scrollable Student List Container (Locked Height) ────
    with st.container(height=560, border=True):
        for idx, student in enumerate(students, start=1):
            name = student["name"]
            stream = student.get("stream", "—")

            col_num, col_name, col_stream, col_status = st.columns([0.25, 1.15, 0.9, 1.3])

            with col_num:
                st.markdown(
                    f'<div style="padding-top:0.35rem;"><span class="student-number">{idx}</span></div>',
                    unsafe_allow_html=True,
                )

            with col_name:
                st.markdown(
                    f'<div style="padding-top:0.35rem;"><span class="student-name" title="{name}">{name}</span></div>',
                    unsafe_allow_html=True,
                )

            with col_stream:
                st.markdown(
                    f'<div style="padding-top:0.35rem;"><span class="student-stream" title="{stream}">{stream}</span></div>',
                    unsafe_allow_html=True,
                )

            with col_status:
                current_val = st.session_state.attendance.get(name)
                options = ["Present", "Absent"]
                default_idx = None
                if current_val == "Present":
                    default_idx = 0
                elif current_val == "Absent":
                    default_idx = 1

                status = st.radio(
                    label=f"Status for {name}",
                    options=options,
                    index=default_idx,
                    key=f"radio_{name}",
                    horizontal=True,
                    label_visibility="collapsed",
                )

                if status:
                    st.session_state.attendance[name] = status

    # ── Live summary stats ────────────────────────────────────
    total = len(students)
    present = sum(1 for s in students if st.session_state.attendance.get(s["name"]) == "Present")
    absent = sum(1 for s in students if st.session_state.attendance.get(s["name"]) == "Absent")
    unmarked = total - present - absent

    st.markdown(
        f"""
        <div class="stats-row">
            <div class="stat-card stat-total">
                <div class="stat-value">{total}</div>
                <div class="stat-label">Total</div>
            </div>
            <div class="stat-card stat-present">
                <div class="stat-value">{present}</div>
                <div class="stat-label">Present</div>
            </div>
            <div class="stat-card stat-absent">
                <div class="stat-value">{absent}</div>
                <div class="stat-label">Absent</div>
            </div>
            <div class="stat-card stat-unmarked">
                <div class="stat-value">{unmarked}</div>
                <div class="stat-label">Unmarked</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Action buttons ────────────────────────────────────────
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("← Back", key="btn_back", use_container_width=True, type="secondary"):
            st.session_state.current_section = 1
            st.rerun()

    with btn_col2:
        if st.button("Submit Attendance ✓", key="btn_submit", use_container_width=True, type="primary"):
            student_names = [s["name"] for s in students]
            is_valid, error_msg = validate_attendance(st.session_state.attendance, student_names)

            if not is_valid:
                st.error(f"⚠️ {error_msg}")
                st.stop()

            # Build records
            records = []
            for s in students:
                records.append({
                    "name": s["name"],
                    "stream": s.get("stream", "NA"),
                    "status": st.session_state.attendance[s["name"]],
                })

            success = store_attendance(
                session_date=session_date,
                college=college,
                attendance_records=records,
            )

            if success:
                st.session_state.submitted = True
                st.session_state.current_section = 3
                st.rerun()


# ═══════════════════════════════════════════════════════════════
# SECTION 3 — Success / Thank You
# ═══════════════════════════════════════════════════════════════
def render_success():
    st.balloons()

    college = st.session_state.selected_college
    session_date = st.session_state.selected_date
    attendance = st.session_state.attendance
    total = len(attendance)
    present = sum(1 for v in attendance.values() if v == "Present")
    absent = total - present

    st.markdown(
        f"""
        <div class="success-box">
            <h3>🎉 Attendance Submitted Successfully!</h3>
            <p>
                <strong>{college}</strong><br>
                Session: {session_date}<br><br>
                ✅ Present: <strong>{present}</strong> &nbsp;|&nbsp;
                ❌ Absent: <strong>{absent}</strong> &nbsp;|&nbsp;
                📊 Total: <strong>{total}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("📝 Submit Another", key="btn_another", use_container_width=True, type="primary"):
            st.session_state.current_section = 1
            st.session_state.selected_date = None
            st.session_state.selected_college = None
            st.session_state.attendance = {}
            st.session_state.submitted = False
            st.rerun()


# ═══════════════════════════════════════════════════════════════
# ROUTER
# ═══════════════════════════════════════════════════════════════
section = st.session_state.current_section

if section == 1:
    render_section_1()
elif section == 2:
    render_section_2()
elif section == 3:
    render_success()
