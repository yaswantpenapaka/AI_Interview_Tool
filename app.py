"""
AI/ML Interview Coach — V3
────────────────────────────────────────────────────────────
Features:
• Groq API through the OpenAI-compatible SDK
• Adaptive 5-response AI/ML interview
• Evidence-based evaluation
• Structured JSON scoring
• Streaming interviewer responses
• Cached API client
• Error recovery
• Downloadable Markdown scorecard
• Clean Streamlit state management
"""

import streamlit as st

from evaluation.view import render_feedback
from interview.view import render_interview
from profile.view import render_setup
from shared.session import initialize_session
from shared.styles import apply_styles, render_header

# ============================================================
# INITIALIZATION
# ============================================================

apply_styles()
render_header()
initialize_session()

# ============================================================
# APPLICATION ROUTING
# ============================================================

if st.session_state.stage == "setup":

    render_setup()

elif st.session_state.stage == "interview":

    render_interview()

elif st.session_state.stage == "feedback":

    render_feedback()
