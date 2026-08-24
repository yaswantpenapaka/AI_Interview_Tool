"""
Streaming response handling for OpenAI-compatible APIs.
"""

import streamlit as st


def text_chunks(stream):
    """
    Safely extract text from a streaming OpenAI-compatible response.
    """
    for chunk in stream:
        if not chunk.choices:
            continue

        content = chunk.choices[0].delta.content

        if content:
            yield content


def write_stream(stream):
    """
    Write streaming response to Streamlit UI.
    """
    response = st.write_stream(text_chunks(stream))
    return str(response).strip()
