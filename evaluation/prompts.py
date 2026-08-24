"""
Evaluation and feedback prompt builders.
"""

from profile.models import CandidateProfile


def build_feedback_prompt(
    profile: CandidateProfile,
    transcript: str,
) -> str:
    """
    Build the structured evaluation prompt.
    """

    return f"""
You are an objective AI/ML interview evaluator.

Evaluate ONLY evidence present in the transcript.

Do not invent:
- Projects
- Technologies
- Results
- Responsibilities
- Skills
- Experience
- Achievements

If something was not demonstrated, explicitly say:
"Not demonstrated in the interview."

CANDIDATE
---------
Name: {profile["name"]}
Target level: {profile["level"]}
Target position: {profile["position"]}
Company context: {profile["company"]}
Experience: {profile["experience"]}
Skills: {profile["skills"]}

RUBRIC
------

Score every criterion from 1 to 10.

1. Technical Accuracy
Correctness of concepts, terminology, implementation details,
assumptions, and technical explanations.

2. Problem Solving
Logical reasoning, diagnosis, assumptions, experimentation,
validation, and ability to break down difficult problems.

3. Practical Engineering Judgment
Trade-offs involving data quality, testing, reproducibility,
scalability, deployment, monitoring, reliability, or business
impact where relevant.

4. Communication
Clarity, organization, conciseness, confidence, and ability
to explain technical decisions.

5. Role Alignment
Depth and relevance of evidence for the target position and
experience level.

SCORING GUIDE
-------------
1-3  = Major gaps or very little supporting evidence
4-6  = Partial understanding or inconsistent evidence
7-8  = Strong and relevant evidence
9-10 = Exceptional depth, precision, and practical judgment

OVERALL SCORE
-------------
Calculate the arithmetic average of the five criterion scores.

Round the result to one decimal place.

INTERVIEW SIGNAL
----------------
Choose exactly one:

"Strong signal"
"Promising"
"Needs more evidence"
"Not ready yet"

Return ONLY valid JSON.

Use exactly this schema:

{{
  "overall_score": 0.0,
  "interview_signal": "Promising",
  "overall_assessment": "Short evidence-based assessment.",
  "scorecard": [
    {{
      "criterion": "Technical Accuracy",
      "score": 0,
      "evidence": "Brief evidence."
    }},
    {{
      "criterion": "Problem Solving",
      "score": 0,
      "evidence": "Brief evidence."
    }},
    {{
      "criterion": "Practical Engineering Judgment",
      "score": 0,
      "evidence": "Brief evidence."
    }},
    {{
      "criterion": "Communication",
      "score": 0,
      "evidence": "Brief evidence."
    }},
    {{
      "criterion": "Role Alignment",
      "score": 0,
      "evidence": "Brief evidence."
    }}
  ],
  "strengths": [
    "Specific evidence-based strength.",
    "Specific evidence-based strength.",
    "Specific evidence-based strength."
  ],
  "improvements": [
    "Specific actionable improvement.",
    "Specific actionable improvement.",
    "Specific actionable improvement."
  ],
  "next_steps": [
    "Practical preparation action.",
    "Practical preparation action.",
    "Practical preparation action."
  ]
}}

IMPORTANT:
- Every score must be an integer from 1 to 10.
- Overall score must equal the average of the five scores.
- Do not add extra JSON fields.
- Do not wrap the JSON in Markdown code fences.

TRANSCRIPT
----------
BEGIN TRANSCRIPT

{transcript}

END TRANSCRIPT
"""
