"""
Header component — renders the responsive Vigyan Shaala logo and page title.
"""

import os
import base64
import streamlit as st


def render_header():
    """Display a compact, responsive Vigyan Shaala logo and form title."""

    # ── Logo ──────────────────────────────────────────────────
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images.jpg")

    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <div class="logo-header-bg">
                <div class="logo-container">
                    <img src="data:image/jpeg;base64,{logo_b64}" alt="Vigyan Shaala Logo" class="logo-img" />
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Logo file not found.")

    # ── Title ─────────────────────────────────────────────────
    st.markdown(
        """
        <div class="form-title-container">
            <h1 class="form-title">NEW BATCH August 2026: Attendance</h1>
            <p class="form-subtitle">Faculty Mentors to verify Nominations &amp; Confirm</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
