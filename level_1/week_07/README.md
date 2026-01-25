# Level 1 — Week 7: Capstone Engineering & Quality

## What you should be able to do by the end of this week

- Improve usability: CLI flags, clear defaults, good `--help`.
- Improve reliability: better error messages, safer file handling, stable outputs.
- Add tests (or an equivalent smoke-test + manual checklist).

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) CLI design

**Mental model**:

- Your CLI is an interface like an API.
- A good CLI makes the correct usage easy and incorrect usage obvious.

**Practical checklist**:

- descriptive `--help`
- sensible defaults
- explicit inputs/outputs

Citations:

- Python `argparse`: https://docs.python.org/3/library/argparse.html
- Click (CLI library): https://click.palletsprojects.com/

### 2) Config management and secrets

**Mental model**:

- Keep configuration out of code.
- Never hardcode or commit API keys.

Citations:

- Twelve-Factor App — config: https://12factor.net/config
- python-dotenv: https://github.com/theskumar/python-dotenv

### 3) Error handling that teaches the user what to do

**Mental model**:

- “Explainable failures” reduce support burden and speed up debugging.
- Good error messages contain:
  - what went wrong
  - where it happened
  - what the user should try next

Citations:

- Python errors and exceptions: https://docs.python.org/3/tutorial/errors.html

### 4) Testing options (pytest vs smoke tests)

**Mental model**:

- Tests are just executable checks that protect you from regressions.
- For Level 1, you can choose:
  - `pytest` unit tests (preferred)
  - or `smoke_test.py` + a manual checklist (acceptable)

Citations:

- pytest documentation: https://docs.pytest.org/

## Workshop / Implementation Plan

- Add/upgrade:
  - CLI flags and README usage examples
  - `.env` loading for secrets
  - tests or smoke tests for 3+ cases
  - better error messages
- Stabilize output formatting (JSON field names, deterministic ordering if needed)

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: CLI and config flow (args/env -> config -> pipeline)


### Figure B: Test strategy overview (happy path + edge + failure)


## Self-check questions

- Can a teammate run your project with only the README?
- Do you have at least 3 test cases and can you execute them easily?
- When it fails, does your error message tell you what to do next?
