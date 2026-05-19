# Week 3: Data Processing + Reproducible Outputs

Week 3 is the first data-focused practice week. The goal is not to become a Python expert; the goal is to inspect CSV data reproducibly before it is used by models, scripts, or LLM workflows.

Python environment setup is taught in [Week 2](../week_02/06_python_environment_setup.md). Week 3 starts with a short preflight check, then focuses on building a CSV profiling script.

## What You Should Be Able to Do

By the end of this week, you should be able to:

- Activate the Python environment prepared in Week 2.
- Verify that the notebook kernel uses the intended Python environment.
- Load a CSV file with pandas.
- Generate reproducible `profile.json` and `profile.md` outputs.
- Explain at least 3 data quality findings in plain language.

## Python Minimum Checklist

You do not need full Python fluency before starting Week 3. You should be able to recognize these basics and ask AI to explain them while you work:

- Variables: store file paths, counts, and strings.
- Functions: read `def load_csv(...):` as a reusable step with inputs and outputs.
- Lists and dictionaries: read structures like `["name", "age"]` and `{"rows": 100}`.
- File paths: understand relative paths such as `data/sample.csv` and `output/profile.json`.
- Command-line arguments: recognize flags such as `--input data.csv --output_dir output`.
- Error messages: copy the full traceback or terminal output when asking for help.
- Imports: understand that `import pandas as pd` loads a library used by the script.

The notebooks introduce the required background inline. External documentation is listed only as optional reference material.

## Week 3 Preflight

Before starting the data profiling script, run:

```bash
python --version
which python
python -c "import pandas as pd; print(pd.__version__)"
```

On Windows, replace `which python` with `where python`.

If pandas is missing, return to [Week 2 Python Environment Setup](../week_02/06_python_environment_setup.md), activate the environment, and install the required packages before continuing.

## Tutorials

Required Week 3 path:

- [01 Environment Preflight](01_environment_setup.md)
- [02 Data Profiling Script](02_data_profiling_script.md)

For local inference and LLM reliability topics, see [Week 4](../week_04/README.md).

## Workshop Plan

1. Activate the Week 2 environment.
2. Verify pandas imports successfully.
3. Confirm the notebook kernel uses the same environment.
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
- Required profile fields: row and column counts, column names, dtypes, missing values, duplicate rows, numeric summaries, and categorical top values.
- A short report with at least 3 findings.
- A README with setup and run commands.
- Manual test checklist or automated tests.

## Common Pitfalls

- Forgetting to activate the Week 2 environment.
- Running notebooks with the wrong kernel.
- Sharing screenshots of errors without the full text output.
- Writing output files to unclear locations.
- Treating data as ready before checking missing values, types, and duplicates.

## Self-check Questions

- Can someone follow your README and reproduce your output files?
- Can you prove you are using the intended Python environment?
- Can you point to the exact CSV input that produced your report?
- What is the most important data quality issue you found?
