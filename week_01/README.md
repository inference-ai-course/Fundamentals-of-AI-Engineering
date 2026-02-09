# Foundamental Course — Week 1: Environment Setup & Data Processing Basics

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 1: Tool Preparation](../../self_learn/Chapters/1/Chapter1.md)
- [Self-learn — Chapter 2: Python and Environment Management](../../self_learn/Chapters/2/Chapter2.md)

## What you should be able to do by the end of this week

- Create a clean Python environment and install dependencies reliably.
- Run a project from a README on a fresh machine (or a fresh folder).
- Build a small “data profiling” script that reads a CSV and produces reproducible outputs.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_environment_setup.md](01_environment_setup.md)
- [02_data_profiling_script.md](02_data_profiling_script.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (Self-learn refresher)

Foundamental Course assumes you already learned the fundamentals in Self-learn. If you need a refresher for this week:

- Environment management (conda/venv):
  - ../../self_learn/Chapters/2/03_conda_environments.md
  - ../../self_learn/Chapters/1/04_conda_environment_management.md
- Jupyter basics:
  - ../../self_learn/Chapters/1/05_jupyter_interactive_computing.md
- Modules, exception handling, and JSON/file I/O patterns:
  - ../../self_learn/Chapters/2/02_modules_exceptions.md

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

```mermaid
flowchart TD
  A[System Python] --> B[Create venv: python -m venv .venv]
  B --> C[Activate venv]
  C --> D[Upgrade pip]
  D --> E[Install deps]
  E --> F[Freeze: requirements.txt]
  F --> G[Run script]
  G --> H[Recreate env from requirements.txt]
```

### Figure B: Data profiling pipeline (read -> validate -> stats -> export)

```mermaid
flowchart TD
  A[Input CSV] --> B[Load CSV]
  B --> C{Validate}
  C -->|missing file| E1[Fail: FileNotFoundError]
  C -->|empty file| E2[Fail: ValueError]
  C -->|ok| D[Compute stats]
  D --> F[Write output/profile.json]
  D --> G[Write output/profile.md]
  F --> H[Done]
  G --> H
```

## Self-check questions

- Can you explain the difference between a virtual environment and the system Python?
- Can you re-run your script and get the same output files from the same input?
- If someone else runs your README steps, do they succeed without extra “secret” steps?
