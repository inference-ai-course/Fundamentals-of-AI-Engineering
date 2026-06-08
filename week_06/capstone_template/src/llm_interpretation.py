"""Real LLM interpretation TODOs for the capstone template."""

from __future__ import annotations

import json
from typing import Any


REQUIRED_LLM_KEYS = [
    "summary",
    "insights",
    "recommendations",
    "risk_notes",
]


def build_prompt(compressed: dict) -> str:
    """Build a structured prompt from the compressed data summary."""
    # TODO: adapt this prompt to your chosen topic.
    #
    # This is where the skill ANALYSIS happens: the model reads the compressed
    # evidence and produces structured skill insights. Two rules keep it honest:
    #   1. Tell it to use ONLY the supplied evidence (no generic career advice),
    #      and to report uncertainty (small sample, truncated text) in risk_notes.
    #   2. Ask for JSON only, so validate_llm_output() can parse it reliably.
    #
    # For the job-posting theme, request these fields and map them inside
    # report.json's `llm_interpretation` (keep the top-level report keys stable):
    #   common_skills, common_tools, role_clusters,
    #   learning_priorities, beginner_learning_path, portfolio_project_ideas
    # The default prompt below asks for generic fields; swap in the ones above.
    # See 03_skill_analysis.md for a worked example.
    return f"""You are a careful data analysis assistant.

Analyze the compressed dataset summary below.

Return ONLY valid JSON with these keys:
- summary: one paragraph
- insights: list of concise observations
- recommendations: list of concrete next actions
- risk_notes: list of risks, uncertainty, or data quality cautions

Compressed dataset summary:
{json.dumps(compressed, indent=2, sort_keys=True)}
"""


def call_llm(prompt: str, provider: str, model: str = "") -> str:
    """Call a real LLM and return raw text.

    Final submission requirement:
    - this function must call a real LLM provider
    - save the raw response in the output directory from analyze.py
    - include timeout/retry or repair handling

    Mock responses are allowed only while debugging and are not enough for final submission.
    """
    # TODO: implement the real provider call used by your class.
    # TODO: add timeout and a bounded retry or repair attempt.
    # TODO: raise a clear error if API key/model/provider settings are missing.
    raise NotImplementedError("TODO: implement call_llm() with a real LLM provider")


def validate_llm_output(raw_response: str) -> dict[str, Any]:
    """Parse and validate the LLM response.

    Expected behavior:
    - parse JSON from raw_response
    - check the required keys
    - convert missing optional lists to []
    - raise a clear error if the response cannot be repaired
    """
    # TODO: parse JSON and validate REQUIRED_LLM_KEYS.
    # TODO: optionally add one repair attempt before failing.
    raise NotImplementedError("TODO: implement validate_llm_output()")
