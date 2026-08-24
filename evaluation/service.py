"""
Evaluation and feedback generation.
"""

import json
import re
from typing import Any

import streamlit as st

from ai.client import initialize_client
from config import FEEDBACK_MAX_TOKENS, MODEL
from evaluation.prompts import build_feedback_prompt
from evaluation.validator import validate_feedback
from profile.models import CandidateProfile


def build_transcript(
    messages: list[dict[str, str]],
) -> str:
    """
    Convert conversation messages into an evaluation transcript.
    """

    parts = []

    for message in messages:

        role = message["role"]

        if role == "system":
            continue

        speaker = (
            "Interviewer"
            if role == "assistant"
            else "Candidate"
        )

        parts.append(
            f"{speaker}: {message['content']}"
        )

    transcript = "\n\n".join(parts)

    # Safety limit.
    max_chars = 14000

    if len(transcript) > max_chars:
        transcript = (
            "[Earlier transcript omitted for token control]\n\n"
            + transcript[-max_chars:]
        )

    return transcript


def parse_json_response(text: str) -> dict[str, Any]:
    """
    Parse JSON even if the model accidentally adds Markdown fences
    or surrounding text.
    """

    cleaned = text.strip()

    # Remove ```json ... ``` if present.
    cleaned = re.sub(
        r"^```(?:json)?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )

    cleaned = re.sub(
        r"\s*```$",
        "",
        cleaned,
    )

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError:

        # Attempt to locate the outermost JSON object.
        start = cleaned.find("{")
        end = cleaned.rfind("}")

        if start == -1 or end == -1 or end <= start:
            raise ValueError(
                "The evaluator returned invalid JSON."
            )

        try:
            return json.loads(
                cleaned[start:end + 1]
            )

        except json.JSONDecodeError as error:
            raise ValueError(
                "The evaluator returned malformed JSON."
            ) from error


def generate_feedback(
    profile: CandidateProfile,
    messages: list[dict[str, str]],
) -> dict[str, Any]:
    """
    Generate and validate structured interview feedback.
    """
    client = initialize_client()

    transcript = build_transcript(messages)

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise, fair, evidence-based "
                    "AI/ML interview evaluator. "
                    "Return only valid JSON."
                ),
            },
            {
                "role": "user",
                "content": build_feedback_prompt(
                    profile,
                    transcript,
                ),
            },
        ],
        temperature=0.1,
        top_p=1.0,
        max_tokens=FEEDBACK_MAX_TOKENS,
    )

    content = completion.choices[0].message.content

    if not content:
        raise RuntimeError(
            "The feedback response was empty."
        )

    data = parse_json_response(content)

    return validate_feedback(data)
