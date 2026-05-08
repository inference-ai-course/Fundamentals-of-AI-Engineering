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

## Python Minimum Checklist

You do not need to become fluent in Python before starting Week 3. You should be able to recognize and ask AI to explain these basics while working through the exercises:

- Variables: store simple values such as file paths, counts, and strings.
- Functions: understand `def load_csv(...):` as a reusable step with inputs and outputs.
- Lists and dictionaries: read simple structures like `["name", "age"]` and `{"rows": 100}`.
- File paths: understand relative paths such as `data/sample.csv` and output paths such as `output/profile.json`.
- Command-line arguments: recognize flags such as `--input data.csv --output_dir output`.
- Error messages: copy the full traceback or terminal output when asking for help.
- Imports: understand that `import pandas as pd` loads a library used by the script.

If any item is unfamiliar, use the linked self-learn chapter as a reference only when needed; it is not a separate prerequisite.

## Tutorials

Main Week 3 learning path:

- [01_environment_setup.md](01_environment_setup.md)
- [02_data_profiling_script.md](02_data_profiling_script.md)

Optional/advanced local inference reference:

- [01_local_inference_setup.md](01_local_inference_setup.md)
- [02_ollama_http_client.md](02_ollama_http_client.md)
- [03_benchmarking_script.md](03_benchmarking_script.md)

Other LLM reliability files that remain in this folder are legacy references. For the required LLM workflow, use the Week 4 materials.

## Workshop Plan

1. Create a fresh environment with venv or conda.
2. Install pandas and any required dependencies.
3. Run a small CSV loading example.
4. Build or adapt a data profiling script:
   - input: `--input path/to/data.csv`
   - output directory: `output/`
   - output files: `profile.json` and `profile.md`
5. Run the script on a provided CSV or your own small dataset.
6. Write a short data quality note.

## Deliverables

- A runnable data profiling script.
- `output/profile.json`.
- `output/profile.md`.
- A short report with at least 3 findings.
- A README with setup and run commands.
- Manual test checklist or automated tests.

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
