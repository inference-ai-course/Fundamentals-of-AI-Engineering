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

For each stage, aim to make the contract explicit.

1. **Load**
    - **Inputs**: `data/*.csv` (or a single CSV path)
    - **Outputs**: an in-memory dataframe/table OR a saved intermediate like `output/loaded.parquet`
    - **Common pitfalls**: silent dtype changes, unexpected delimiters/encodings, missing columns that only fail later.

2. **Profile**
    - **Inputs**: loaded table
    - **Outputs**: `output/profile.json` (machine-readable) and optionally `output/profile.md` (human-readable)
    - **What “profile” means**: row/column counts, missing values per column, basic numeric stats, top categories.

3. **Compress**
    - **Inputs**: table + profiling results
    - **Outputs**: `output/compressed_input.json`
    - **Goal**: fit the most decision-relevant information into a bounded context window.
    - **Common pitfalls**: sampling that drops rare-but-important cases; summaries that remove units/definitions.

4. **LLM**
    - **Inputs**: prompt template + `output/compressed_input.json`
    - **Outputs**: `output/llm_raw.txt` (or JSON) and `output/llm_validated.json`
    - **Common pitfalls**: calling the model without saving the exact prompt/context; not handling timeouts/429s.

5. **Report**
    - **Inputs**: validated LLM output + (optional) original profile
    - **Outputs**: `output/report.json` and `output/report.md`
    - **Goal**: produce a stable, demo-friendly artifact with predictable keys/sections.

A useful rule of thumb: if a stage fails, you should still have the previous stage’s artifact saved so you can debug without re-running everything.

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
