# Capstone Template: AI-Assisted CSV Data Analyzer

This is a scaffold for the Week 6 capstone. It is intentionally incomplete.

Target pipeline:

```text
CSV input -> data profile -> compressed summary -> real LLM interpretation -> report.json + report.md
```

## What You Must Complete

Look for `TODO` comments in:

- `analyze.py`
- `src/data_profile.py`
- `src/compression.py`
- `src/llm_interpretation.py`
- `src/report_builder.py`

The template should not run end-to-end until you complete those TODOs.

## Setup

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure your real LLM provider. The exact environment variable depends on your provider and classroom setup.

Example:

```bash
export OPENAI_API_KEY="your-key-here"
```

## Target Run Command

After completing the TODOs, your project should support:

```bash
python analyze.py --input ../data/sample_sales.csv --out output
```

This command is a target, not proof that the untouched template is complete.

## Expected Outputs

Your completed project should write:

```text
output/
  profile.json
  compressed_input.json
  llm_prompt.txt
  llm_raw_response.txt
  report.json
  report.md
```

## Required Final Evidence

- The final run must call a real LLM.
- Save the prompt and raw/validated LLM response.
- Do not send the full CSV to the LLM.
- Preserve the required top-level keys in `report.json`.
- Document AI Agent Coding Tool use in `prompts.md` or `ai_usage.md`.

## Suggested AI Agent Prompts

```text
Explain the TODOs in this project before writing code.
Which file should I complete first and why?
```

```text
Help me complete build_profile().
Keep the output keys stable and explain how I should test it.
```

```text
Help me add a real LLM call.
Ask me which provider I am using before writing provider-specific code.
```

```text
Review my report.json output against the required schema.
Tell me what is missing before suggesting edits.
```
