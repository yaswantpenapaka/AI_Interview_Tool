"""
Streamlit session state management.
"""

import streamlit as st

DEFAULT_STATE = {
    "stage": "setup",
    "profile": {},
    "messages": [],
    "response_count": 0,
    "feedback": None,
}


def initialize_session():
    """Initialize default session state values."""
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value
