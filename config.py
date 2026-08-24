"""
Configuration settings for the AI/ML Interview Coach.
"""

import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI/ML Interview Coach",
    page_icon="🎯",
    layout="centered",
)

# ============================================================
# INTERVIEW SETTINGS
# ============================================================

MAX_RESPONSES = 5
ANSWER_MAX_CHARS = 1500

INTERVIEW_MAX_TOKENS = 280
FEEDBACK_MAX_TOKENS = 900

DEFAULT_MODEL = "openai/gpt-oss-120b"

MODEL = st.secrets.get(
    "GROQ_MODEL",
    DEFAULT_MODEL,
)

# ============================================================
# INTERVIEW OPTIONS
# ============================================================

POSITIONS = [
    "Data Scientist",
    "Data Engineer",
    "ML Engineer",
    "BI Analyst",
    "Financial Analyst",
]

COMPANIES = [
    "Amazon",
    "Meta",
    "Udemy",
    "365 Company",
    "Nestle",
    "LinkedIn",
    "Spotify",
]

LEVELS = [
    "Junior",
    "Mid-level",
    "Senior",
]
