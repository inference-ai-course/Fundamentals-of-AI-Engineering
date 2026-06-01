"""Offline Week 4 demo: profile.json -> structured insight JSON.

This uses a mock LLM response so the required Week 4 parsing, validation,
repair, and logging workflow can run without an API key.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List

from pydantic import BaseModel, Field, ValidationError


class InsightReport(BaseModel):
    summary: str
    data_quality_risks: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    needs_human_review: bool


def load_profile(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Profile file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build_prompt(profile: dict[str, Any]) -> str:
    compact_profile = json.dumps(profile, sort_keys=True)
    return (
        "You are a data quality assistant.\n"
        "Task: turn the data profile into structured insights.\n"
        "Return ONLY valid JSON with exactly these keys:\n"
        "- summary: string\n"
        "- data_quality_risks: list of strings\n"
        "- recommendations: list of strings\n"
        "- needs_human_review: boolean\n"
        f"Data profile:\n{compact_profile}"
    )


def mock_llm_call(prompt: str, invalid_first: bool = False) -> str:
    if invalid_first:
        return "Here is the JSON: {'summary': 'Almost valid, but not strict JSON'}"

    needs_review = "missing_by_column" in prompt or "duplicate_rows" in prompt
    return json.dumps(
        {
            "summary": "The dataset profile was reviewed for shape, missing values, duplicates, and column summaries.",
            "data_quality_risks": [
                "Columns with missing values may affect downstream analysis.",
                "Duplicate rows can overstate counts or repeated events.",
            ],
            "recommendations": [
                "Review columns with the highest missing counts.",
                "Decide whether duplicate rows should be removed or explained.",
                "Check numeric min/max values for impossible ranges.",
            ],
            "needs_human_review": needs_review,
        },
        sort_keys=True,
    )


def repair_mock_response(raw: str) -> str:
    return json.dumps(
        {
            "summary": "The first model response was invalid JSON, so a repair attempt produced this structured report.",
            "data_quality_risks": ["The raw model response was not parseable JSON."],
            "recommendations": ["Save raw responses and cap repair attempts."],
            "needs_human_review": True,
        },
        sort_keys=True,
    )


def parse_and_validate(raw: str) -> InsightReport:
    data = json.loads(raw)
    return InsightReport.model_validate(data)


def call_with_repair(prompt: str, invalid_first: bool, max_repairs: int = 1) -> tuple[InsightReport, list[str]]:
    raw_responses = [mock_llm_call(prompt, invalid_first=invalid_first)]

    for attempt in range(max_repairs + 1):
        try:
            return parse_and_validate(raw_responses[-1]), raw_responses
        except (json.JSONDecodeError, ValidationError):
            if attempt >= max_repairs:
                raise
            raw_responses.append(repair_mock_response(raw_responses[-1]))

    raise RuntimeError("unreachable")


def write_outputs(out_dir: Path, prompt: str, raw_responses: list[str], report: InsightReport) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
    (out_dir / "raw_responses.json").write_text(json.dumps(raw_responses, indent=2), encoding="utf-8")
    (out_dir / "insights.json").write_text(report.model_dump_json(indent=2), encoding="utf-8")
    log_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "raw_response_count": len(raw_responses),
        "output": "insights.json",
    }
    with (out_dir / "llm_demo.log.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_record, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a Week 3 profile.json into mock structured LLM insights")
    parser.add_argument("--profile", required=True, help="Path to Week 3 profile.json")
    parser.add_argument("--out", default="output/week4_demo", help="Output directory")
    parser.add_argument("--invalid_first", action="store_true", help="Simulate one invalid model response before repair")
    args = parser.parse_args()

    profile = load_profile(Path(args.profile))
    prompt = build_prompt(profile)
    report, raw_responses = call_with_repair(prompt, invalid_first=args.invalid_first)
    write_outputs(Path(args.out), prompt, raw_responses, report)
    print(f"Wrote: {Path(args.out, 'insights.json').as_posix()}")
    print(f"Wrote: {Path(args.out, 'raw_responses.json').as_posix()}")


if __name__ == "__main__":
    main()
