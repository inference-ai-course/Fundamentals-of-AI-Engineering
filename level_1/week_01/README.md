# Level 1 — Week 1: Environment Setup & Data Processing Basics

## What you should be able to do by the end of this week

- Create a clean Python environment and install dependencies reliably.
- Run a project from a README on a fresh machine (or a fresh folder).
- Build a small “data profiling” script that reads a CSV and produces reproducible outputs.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_environment_setup.md](01_environment_setup.md)
- [02_data_profiling_script.md](02_data_profiling_script.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Python environments and dependency management

**Mental model**:

- Your OS can have many Python versions and many package versions.
- A **virtual environment** isolates packages for one project so that:
  - Project A can use `pandas==x` and Project B can use `pandas==y` without conflicts.
  - “It works on my machine” becomes less common.

**What to practice**:

- Create an environment.
- Install dependencies from `requirements.txt` or `pyproject.toml`.
- Record versions so another person can reproduce your run.

Citations:

- Python `venv` (official): https://docs.python.org/3/library/venv.html
- Python Packaging User Guide (official): https://packaging.python.org/
- pip user guide (official): https://pip.pypa.io/en/stable/user_guide/

### 2) Project structure: scripts vs modules

**Mental model**:

- A **script** is an entrypoint (e.g. `python data_profile.py --input ...`).
- A **module** is reusable code (e.g. `src/data_profile.py`) imported by scripts.
- In Level 1, it’s acceptable to start with simple scripts; you’ll modularize more later.

**Why it matters**:

- Clean structure makes debugging easier (you know where logic lives).
- A clear entrypoint makes “one-command runs” possible.

Citations:

- Python tutorial (modules): https://docs.python.org/3/tutorial/modules.html

### 3) Exceptions vs logs (debugging intuition)

**Mental model**:

- An **exception** tells you what failed and where.
- **Logs** tell you what happened leading up to the failure.

**Practical approach**:

- When debugging, do not start by guessing.
- First, capture:
  - the exact command
  - the full stack trace
  - the input that triggered the failure

Citations:

- Python errors and exceptions (official): https://docs.python.org/3/tutorial/errors.html
- Python `logging` (official): https://docs.python.org/3/library/logging.html

### 4) Pandas I/O and basic cleaning

**Mental model**:

- A dataframe is a table with:
  - rows = records
  - columns = features/attributes
- “Data cleaning” usually means making types consistent and handling missing/bad values.

**What to practice**:

- Read a CSV.
- Inspect dtypes.
- Compute missing value stats.
- Export a report (JSON/Markdown) to `output/`.

Citations:

- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas I/O (CSV): https://pandas.pydata.org/docs/user_guide/io.html

## Common pitfalls

- Running `pip install ...` outside your environment.
- Not pinning dependencies (or not recording them anywhere).
- Only sharing screenshots of errors instead of copy/paste logs.
- Writing outputs to random locations (hard to reproduce).

## Workshop / Implementation Plan

- Create environment and install dependencies.
- Implement `data_profile.py`:
  - input: `--input path/to.csv`
  - output: write files to `output/`
  - include clear errors for missing file / empty file / missing columns

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: Environment setup flow (Python -> venv -> install -> run)


### Figure B: Data profiling pipeline (read -> validate -> stats -> export)


## Self-check questions

- Can you explain the difference between a virtual environment and the system Python?
- Can you re-run your script and get the same output files from the same input?
- If someone else runs your README steps, do they succeed without extra “secret” steps?
