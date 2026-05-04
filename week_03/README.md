# Week 3: Environment + Data Processing

Week 3 is the first technical practice week. The goal is not to become a Python expert; the goal is to learn how AI projects stay reproducible and how data is inspected before it is used by models or LLMs.

## Pre-study (Optional Refresher)

Self-learn is optional. Use these only if you want extra background:

- [Pre-study guide](../PRESTUDY.md)
- [Self-learn - Chapter 1: Tool Preparation](../self_learn/Chapters/1/Chapter1.md)
- [Self-learn - Chapter 2: Python and Environment Management](../self_learn/Chapters/2/Chapter2.md)

## What You Should Be Able to Do

By the end of this week, you should be able to:

- Create and activate a clean Python environment.
- Install dependencies and record them in `requirements.txt`.
- Load a CSV file with pandas.
- Generate reproducible `profile.json` and `profile.md` outputs.
- Explain at least 3 data quality findings in plain language.

## Tutorials

Main Week 3 learning path:

- [01_environment_setup.md](01_environment_setup.md)
- [02_data_profiling_script.md](02_data_profiling_script.md)

Local inference materials are no longer required for Week 3. They live under Week 4 optional/advanced materials.

Optional/advanced local inference reference:

- [../week_04/optional_local_inference/01_local_inference_setup.md](../week_04/optional_local_inference/01_local_inference_setup.md)
- [../week_04/optional_local_inference/02_ollama_http_client.md](../week_04/optional_local_inference/02_ollama_http_client.md)
- [../week_04/optional_local_inference/03_benchmarking_script.md](../week_04/optional_local_inference/03_benchmarking_script.md)

## Workshop Plan

1. Create a fresh environment with venv or conda.
2. Install pandas and any required dependencies.
3. Run a small CSV loading example.
4. Build or adapt a data profiling script:
   - input: `--input path/to/data.csv`
   - output directory: `output/`
   - output files: `profile.json` and `profile.md`
5. Run the script on the provided sample CSV (`data/sample.csv`) or your own small dataset.
6. Write a short data quality report (see Report Template below).

## Deliverables

- A runnable data profiling script.
- `output/profile.json`.
- `output/profile.md`.
- A short report with at least 3 findings.
- A README with setup and run commands.
- Manual test checklist or automated tests.

## Report Template

Your `report.md` should follow this structure:

```markdown
# Data Quality Report

## Dataset

- Source: (filename or URL)
- Rows: (from profile)
- Columns: (from profile)

## Findings

### Finding 1: (title)

(What you observed, why it matters, and what action you would take.)

### Finding 2: (title)

(What you observed, why it matters, and what action you would take.)

### Finding 3: (title)

(What you observed, why it matters, and what action you would take.)

## Summary

(One paragraph: overall data quality assessment and recommended next steps.)
```

Examples of good findings:
- "Column `salary` has 2 missing values (10% of rows). These should be imputed or excluded before training."
- "Row 1 and row 11 are exact duplicates. This could inflate model accuracy if not removed."
- "Column `city` has 5 distinct values. The top value 'New York' accounts for 30% of records, suggesting geographic imbalance."

## Common Pitfalls

- Running `pip install` outside the active environment.
- Sharing screenshots of errors without the full text output.
- Writing output files to unclear locations.
- Treating data as "ready" before checking missing values, types, and duplicates.

## Self-check Questions

- Can someone follow your README and reproduce your output files?
- Can you explain the difference between system Python and a virtual environment?
- Can you point to the exact CSV input that produced your report?
- What is the most important data quality issue you found?
