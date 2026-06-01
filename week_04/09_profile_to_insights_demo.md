# Week 4 — Required Demo: Profile JSON to Structured Insights

## Overview

Week 3 produced `profile.json`. Week 4 turns that machine-readable profile into structured insight output that code can validate.

This required demo uses a mock LLM response so every student can practice:

- prompt contracts
- structured JSON validation
- bounded repair attempts
- saved raw responses
- simple logging

No API key is required.

## Input And Output

Input:

- Week 3 `profile.json`

Output:

- `prompt.txt`
- `raw_responses.json`
- `insights.json`
- `llm_demo.log.jsonl`

The validated insight schema is:

```json
{
  "summary": "string",
  "data_quality_risks": ["string"],
  "recommendations": ["string"],
  "needs_human_review": true
}
```

## Setup

From `week_04/`, install the required Week 4 dependencies in your active course environment:

```bash
pip install -r requirements.txt
```

## Run The Happy Path

Use a Week 3 profile file:

```bash
python profile_to_insights_demo.py --profile ../week_03/output/profile.json --out output/profile_insights
```

Then inspect:

```bash
cat output/profile_insights/insights.json
cat output/profile_insights/raw_responses.json
```

## Run The Repair Path

This simulates a first response that is not valid JSON:

```bash
python profile_to_insights_demo.py --profile ../week_03/output/profile.json --out output/profile_insights_repair --invalid_first
```

The script should save both the invalid raw response and the repaired response, then write a valid `insights.json`.

## What to Complete

For Week 4, document:

- the prompt contract
- `raw_responses.json`
- `insights.json`
- a short note explaining whether the happy path or repair path was used
- one failure mode and how the code made it debuggable

## Self-Check

- Can you explain why `profile.json` is safer to send than a full CSV?
- Can you point to the exact schema used to validate model output?
- Can you show the saved raw response for debugging?
- Does the required demo work without an API key?
