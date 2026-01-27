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

## Underlying theory: pipelines make dataflow explicit

You can view a pipeline as a composition of functions:

$$
Y = (f_k \circ f_{k-1} \circ \cdots \circ f_1)(X)
$$

Each stage $f_i$ should have a small, testable contract:

- **inputs**: what files/values it needs
- **outputs**: what artifacts it produces
- **invariants**: what must be true after it runs (schema, counts, non-empty, etc.)

Practical implication:

- a bug is easier to locate because you can bisect stages
- you can cache/reuse artifacts (don’t redo expensive work unnecessarily)
- you can re-run only the stage you changed (faster iteration)

---

## Suggested capstone stages

1. **Load**: read CSV
2. **Profile**: compute stats
3. **Compress**: sample rows, compute summaries
4. **LLM**: send compressed representation
5. **Report**: produce `report.json` + `report.md`

For Level 1, this can all be in one script, but you should treat these stages explicitly.

Artifact mindset (recommended):

- every stage writes an output file in a predictable location
- later stages read those files instead of re-computing silently

This makes your pipeline debuggable even when the LLM call fails or is rate-limited.

---

## Self-check

- If the LLM call fails, do you still have the profiling artifact?
- Can you re-run only the LLM stage with the saved compressed input?

---

## References

- Twelve-Factor logs/config mindset: https://12factor.net/
