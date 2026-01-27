# Level 2 — Week 10 Tutorials

## Overview

Week 10 is the delivery sprint:

- demo story
- evaluation evidence
- architecture defense
- limitations + roadmap

Underlying theory you should internalize this week:

- a demo is an argument: claim → evidence → reasoning
- strong defenses use falsifiable claims (metrics/artifacts), not “it feels better”
- most questions reduce to tradeoffs (precision vs recall, latency vs reliability, strictness vs UX)

## Navigation

- [01 — Demo script + failure case story](01_demo_script.md)
- [02 — Evidence pack (metrics + failures + before/after)](02_evidence_pack.md)
- [03 — Defense checklist (tradeoffs + limitations)](03_defense_checklist.md)

## Recommended order

1. Read 01 and make the demo repeatable.
2. Read 02 and regenerate evidence.
3. Read 03 and prepare the defense narrative.

Why this order works:

1. **Repeatable demo first**
    - If the demo is flaky, you can’t trust any claims you make about quality.
    - What to verify: you can run the demo twice and get the same high-level behavior and artifacts.

2. **Evidence second**
    - Claims must be backed by artifacts (metrics + failure cases) that someone else can rerun.
    - What to verify: your eval script produces a before/after summary and you can point to raw outputs.

3. **Defense narrative third**
    - Once you have evidence, you can answer questions about tradeoffs and limitations credibly.
    - What to verify: you can explain precision/recall, latency/reliability, and strictness/UX tradeoffs using your project’s data.

## What “done” looks like

- You can run the demo start-to-finish without surprises.
- You have at least one intentional failure case and you can explain it.
- Your evidence pack is reproducible (scripts + artifacts).
- You can explain tradeoffs and limitations without hand-waving.

## References

- SRE SLOs: https://sre.google/sre-book/service-level-objectives/
- Twelve-Factor: https://12factor.net/
