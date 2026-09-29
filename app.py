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

    # Show success message after submission
    if st.session_state.get("show_success"):
        st.success("✅ Attendance submitted successfully.")
        st.session_state.show_success = False

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
        key="selected_date",
    )

    # College dropdown
    colleges = fetch_colleges()
    selected_college = st.selectbox(
        "Select College Name *",
        options=[""] + colleges,
        key="selected_college",
    )

    # Next button
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("Next  →", key="btn_next", use_container_width=True, type="primary"):
            if not st.session_state.selected_date:
                st.error("⚠️ Please select a session date.")
            elif not st.session_state.selected_college:
                st.error("⚠️ Please select a college name.")
            else:
                # Store confirmed values to survive widget unmounting
                st.session_state.confirmed_date = st.session_state.selected_date
                st.session_state.confirmed_college = st.session_state.selected_college
                st.session_state.attendance = {}
                st.session_state.current_section = 2
                st.rerun()


# ═══════════════════════════════════════════════════════════════
# SECTION 2 — Attendance Grid (Single-Page View with Scrollable List)
# ═══════════════════════════════════════════════════════════════
def render_section_2():
    render_section_indicator(2)

    # Use confirmed values stored at Next click; fall back to widget state
    college = st.session_state.get("confirmed_college") or st.session_state.get("selected_college", "")
    session_date = st.session_state.get("confirmed_date") or st.session_state.get("selected_date", "")
    
    # Defensive: ensure college is valid
    if not college:
        st.error("⚠️ No college selected. Please go back and select a college.")
        if st.button("← Back", key="btn_back_no_college", type="secondary"):
            st.session_state.current_section = 1
            st.rerun()
        return

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
    qa_col1, qa_col2 = st.columns(2)
    with qa_col1:
        if st.button("✅ All Present", key="btn_all_present", use_container_width=True):
            for s in students:
                name = s["name"]
                safe_name = "".join(c if c.isalnum() else "_" for c in name)
                st.session_state.attendance[name] = "Present"
                st.session_state[f"radio_{safe_name}"] = "Present"
            st.rerun()
    with qa_col2:
        if st.button("❌ All Absent", key="btn_all_absent", use_container_width=True):
            for s in students:
                name = s["name"]
                safe_name = "".join(c if c.isalnum() else "_" for c in name)
                st.session_state.attendance[name] = "Absent"
                st.session_state[f"radio_{safe_name}"] = "Absent"
            st.rerun()

    # ── Table Column Headers ──────────────────────────────────
    st.markdown(
        """
        <div class="attendance-header-bar">
            <div>#</div>
            <div style="text-align:left; padding-right: 4rem;">Student Name</div>
            <div style="text-align:center; padding-right: 4rem;">Stream</div>
            <div style="text-align:left; padding-left: 1rem;">Status</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Scrollable Student List Container (Locked Height) ────
    with st.container(height=560, border=True):
        for idx, student in enumerate(students, start=1):
            name = student["name"]
            stream = student.get("stream", "—")

            # Use columns with fixed pixel-like ratios for consistent spacing
            # Ratios: # (0.15), Name (1.2), Stream (0.9), Status (1.0)
            col_num, col_name, col_stream, col_status = st.columns([0.15, 1.2, 0.9, 1.0])

            with col_num:
                st.markdown(
                    f'<div class="student-number">{idx}</div>',
                    unsafe_allow_html=True,
                )

            with col_name:
                st.markdown(
                    f'<div class="student-name" title="{name}">{name}</div>',
                    unsafe_allow_html=True,
                )

            with col_stream:
                st.markdown(
                    f'<div class="student-stream" title="{stream}">{stream}</div>',
                    unsafe_allow_html=True,
                )

            with col_status:
                current_val = st.session_state.attendance.get(name)
                options = ["Present", "Absent"]
                # Use None for unselected (neutral) state
                default_idx = 0 if current_val == "Present" else 1 if current_val == "Absent" else None

                safe_name = "".join(c if c.isalnum() else "_" for c in name)
                status = st.radio(
                    label=f"Status for {name}",
                    options=options,
                    index=default_idx,
                    key=f"radio_{safe_name}",
                    horizontal=True,
                    label_visibility="collapsed",
                )

                if status == "Present":
                    st.session_state.attendance[name] = "Present"
                elif status == "Absent":
                    st.session_state.attendance[name] = "Absent"
                elif name in st.session_state.attendance:
                    del st.session_state.attendance[name]

    # ── Live summary stats ────────────────────────────────────
    total = len(students)
    present = sum(1 for s in students if st.session_state.attendance.get(s["name"]) == "Present")
    absent = sum(1 for s in students if st.session_state.attendance.get(s["name"]) == "Absent")
    unmarked = total - present - absent

    # Conditional CSS for spacing when fewer than 10 students
    if total < 10:
        st.markdown(
            """
            <style>
            .stats-row {
                margin-top: 0.25rem !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

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
                st.balloons()
                import time
                time.sleep(1.5)
                # Show success message and redirect to home page
                st.session_state.show_success = True
                st.session_state.current_section = 1
                st.session_state.selected_date = None
                st.session_state.selected_college = None
                st.session_state.confirmed_date = None
                st.session_state.confirmed_college = None
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
