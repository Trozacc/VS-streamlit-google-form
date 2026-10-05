"""
Admin authentication module.
Handles login/logout for the Admin Monitoring Dashboard.
"""

import streamlit as st


def check_admin_credentials(username: str, password: str) -> bool:
    """Verify admin credentials against Streamlit secrets."""
    try:
        admin_user = st.secrets.get("admin", {}).get("ADMIN_USERNAME", "")
        admin_pass = st.secrets.get("admin", {}).get("ADMIN_PASSWORD", "")
        return username == admin_user and password == admin_pass
    except Exception:
        return False


def render_admin_login() -> bool:
    """
    Render the admin login form.
    Returns True if login successful, False otherwise.
    """
    st.markdown(
        """
        <div class="admin-login-container">
            <div class="admin-login-card">
                <div class="admin-login-header">
                    <h2>🔐 Team / Admin Login</h2>
                    <p>Enter credentials to access the Monitoring Dashboard</p>
                </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("admin_login_form", clear_on_submit=False):
        username = st.text_input("Username", key="admin_username_input", placeholder="Enter username")
        password = st.text_input("Password", type="password", key="admin_password_input", placeholder="Enter password")
        col_login, col_cancel = st.columns(2)
        with col_login:
            submitted = st.form_submit_button("Login", use_container_width=True, type="primary")
        with col_cancel:
            cancelled = st.form_submit_button("Cancel", use_container_width=True, type="secondary")

        if submitted:
            if check_admin_credentials(username, password):
                st.session_state.admin_authenticated = True
                st.session_state.admin_username = username
                st.session_state.show_admin_login = False
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

        if cancelled:
            st.session_state.show_admin_login = False
            st.rerun()

    st.markdown(
        """
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return False


def is_admin_authenticated() -> bool:
    """Check if admin is currently authenticated."""
    return st.session_state.get("admin_authenticated", False)


def get_admin_username() -> str:
    """Get the authenticated admin username."""
    return st.session_state.get("admin_username", "")