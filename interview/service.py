"""
Interview generation and management.
"""

from ai.client import initialize_client
from ai.streaming import write_stream
from config import INTERVIEW_MAX_TOKENS, MODEL


def generate_interviewer_response(
    messages: list[dict[str, str]],
) -> str:
    """
    Generate the next interview question.
    """
    client = initialize_client()

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.35,
        top_p=1.0,
        max_tokens=INTERVIEW_MAX_TOKENS,
        stream=True,
    )

    response = write_stream(stream)

    return str(response).strip()
