"""
Admin Monitoring Dashboard page.
Displays attendance analytics and monitoring views.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db.admin_queries import (
    fetch_attendance_data,
    fetch_available_dates,
    fetch_available_streams,
    fetch_available_students,
    fetch_available_statuses,
    fetch_available_colleges,
    calculate_kpis,
    get_todays_attendance,
    get_attendance_trend,
    get_stream_analysis,
    get_college_analysis,
    get_student_overview,
    get_students_needing_attention,
    get_colleges_needing_attention,
    get_recent_records,
)
from utils.auth import is_admin_authenticated, get_admin_username


def render_metric_card(label: str, value: str, accent_color: str = "#69ab4a", icon: str = ""):
    """Render a styled metric card."""
    st.markdown(
        f"""
        <div class="metric-card" style="border: 2px solid #69ab4a; border-radius: 12px; padding: 1.25rem 1.5rem; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.08); min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
            <div class="metric-icon" style="font-size: 1.5rem; margin-bottom: 0.5rem; opacity: 0.7;">{icon}</div>
            <div class="metric-label" style="font-size: 0.8rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; margin-bottom: 0.35rem;">{label}</div>
            <div class="metric-value" style="font-size: 2rem; font-weight: 800; line-height: 1.1; color: #69ab4a;">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_admin_dashboard():
    """Render the Admin Monitoring Dashboard."""
    # Check authentication
    if not is_admin_authenticated():
        st.error("Unauthorized access")
        return

    # Page header
    st.markdown(
        """
        <div class="admin-dashboard-header">
            <div>
                <h1 class="admin-dashboard-title">Attendance Monitoring Dashboard</h1>
                <p class="admin-dashboard-subtitle">Team / Admin Overview</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Refresh button
    col_refresh, _ = st.columns([1, 5])
    with col_refresh:
        if st.button("Refresh Data", key="refresh_dashboard", use_container_width=True, type="primary"):
            st.cache_data.clear()
            st.rerun()

    # Fetch all data for filters
    all_data = fetch_attendance_data()

    if all_data.empty:
        st.info("No attendance data available yet.")
        return

    # ── Filters Section ────────────────────────────────────────
    st.markdown('<div class="filters-section">', unsafe_allow_html=True)
    st.markdown('<div class="filters-title">🔍 Filters</div>', unsafe_allow_html=True)

    def reset_filters():
        st.session_state.filter_date_start = None
        st.session_state.filter_date_end = None
        st.session_state.filter_college = "All"
        st.session_state.filter_stream = "All"
        st.session_state.filter_student = "All"
        st.session_state.filter_status = "All"

    # Get filter options
    dates = fetch_available_dates()
    date_options = ["All"] + [d.strftime("%Y-%m-%d") if hasattr(d, 'strftime') else str(d) for d in dates]

    streams = fetch_available_streams()
    stream_options = ["All"] + streams

    students = fetch_available_students()
    student_options = ["All"] + students

    statuses = fetch_available_statuses()
    status_options = ["All"] + statuses

    colleges = fetch_available_colleges()
    college_options = ["All"] + colleges

    # Row 1: College (wide) | Stream / Batch
    fcol1, fcol2 = st.columns([3, 2])
    with fcol1:
        selected_college = st.selectbox("College", college_options, key="filter_college")
    with fcol2:
        selected_stream = st.selectbox("Stream / Batch", stream_options, key="filter_stream")

    # Row 2: Date Range - From and To side by side
    fcol3, fcol4 = st.columns(2)
    with fcol3:
        st.markdown('<div class="filter-label">From</div>', unsafe_allow_html=True)
        date_range_start = st.date_input("From", value=None, key="filter_date_start", label_visibility="collapsed")
    with fcol4:
        st.markdown('<div class="filter-label">To</div>', unsafe_allow_html=True)
        date_range_end = st.date_input("To", value=None, key="filter_date_end", label_visibility="collapsed")

    # Row 3: Student (wide) | Status | Clear Filters
    fcol5, fcol6, fcol7 = st.columns([2, 1, 1])
    with fcol5:
        selected_student = st.selectbox("Student", student_options, key="filter_student")
    with fcol6:
        selected_status = st.selectbox("Status", status_options, key="filter_status")
    with fcol7:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Clear Filters", key="clear_filters", use_container_width=True, on_click=reset_filters)

    st.markdown('</div>', unsafe_allow_html=True)

    # Apply filters
    filtered_data = fetch_attendance_data(
        date_range_start=date_range_start.strftime("%Y-%m-%d") if date_range_start else None,
        date_range_end=date_range_end.strftime("%Y-%m-%d") if date_range_end else None,
        college_filter=selected_college if selected_college != "All" else None,
        stream_filter=selected_stream if selected_stream != "All" else None,
        student_filter=selected_student if selected_student != "All" else None,
        status_filter=selected_status if selected_status != "All" else None,
    )

    # ── KPI Cards ──────────────────────────────────────────────
    college_for_kpi = selected_college if selected_college != "All" else None
    kpis = calculate_kpis(filtered_data, college_filter=college_for_kpi)

    # Row 1: 4 cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("Total Students", str(kpis['total_students']), "#3498db", "👥")
    with col2:
        render_metric_card("Present Today", str(kpis['present_today']), "#27ae60", "✅")
    with col3:
        render_metric_card("Absent Today", str(kpis['absent_today']), "#e74c3c", "❌")
    with col4:
        render_metric_card("Attendance %", f"{kpis['attendance_pct']}%", "#9b59b6", "📊")

    # Row 2: 2 cards (first two columns of 4-column grid)
    col5, col6, _, _ = st.columns(4)
    with col5:
        render_metric_card("Total Records", str(kpis['total_records']), "#95a5a6", "📋")
    with col6:
        render_metric_card("Total Days", str(kpis['total_days']), "#95a5a6", "📅")

    # ── Today's Attendance Chart ───────────────────────────────
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📊 Today\'s Attendance</div>', unsafe_allow_html=True)

    today_data = get_todays_attendance(filtered_data)
    if not today_data.empty:
        fig_today = px.pie(
            today_data,
            values="Count",
            names="Status",
            color="Status",
            color_discrete_map={
                "Present": "#69ab4a",
                "Absent": "#ff0000",
            },
            hole=0.5,
        )
        fig_today.update_traces(textposition='inside', textinfo='percent+label', textfont_size=14)
        fig_today.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            margin=dict(t=0, b=0, l=0, r=0),
            height=300,
        )
        st.plotly_chart(fig_today, use_container_width=True)
    else:
        st.info("No attendance data for today.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Attendance Trend Chart ─────────────────────────────────
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📈 Attendance Trend</div>', unsafe_allow_html=True)

    trend_data = get_attendance_trend(filtered_data)
    if not trend_data.empty:
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=trend_data["Date_of_live_secssion"],
            y=trend_data["attendance_pct"],
            mode="lines+markers",
            line=dict(color="#69ab4a", width=3),
            marker=dict(size=8, color="#69ab4a"),
            fill="tozeroy",
            fillcolor="rgba(105, 171, 74, 0.1)",
            name="Attendance %",
        ))
        fig_trend.update_layout(
            xaxis_title="Date",
            yaxis_title="Attendance %",
            yaxis=dict(range=[0, 105]),
            margin=dict(t=10, b=0, l=0, r=0),
            height=350,
            hovermode="x unified",
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    else:
        st.info("No trend data available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Stream / Batch Analysis ────────────────────────────────
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📚 Stream / Batch-wise Attendance</div>', unsafe_allow_html=True)

    stream_data = get_stream_analysis(filtered_data)
    if not stream_data.empty:
        fig_stream = go.Figure()
        fig_stream.add_trace(go.Bar(
            x=stream_data["Stream"],
            y=stream_data["present"],
            name="Present",
            marker_color="#69ab4a",
        ))
        fig_stream.add_trace(go.Bar(
            x=stream_data["Stream"],
            y=stream_data["absent"],
            name="Absent",
            marker_color="#ff0000",
        ))
        fig_stream.update_layout(
            barmode="group",
            xaxis_title="Stream / Batch",
            yaxis_title="Count",
            margin=dict(t=10, b=40, l=0, r=0),
            height=350,
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
            xaxis=dict(tickangle=0, tickfont=dict(size=12)),
        )
        st.plotly_chart(fig_stream, use_container_width=True)

        # Stream detail table
        st.dataframe(
            stream_data[["Stream", "present", "absent", "attendance_pct"]].rename(
                columns={"present": "Present", "absent": "Absent", "attendance_pct": "Attendance %"}
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No stream data available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── College-wise Analysis ────────────────────────────────────
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">🏫 College-wise Attendance</div>', unsafe_allow_html=True)

    college_data = get_college_analysis(filtered_data)
    if not college_data.empty:
        fig_college = go.Figure()
        fig_college.add_trace(go.Bar(
            x=college_data["College"],
            y=college_data["present"],
            name="Present",
            marker_color="#69ab4a",
        ))
        fig_college.add_trace(go.Bar(
            x=college_data["College"],
            y=college_data["absent"],
            name="Absent",
            marker_color="#ff0000",
        ))
        fig_college.update_layout(
            barmode="group",
            xaxis_title="College",
            yaxis_title="Count",
            margin=dict(t=10, b=0, l=0, r=0),
            height=350,
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        )
        st.plotly_chart(fig_college, use_container_width=True)

        # College detail table
        st.dataframe(
            college_data[["College", "present", "absent", "attendance_pct"]].rename(
                columns={"present": "Present", "absent": "Absent", "attendance_pct": "Attendance %"}
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No college data available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Student Attendance Overview ────────────────────────────
    st.markdown('<div class="data-table-container">', unsafe_allow_html=True)
    st.markdown('<div class="data-table-title">👥 Student Attendance Overview</div>', unsafe_allow_html=True)

    student_data = get_student_overview(filtered_data)
    if not student_data.empty:
        st.dataframe(
            student_data[["Student Name", "Stream / Batch", "present", "absent", "total_days", "attendance_pct"]].rename(
                columns={"present": "Present", "absent": "Absent", "total_days": "Total Days", "attendance_pct": "Attendance %"}
            ),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Attendance %": st.column_config.ProgressColumn(
                    "Attendance %",
                    min_value=0,
                    max_value=100,
                    format="%.1f%%",
                ),
            },
        )
    else:
        st.info("No student data available.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Colleges Requiring Attention ───────────────────────────────
    st.markdown('<div class="data-table-container">', unsafe_allow_html=True)
    st.markdown('<div class="data-table-title">⚠️ Colleges Requiring Attention</div>', unsafe_allow_html=True)

    # Threshold slider
    threshold = st.slider(
        "Attendance threshold (%)",
        min_value=0,
        max_value=100,
        value=70,
        step=5,
        key="attention_threshold",
        help="Show colleges with attendance below this percentage"
    )

    attention_data = get_colleges_needing_attention(filtered_data, threshold_pct=threshold)
    if not attention_data.empty:
        st.dataframe(
            attention_data[["College", "present", "absent", "attendance_pct"]].rename(
                columns={"present": "Present", "absent": "Absent", "attendance_pct": "Attendance %"}
            ),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Attendance %": st.column_config.ProgressColumn(
                    "Attendance %",
                    min_value=0,
                    max_value=100,
                    format="%.1f%%",
                ),
            },
        )
    else:
        st.success(f"✅ All colleges have attendance ≥ {threshold}%")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Recent Attendance Records ──────────────────────────────
    st.markdown('<div class="data-table-container">', unsafe_allow_html=True)
    st.markdown('<div class="data-table-title">📋 Recent Attendance Records</div>', unsafe_allow_html=True)

    recent_data = get_recent_records(filtered_data, limit=100)
    if not recent_data.empty:
        st.dataframe(
            recent_data,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No recent records.")
    st.markdown('</div>', unsafe_allow_html=True)