"""
Profile and candidate models.
"""

from typing import TypedDict


class CandidateProfile(TypedDict):
    """Candidate profile information."""
    name: str
    level: str
    position: str
    company: str
    experience: str
    skills: str
