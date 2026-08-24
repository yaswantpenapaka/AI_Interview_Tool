"""
Candidate profile setup UI.
"""

import streamlit as st

from config import COMPANIES, LEVELS, POSITIONS
from interview.prompts import build_interviewer_prompt
from profile.models import CandidateProfile


def render_setup():
    """Render the interview setup screen."""
    st.subheader("Interview setup")

    st.caption(
        "Provide enough context so the interviewer can "
        "ask relevant questions."
    )

    with st.form("setup_form"):

        name = st.text_input(
            "Name",
            max_chars=50,
            placeholder="Your name",
        )

        col1, col2 = st.columns(2)

        with col1:

            level = st.selectbox(
                "Experience level",
                LEVELS,
            )

        with col2:

            position = st.selectbox(
                "Target position",
                POSITIONS,
            )

        company = st.selectbox(
            "Target company",
            COMPANIES,
        )

        experience = st.text_area(
            "Relevant experience",
            max_chars=700,
            height=120,
            placeholder=(
                "Describe your projects, responsibilities, "
                "or achievements."
            ),
        )

        skills = st.text_area(
            "Technical skills",
            max_chars=600,
            height=100,
            placeholder=(
                "For example: Python, SQL, PyTorch, "
                "Docker, AWS, Spark."
            ),
        )

        with st.expander("📋 Evaluation areas"):

            st.markdown(
                """
                The interview will assess:

                1. **Technical Accuracy**
                2. **Problem Solving**
                3. **Practical Engineering Judgment**
                4. **Communication**
                5. **Role Alignment**
                """
            )

        submitted = st.form_submit_button(
            "Start Interview",
            type="primary",
            use_container_width=True,
        )

    if not submitted:
        return

    if not name.strip():

        st.error(
            "Please enter your name."
        )
        return

    if not experience.strip():

        st.error(
            "Please describe your relevant experience."
        )
        return

    if not skills.strip():

        st.error(
            "Please list your technical skills."
        )
        return

    profile: CandidateProfile = {
        "name": name.strip(),
        "level": level,
        "position": position,
        "company": company,
        "experience": experience.strip(),
        "skills": skills.strip(),
    }

    opening_message = (
        f"Hi {profile['name']}, welcome to your "
        f"{profile['position']} interview. "
        "To begin, please introduce yourself and briefly "
        "describe one project that is most relevant to this role."
    )

    st.session_state.profile = profile

    st.session_state.messages = [
        {
            "role": "system",
            "content": build_interviewer_prompt(profile),
        },
        {
            "role": "assistant",
            "content": opening_message,
        },
    ]

    st.session_state.response_count = 0
    st.session_state.feedback = None
    st.session_state.stage = "interview"

    st.rerun()
