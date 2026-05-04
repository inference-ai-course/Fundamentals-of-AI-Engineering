"""CLI skeleton for the Week 6 capstone.

This file is intentionally incomplete. Students should fill in the TODOs with
AI Agent Coding Tool assistance and personal verification.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from src.compression import compress_profile
from src.data_profile import build_profile, load_csv
from src.llm_interpretation import build_prompt, call_llm, validate_llm_output
from src.report_builder import build_json_report, build_markdown_report, write_report_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI-assisted CSV data analyzer")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--out", default="output", help="Output directory")
    parser.add_argument("--provider", default="openai-compatible", help="LLM provider name")
    parser.add_argument("--model", default="", help="Model name required by your provider")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    # TODO: load_csv should read and validate the input CSV.
    df = load_csv(input_path)

    # TODO: build_profile should compute the required data profiling fields.
    profile = build_profile(df)

    # TODO: compress_profile should avoid sending the full CSV to the LLM.
    compressed = compress_profile(profile, df)

    # TODO: build_prompt should create a structured prompt for a real LLM.
    prompt = build_prompt(compressed)
    (output_dir / "llm_prompt.txt").write_text(prompt, encoding="utf-8")

    # TODO: call_llm must perform a real LLM call for final submission.
    raw_response = call_llm(prompt=prompt, provider=args.provider, model=args.model)
    (output_dir / "llm_raw_response.txt").write_text(raw_response, encoding="utf-8")

    # TODO: validate_llm_output should parse/repair/check expected fields.
    llm_output = validate_llm_output(raw_response)

    # TODO: build report objects and write output/report.json + output/report.md.
    json_report = build_json_report(profile=profile, compressed=compressed, llm_output=llm_output)
    markdown_report = build_markdown_report(json_report)
    write_report_files(output_dir=output_dir, json_report=json_report, markdown_report=markdown_report)


if __name__ == "__main__":
    main()
