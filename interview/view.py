"""
Interview conversation UI.
"""

import streamlit as st

from config import ANSWER_MAX_CHARS, MAX_RESPONSES
from interview.service import generate_interviewer_response


def render_interview():
    """Render the interview conversation screen."""
    profile = st.session_state.profile

    st.caption(
        f"{profile['level']} {profile['position']} "
        f"· {profile['company']}"
    )

    progress = (
        st.session_state.response_count
        / MAX_RESPONSES
    )

    st.progress(
        progress,
        text=(
            f"Candidate responses: "
            f"{st.session_state.response_count}/"
            f"{MAX_RESPONSES}"
        ),
    )

    st.caption(
        "Evaluation areas: technical accuracy · "
        "problem solving · engineering judgment · "
        "communication · role alignment"
    )

    # --------------------------------------------------------
    # Conversation history
    # --------------------------------------------------------

    for message in st.session_state.messages:

        if message["role"] == "system":
            continue

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --------------------------------------------------------
    # Interview active
    # --------------------------------------------------------

    if st.session_state.response_count < MAX_RESPONSES:

        prompt = st.chat_input(
            "Write your answer...",
            max_chars=ANSWER_MAX_CHARS,
        )

        if not prompt or not prompt.strip():
            return

        prompt = prompt.strip()

        # Save candidate response.
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        next_response_count = (
            st.session_state.response_count + 1
        )

        # ----------------------------------------------------
        # Generate next interviewer question
        # ----------------------------------------------------

        if next_response_count < MAX_RESPONSES:

            try:

                with st.chat_message("assistant"):

                    with st.spinner(
                        "Preparing the next question..."
                    ):

                        response = (
                            generate_interviewer_response(
                                st.session_state.messages
                            )
                        )

                if not response:
                    raise RuntimeError(
                        "The interviewer returned no text."
                    )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as error:

                # Remove candidate response so they can retry.
                st.session_state.messages.pop()

                st.error(
                    "The interviewer request failed. "
                    "Your answer was not submitted."
                )

                with st.expander("Technical details"):
                    st.code(str(error))

                return

        st.session_state.response_count = (
            next_response_count
        )

        st.rerun()

    # --------------------------------------------------------
    # Interview complete
    # --------------------------------------------------------

    st.success(
        "Interview complete. "
        "You can now generate your evidence-based scorecard."
    )

    if st.button(
        "Generate Scorecard",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.stage = "feedback"
        st.rerun()
