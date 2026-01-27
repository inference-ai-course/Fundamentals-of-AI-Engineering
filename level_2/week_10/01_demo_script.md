# Week 10 — Part 01: Demo story + failure case

## Overview

A good demo shows:

- problem
- approach
- live run
- failure case
- evidence
- roadmap

---

## Underlying theory: a demo is an argument (claim → evidence → reasoning)

Good technical demos are not just “look, it runs”. They are a structured argument:

- claim: what your system can do (and cannot do)
- evidence: artifacts and live runs that support the claim
- reasoning: why the evidence supports the claim (mechanism + metrics)

For RAG systems, the most important claims are usually:

- grounded answers when evidence exists
- safe behavior (clarify/refuse) when evidence is missing

---

## Why you must include a failure case

Every real RAG system fails.

Showing a controlled failure case demonstrates:

- you understand failure modes
- you built deterministic guardrails (not “prompt hope”)
- you can debug via `/search` and traces

This builds credibility because it shows engineering control.

## Standard demo timing (example)

- 60s: problem framing + constraints
- 90s: architecture + data flow
- 2m: in-KB answer with citations
- 1m: out-of-KB failure case (refusal/clarification)
- 1m: evidence (metrics + top failures)
- 30s: roadmap

---

## Demo script (what to literally say/do)

- State the problem and constraints in one sentence.
- Show the system diagram and name each component.
- Run an in-KB question:
  - show the answer
  - show citations
  - (optional) show `/search` output to prove evidence
- Run an out-of-KB question:
  - show refusal/clarification
  - explain the deterministic rule
- Show evidence pack:
  - metrics file
  - top failures with labels
- Close with roadmap (two concrete iterations).

Practical rule:

- if you show “before vs after”, name the single variable you changed and the metric that moved

---

## Self-check

- Can you demo without editing code live?
- Do you have a clear failure case story?

---

## References

- FastAPI docs (demo via /docs): https://fastapi.tiangolo.com/
