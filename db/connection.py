"""
Database connection module.
Creates a SQLAlchemy engine from Streamlit secrets and caches it.
"""

import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


@st.cache_resource
def get_engine() -> Engine:
    """
    Create and cache a SQLAlchemy engine using credentials from st.secrets.

    Expected keys in .streamlit/secrets.toml:
        DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    """
    try:
        db_url = (
            f"postgresql://{st.secrets['DB_USER']}:{st.secrets['DB_PASSWORD']}"
            f"@{st.secrets['DB_HOST']}:{st.secrets['DB_PORT']}"
            f"/{st.secrets['DB_NAME']}"
        )
        engine = create_engine(db_url, pool_pre_ping=True)
        return engine
    except Exception as e:
        st.error(f"⚠️ Database connection failed: {e}")
        return None
