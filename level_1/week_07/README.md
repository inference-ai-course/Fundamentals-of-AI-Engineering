# Level 1 — Week 7: Capstone Engineering & Quality

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 2: Python and Environment Management](../../level_0/Chapters/2/Chapter2.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

## What you should be able to do by the end of this week

- Improve usability: CLI flags, clear defaults, good `--help`.
- Improve reliability: better error messages, safer file handling, stable outputs.
- Add tests (or an equivalent smoke-test + manual checklist).

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_cli_design.md](01_cli_design.md)
- [02_config_secrets.md](02_config_secrets.md)
- [03_error_handling.md](03_error_handling.md)
- [04_testing_strategy.md](04_testing_strategy.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (Level 0 refresher)

Level 1 assumes you already learned the fundamentals in Level 0. If you need a refresher for this week:

- Modules, exception handling patterns, and file I/O habits:
  - ../../level_0/Chapters/2/02_modules_exceptions.md
- Environments, reproducibility, and operational basics:
  - ../../level_0/Chapters/2/Chapter2.md
  - ../../level_0/Chapters/5/Chapter5.md

## Workshop / Implementation Plan

- Add/upgrade:
  - CLI flags and README usage examples
  - `.env` loading for secrets
  - tests or smoke tests for 3+ cases
  - better error messages
- Stabilize output formatting (JSON field names, deterministic ordering if needed)

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: CLI and config flow (args/env -> config -> pipeline)

```mermaid
flowchart LR
  A[CLI args] --> C[Config object]
  B[.env / env vars] --> C
  C --> D[Pipeline runner]
  D --> E[Artifacts: output/]
  D --> F[Logs]
 
  F --> G[Debug: request_id/run_id]
```

### Figure B: Test strategy overview (happy path + edge + failure)

```mermaid
flowchart TD
  T[Tests] --> U[Unit tests]
  T --> S[Smoke test]
 
  U --> U1[Parsing/validation]
  U --> U2[File handling]
  U --> U3[Cache key / utils]
 
  S --> S1[Happy path]
  S --> S2[Edge case]
  S --> S3[Failure case]
```

## Self-check questions

- Can a teammate run your project with only the README?
- Do you have at least 3 test cases and can you execute them easily?
- When it fails, does your error message tell you what to do next?
