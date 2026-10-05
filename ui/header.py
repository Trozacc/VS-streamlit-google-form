"""
Header component — renders the responsive Vigyan Shaala logo and page title.
"""

import os
import base64
import streamlit as st
from constants import APP_TITLE, APP_SUBTITLE
from utils.auth import is_admin_authenticated


def render_header(show_admin_button: bool = True):
    """Display a compact, responsive Vigyan Shaala logo and form title."""
    
    # ── Centered logo and title ────
    _render_logo_and_title()
    
    # Logout/Team Login button - rendered but positioned via CSS (fixed top-right)
    if show_admin_button and is_admin_authenticated():
        if st.button("🚪 Logout", key="admin_logout_btn", type="secondary"):
            st.session_state.admin_authenticated = False
            st.session_state.admin_username = None
            st.session_state.current_section = 1
            st.rerun()
    elif show_admin_button:
        if st.button("👥 Team Login", key="team_login_btn", type="secondary"):
            st.session_state.show_admin_login = True
            st.rerun()


def _render_logo_and_title():
    """Render logo and title (centered)."""
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