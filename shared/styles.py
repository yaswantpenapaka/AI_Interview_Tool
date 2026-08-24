"""
Streamlit styling and branding.
"""

import streamlit as st


def apply_styles():
    """Apply custom CSS styles to the application."""
    st.markdown(
        """
        <style>

        .block-container {
            max-width: 850px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 18px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            background:
                linear-gradient(
                    135deg,
                    rgba(99, 102, 241, 0.13),
                    rgba(16, 185, 129, 0.10)
                );
        }

        .hero h1 {
            margin: 0;
            font-size: 2rem;
        }

        .hero p {
            margin: 0.45rem 0 0;
            opacity: 0.75;
        }

        [data-testid="stChatMessage"] {
            border-radius: 14px;
            border: 1px solid rgba(128, 128, 128, 0.18);
            margin-bottom: 0.6rem;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    """Render the application header."""
    st.markdown(
        """
        <div class="hero">
            <h1>🎯 AI/ML Interview Coach</h1>
            <p>
                A focused five-response technical interview
                with an evidence-based AI scorecard.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
