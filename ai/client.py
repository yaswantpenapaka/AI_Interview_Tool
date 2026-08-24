"""
Groq API client initialization and caching.
"""

import streamlit as st
from openai import OpenAI

from config import MODEL


@st.cache_resource
def get_client(api_key: str) -> OpenAI:
    """
    Create and reuse one Groq client.
    """
    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        timeout=45.0,
        max_retries=2,
    )


def initialize_client() -> OpenAI:
    """Initialize and return the Groq client, or stop if API key is missing."""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except KeyError:
        st.error(
            "GROQ_API_KEY is missing. "
            "Add it to .streamlit/secrets.toml."
        )
        st.stop()

    return get_client(api_key)
