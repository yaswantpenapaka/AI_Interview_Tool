"""
Evaluation feedback validation.
"""

from typing import Any

REQUIRED_CRITERIA = [
    "Technical Accuracy",
    "Problem Solving",
    "Practical Engineering Judgment",
    "Communication",
    "Role Alignment",
]


def validate_feedback(data: dict[str, Any]) -> dict[str, Any]:
    """
    Validate the evaluator output before displaying it.
    """

    required_fields = [
        "overall_score",
        "interview_signal",
        "overall_assessment",
        "scorecard",
        "strengths",
        "improvements",
        "next_steps",
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(
                f"Evaluator response is missing '{field}'."
            )

    if not isinstance(data["scorecard"], list):
        raise ValueError(
            "Scorecard must be a list."
        )

    scores = {}

    for item in data["scorecard"]:

        criterion = item.get("criterion")
        score = item.get("score")

        if criterion not in REQUIRED_CRITERIA:
            continue

        if not isinstance(score, int):
            raise ValueError(
                f"Invalid score for {criterion}."
            )

        if score < 1 or score > 10:
            raise ValueError(
                f"Score for {criterion} must be between 1 and 10."
            )

        scores[criterion] = score

    missing = [
        criterion
        for criterion in REQUIRED_CRITERIA
        if criterion not in scores
    ]

    if missing:
        raise ValueError(
            f"Missing scoring criteria: {', '.join(missing)}"
        )

    calculated_average = round(
        sum(scores.values()) / len(scores),
        1,
    )

    model_average = round(
        float(data["overall_score"]),
        1,
    )

    # Trust our calculation rather than an inconsistent model average.
    data["overall_score"] = calculated_average

    if abs(model_average - calculated_average) > 0.2:
        # Keep calculated value.
        data["overall_score"] = calculated_average

    return data
