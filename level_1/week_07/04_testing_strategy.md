# Week 7 — Part 04: Testing strategy (pytest vs smoke tests)

## Overview

Tests are executable checks that protect you from regressions.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on project structure, environments, and reproducibility:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 2: Python and Environment Management](../../level_0/Chapters/2/Chapter2.md)

Why it matters here (Week 7):

- Interfaces are now stable enough (CLI/config/error behavior) that tests can protect you from regressions.
- For LLM projects, assert contracts (valid JSON/required keys/artifacts), not exact text.

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
