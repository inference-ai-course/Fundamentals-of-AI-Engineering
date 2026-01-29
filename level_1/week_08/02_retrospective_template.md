# Week 8 — Part 02: Retrospective / postmortem template

## Overview

A retrospective is a structured reflection:

- what went wrong
- why it went wrong
- what you changed
- what you’d do next

In engineering culture, “blameless postmortems” emphasize learning.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on the overall roadmap and prerequisites:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 Schedule](../../level_0/Schedule.md)

Why it matters here (Week 8):

- Retrospectives turn one-off failures into reusable rules you can apply in future systems.
- Keep it evidence-based: cite artifacts/logs and name concrete fixes.

---

## Template

Create `RETROSPECTIVE.md` (example):

```md
# Capstone Retrospective

## What I built

Describe your system in 3–6 sentences:

- What problem it solves
- What the input/output is
- What the pipeline stages are
- What artifacts it produces

## What went well

Write 2–4 bullets with evidence.
Example: “Our one-command runner produced stable `report.json` outputs across reruns.”

## What went wrong (top 3)

1. <symptom + when it happened>
2. <symptom + when it happened>
3. <symptom + when it happened>

For each item, include:

- Symptom: what you observed (error message, bad output, slow run)
- When it happened (which command / which input)
- Evidence: link to logs or artifacts (a file path is enough)

## Root causes

For each “what went wrong”, write the most likely root cause.
Try to phrase it as a generalizable rule (something you can prevent next time).
Example: “We did not validate LLM JSON, so downstream parsing failed unpredictably.”

## Fixes I implemented

List what you changed in code/process.
Example: “Added schema validation + retry/repair with a hard retry limit.”

## What I would do next (Level 2 direction)

Propose 2 concrete improvements.
Example: “Create a small eval set and track recall@k so retrieval changes are measurable.”

## Key lessons

Write 3–6 short lessons that you can re-use later.
Example: “Saving intermediate artifacts turns debugging from guesswork into inspection.”
```

---

## References

- Google SRE postmortem culture: https://sre.google/sre-book/postmortem-culture/
