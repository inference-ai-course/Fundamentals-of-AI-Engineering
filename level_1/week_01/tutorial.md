# Level 1 — Week 1 Tutorials

## Overview

These tutorials expand Week 1 into a step-by-step, chapter-style walkthrough.

## Navigation

- [01 — Environment setup + dependency management](01_environment_setup.md)
- [02 — Data profiling script (CSV -> JSON/Markdown outputs)](02_data_profiling_script.md)

## Recommended order

1. Read 01, set up your environment.
2. Read 02, implement and run the profiling script.
3. Use [practice.ipynb](practice.ipynb) for extra hands-on practice.

Why this order works:

1. **Environment first**
    - If your environment is unstable, every later step becomes “mystery debugging”.
    - What to verify: you can run `python --version`, activate your venv, and run a small script twice with the same output.

2. **Profiling script second**
    - This is your first “reproducible artifact” workflow: input file → deterministic outputs.
    - What to verify: running the script creates `output/` files in the same place, with predictable names.
    - Example: your script should fail clearly on missing input and succeed on a small sample CSV.

3. **Practice notebook last**
    - Use the notebook to explore variations (different CSVs, edge cases) after the main script path is working.
