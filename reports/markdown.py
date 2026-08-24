"""
Markdown report generation.
"""

from typing import Any

from profile.models import CandidateProfile


def feedback_to_markdown(
    profile: CandidateProfile,
    feedback: dict[str, Any],
) -> str:
    """
    Convert structured feedback into a downloadable Markdown report.
    """

    lines = [
        "# AI/ML Interview Scorecard",
        "",
        f"**Candidate:** {profile['name']}",
        f"**Target role:** {profile['level']} {profile['position']}",
        f"**Company context:** {profile['company']}",
        "",
        "## Overall Assessment",
        "",
        f"**Overall score:** "
        f"{feedback['overall_score']:.1f}/10",
        "",
        f"**Interview signal:** "
        f"{feedback['interview_signal']}",
        "",
        feedback["overall_assessment"],
        "",
        "## Scorecard",
        "",
        "| Criterion | Score | Evidence |",
        "|---|---:|---|",
    ]

    for item in feedback["scorecard"]:

        lines.append(
            f"| {item['criterion']} "
            f"| {item['score']}/10 "
            f"| {item['evidence']} |"
        )

    lines.extend(
        [
            "",
            "## Strengths",
            "",
        ]
    )

    for strength in feedback["strengths"]:
        lines.append(f"- {strength}")

    lines.extend(
        [
            "",
            "## Improvements",
            "",
        ]
    )

    for improvement in feedback["improvements"]:
        lines.append(f"- {improvement}")

    lines.extend(
        [
            "",
            "## Recommended Next Steps",
            "",
        ]
    )

    for step in feedback["next_steps"]:
        lines.append(f"- {step}")

    return "\n".join(lines)
