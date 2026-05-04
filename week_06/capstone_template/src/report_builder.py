"""Report-building TODOs for the capstone template."""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_REPORT_KEYS = [
    "metadata",
    "dataset_summary",
    "data_quality",
    "compression_summary",
    "llm_interpretation",
    "recommendations",
    "risk_notes",
    "errors_or_warnings",
]


def build_json_report(profile: dict, compressed: dict, llm_output: dict) -> dict:
    """Combine profile, compression, and LLM output into final JSON.

    The final object should preserve REQUIRED_REPORT_KEYS.
    """
    # TODO: construct a stable report dict with all required top-level keys.
    raise NotImplementedError("TODO: implement build_json_report()")


def build_markdown_report(json_report: dict) -> str:
    """Build a human-readable Markdown report from the JSON report."""
    # TODO: include dataset overview, data quality notes, LLM interpretation,
    # recommendations, risk notes, and any warnings/errors.
    raise NotImplementedError("TODO: implement build_markdown_report()")


def write_report_files(output_dir: Path, json_report: dict, markdown_report: str) -> None:
    """Write output/report.json and output/report.md."""
    # TODO: ensure output_dir exists and write both final files.
    # TODO: use json.dumps(..., indent=2, sort_keys=True) for stable JSON.
    raise NotImplementedError("TODO: implement write_report_files()")


def assert_required_report_keys(report: dict) -> None:
    """Optional helper students can use in tests or smoke checks."""
    missing = [key for key in REQUIRED_REPORT_KEYS if key not in report]
    if missing:
        raise ValueError(f"report is missing required keys: {missing}")


def preview_json(report: dict) -> str:
    """Optional helper for debugging."""
    return json.dumps(report, indent=2, sort_keys=True)
