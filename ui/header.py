"""
Header component — renders the responsive Vigyan Shaala logo and page title.
"""

import os
import base64
import streamlit as st
from constants import APP_TITLE, APP_SUBTITLE
from utils.auth import is_admin_authenticated, render_admin_logout_button


def render_header(show_admin_button: bool = True):
    """Display a compact, responsive Vigyan Shaala logo and form title."""

    # ── Top bar with logo/title on left, admin button on right ────
    if show_admin_button:
        col_left, col_right = st.columns([5, 1])

        with col_left:
            _render_logo_and_title()

        with col_right:
            _render_admin_button_area()
    else:
        _render_logo_and_title()


def _render_logo_and_title():
    """Render logo and title (left side of header)."""
    # ── Logo ──────────────────────────────────────────────────
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cover.jpg")

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
        f"""
        <div class="form-title-container">
            <h1 class="form-title">{APP_TITLE}</h1>
            <p class="form-subtitle">{APP_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_admin_button_area():
    """Render admin login/logout button (right side of header)."""
    if is_admin_authenticated():
        # Show logout button when authenticated
        render_admin_logout_button()
    else:
        # Show login button when not authenticated
        st.markdown("<div style='margin-top: 1.5rem;'>", unsafe_allow_html=True)
        if st.button("👥 Team Login", key="team_login_btn", use_container_width=True, type="secondary"):
            st.session_state.show_admin_login = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)