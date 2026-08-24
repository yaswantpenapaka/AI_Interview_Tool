"""
Evaluation and scorecard UI.
"""

import streamlit as st

from evaluation.service import generate_feedback


def render_feedback():
    """Render the interview scorecard screen."""
    st.subheader("📊 Interview Scorecard")

    st.caption(
        "Scores are based only on evidence demonstrated "
        "during the interview."
    )

    # --------------------------------------------------------
    # Generate feedback once
    # --------------------------------------------------------

    if st.session_state.feedback is None:

        with st.spinner(
            "Evaluating your interview..."
        ):

            try:

                st.session_state.feedback = (
                    generate_feedback(
                        st.session_state.profile,
                        st.session_state.messages,
                    )
                )

            except Exception as error:

                st.error(
                    "Feedback generation failed."
                )

                with st.expander("Technical details"):
                    st.code(str(error))

                if st.button(
                    "Retry Evaluation",
                    use_container_width=True,
                ):
                    st.rerun()

                return

    feedback = st.session_state.feedback

    # --------------------------------------------------------
    # Overall score
    # --------------------------------------------------------

    score = feedback["overall_score"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Score",
            f"{score:.1f}/10",
        )

    with col2:

        st.metric(
            "Interview Signal",
            feedback["interview_signal"],
        )

    st.markdown(
        feedback["overall_assessment"]
    )

    st.divider()

    # --------------------------------------------------------
    # Scorecard
    # --------------------------------------------------------

    st.subheader("Scorecard")

    for item in feedback["scorecard"]:

        criterion = item["criterion"]
        criterion_score = item["score"]
        evidence = item["evidence"]

        st.markdown(
            f"**{criterion} — "
            f"{criterion_score}/10**"
        )

        st.progress(
            criterion_score / 10
        )

        st.caption(evidence)

    # --------------------------------------------------------
    # Strengths
    # --------------------------------------------------------

    st.divider()

    st.subheader("💪 Strengths")

    for strength in feedback["strengths"]:
        st.markdown(f"- {strength}")

    # --------------------------------------------------------
    # Improvements
    # --------------------------------------------------------

    st.subheader("🎯 Improvements")

    for improvement in feedback["improvements"]:
        st.markdown(f"- {improvement}")

    # --------------------------------------------------------
    # Next steps
    # --------------------------------------------------------

    st.subheader("🚀 Recommended Next Steps")

    for step in feedback["next_steps"]:
        st.markdown(f"- {step}")

    # --------------------------------------------------------
    # Download report
    # --------------------------------------------------------

    from reports.markdown import feedback_to_markdown

    report = feedback_to_markdown(
        st.session_state.profile,
        feedback,
    )

    st.divider()

    st.download_button(
        label="Download Scorecard",
        data=report,
        file_name="ai_ml_interview_scorecard.md",
        mime="text/markdown",
        use_container_width=True,
    )

    # --------------------------------------------------------
    # Restart
    # --------------------------------------------------------

    if st.button(
        "Start New Interview",
        use_container_width=True,
    ):

        from streamlit_js_eval import streamlit_js_eval

        streamlit_js_eval(
            js_expressions=(
                "parent.window.location.reload()"
            ),
            key="restart_interview",
        )
