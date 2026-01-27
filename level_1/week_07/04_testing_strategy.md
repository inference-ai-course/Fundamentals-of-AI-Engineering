# Week 7 — Part 04: Testing strategy (pytest vs smoke tests)

## Overview

Tests are executable checks that protect you from regressions.

---

## Underlying theory: tests reduce uncertainty when you change things

Every change introduces risk. Tests are a way to keep the system stable while you iterate.

Two common layers:

- **unit tests**: small, fast checks (parsing, validation, file handling)
- **smoke tests**: end-to-end checks (the pipeline runs and produces artifacts)

For LLM projects, you often cannot assert exact text outputs. Instead you assert:

- output is valid JSON
- required keys exist
- file artifacts are created
- failures are handled gracefully (timeouts, missing inputs)

For Level 1 you can choose:

- `pytest` unit tests (preferred)
- or a `smoke_test.py` plus a manual checklist (acceptable)

---

## Minimal test plan (3+ cases)

You should have at least:

- **happy path**: normal input works
- **edge case**: missing values or tiny CSV
- **failure case**: missing file / invalid schema

Practical tip: smoke tests can be “one command” checks that run in CI later. The key is making them deterministic enough to be repeatable.

---

## References

- pytest docs: https://docs.pytest.org/
