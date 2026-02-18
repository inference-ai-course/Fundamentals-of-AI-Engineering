# Foundations Course — Week 7 Tutorials

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Python and Environment Management](../self_learn/Chapters/2/Chapter2.md)
- [Self-learn — Chapter 5: Resource Monitoring and Containerization](../self_learn/Chapters/5/Chapter5.md)

## Overview

This week you make your capstone **usable** and **reliable**:

- better CLI design
- config and secrets management
- safer error handling
- tests (pytest or smoke tests)

## Navigation

- [01 — CLI design (argparse) + good defaults](01_cli_design.md)
- [02 — Config management + secrets (.env)](02_config_secrets.md)
- [03 — Error handling that teaches the user what to do](03_error_handling.md)
- [04 — Testing strategy: pytest vs smoke tests](04_testing_strategy.md)

## Recommended order

1. Read 01 and improve your CLI.
2. Read 02 and cleanly separate config/secrets.
3. Read 03 and make failures explainable.
4. Read 04 and add 3+ checks.

Why this order works:

1. **CLI first**
    - Your CLI is the “front door” to your project. If it’s confusing, everything else becomes harder to test.
    - What to aim for: a single command that runs the happy path (plus `--help` that clearly shows defaults).
    - Example: `python run_capstone.py --input data.csv --out_dir output --model gpt-4o-mini`.

2. **Config + secrets second**
    - You want reproducible configuration (things you can safely commit) separated from secrets (things you must not commit).
    - What to aim for: config flags and a `.env` file for keys.
    - Example: commit `config.json` defaults, but load `OPENAI_API_KEY` from environment.

3. **Explainable failures third**
    - After your project is runnable, the next biggest bottleneck is “it failed, but I don’t know why”.
    - What to aim for: errors that tell the user what to do next (missing file, missing column, invalid response, rate limit).
    - Example: when validation fails, print which field is missing and where the raw output was saved.

4. **Tests last**
    - Tests are easiest to write after interfaces stabilize (CLI args, config shape, error behavior).
    - What to aim for: at least one happy-path run plus a few “expected failure” checks.
    - Example checklist: missing input file, empty CSV, LLM timeout, invalid JSON returned.
