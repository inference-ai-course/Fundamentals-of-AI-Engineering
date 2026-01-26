# Week 6 — Part 01: From scripts to pipelines (stages + artifacts)

## Overview

A pipeline is a sequence of stages.

Each stage should have:

- clear inputs
- clear outputs
- a single responsibility

This structure improves:

- debugging (you can isolate failures)
- reproducibility (you save intermediate artifacts)

---

## Suggested capstone stages

1. **Load**: read CSV
2. **Profile**: compute stats
3. **Compress**: sample rows, compute summaries
4. **LLM**: send compressed representation
5. **Report**: produce `report.json` + `report.md`

For Level 1, this can all be in one script, but you should treat these stages explicitly.

---

## Self-check

- If the LLM call fails, do you still have the profiling artifact?
- Can you re-run only the LLM stage with the saved compressed input?

---

## References

- Twelve-Factor logs/config mindset: https://12factor.net/
