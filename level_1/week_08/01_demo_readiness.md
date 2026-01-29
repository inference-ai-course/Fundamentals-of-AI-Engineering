# Week 8 — Part 01: Demo readiness checklist + README polishing

## Overview

A demo is successful when another person can reproduce it.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on the overall roadmap and prerequisites:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 Schedule](../../level_0/Schedule.md)

Why it matters here (Week 8):

- A demo is a reproducibility test: “fresh clone + README steps” should work without magic steps.
- A failure-case story with saved artifacts/logs increases credibility and shows system understanding.

---

## Demo readiness checklist

- Setup steps start from scratch:
  - create env
  - install deps
  - configure secrets

- Run steps:
  - one command
  - expected outputs listed

- Outputs:
  - stable file paths
  - stable schema fields

- Failure case:
  - show what happens when an input is invalid
  - show how logs help

If you have time, add one “performance realism” note:

- expected runtime on your machine
- known slow step (e.g., first model call)

---

## Self-check

- Can a teammate run your demo without asking you questions?
- Can you demo without editing code live?

---

## References

- GitHub on READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
