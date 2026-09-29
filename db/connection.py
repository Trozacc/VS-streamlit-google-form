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

    Expected keys in .streamlit/secrets.toml under [db] section:
        DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    """
    try:
        from urllib.parse import quote_plus
        password = quote_plus(st.secrets['db']['DB_PASSWORD'])
        db_url = (
            f"postgresql://{st.secrets['db']['DB_USER']}:{password}"
            f"@{st.secrets['db']['DB_HOST']}:{st.secrets['db']['DB_PORT']}"
            f"/{st.secrets['db']['DB_NAME']}"
        )
        engine = create_engine(db_url, pool_pre_ping=True)
        return engine
    except Exception as e:
        st.error(f"⚠️ Database connection failed: {e}")
        return None
