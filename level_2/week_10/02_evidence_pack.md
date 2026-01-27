# Week 10 — Part 02: Evidence pack (metrics + failures + before/after)

## Overview

Your evidence pack should include:

- reproducible eval script output
- top failures list with root causes
- before/after improvement from at least one controlled change

---

## Underlying theory: evidence is about reproducibility and attribution

### Reproducibility

An evidence pack is credible when another person can regenerate it.

This is why you save:

- config
- metrics
- failures

If you can’t rerun it, the evidence is anecdote.

### Attribution (why “one variable at a time” matters)

If you claim improvement, you want a causal story:

- change: what did you modify?
- mechanism: why should it help?
- measurement: which metric moved and which failures disappeared?

This is the controlled iteration discipline from Week 5.

Practical warning:

- with small eval sets, don’t overclaim tiny improvements

## What to regenerate before demo

- retrieval metrics
- rag eval metrics
- failure list

Save as artifacts so reviewers can inspect.

---

## Evidence pack checklist (what to include)

- `runs/<run_id>/config.json`
- `runs/<run_id>/metrics.json`
- `runs/<run_id>/failures.json`
- `runs/<run_id>/samples.md` (a few example Q/A with citations)

Also include:

- a short README describing how to reproduce the run
- one “before vs after” comparison

Reviewers should be able to inspect without reading your entire codebase.

---

## Self-check

- Can another person rerun your eval script and see the same results?

---

## References

- JSON Lines: https://jsonlines.org/
