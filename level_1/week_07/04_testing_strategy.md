# Week 7 — Part 04: Testing strategy (pytest vs smoke tests)

## Overview

Tests are executable checks that protect you from regressions.

For Level 1 you can choose:

- `pytest` unit tests (preferred)
- or a `smoke_test.py` plus a manual checklist (acceptable)

---

## Minimal test plan (3+ cases)

You should have at least:

- **happy path**: normal input works
- **edge case**: missing values or tiny CSV
- **failure case**: missing file / invalid schema

---

## References

- pytest docs: https://docs.pytest.org/
