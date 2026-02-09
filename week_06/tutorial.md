# Foundamental Course — Week 6 Tutorials

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 3: AI Engineering Fundamentals](../../self_learn/Chapters/3/Chapter3.md)

## Overview

This week you build the **capstone happy path** end-to-end:

- CSV profiling
- sampling/compression to fit context limits
- LLM call using your client
- stable outputs: `report.json` + `report.md`

## Navigation

- [01 — From scripts to pipelines (stages + artifacts)](01_pipeline_design.md)
- [02 — Sampling/compression strategies for tabular data](02_sampling_compression.md)
- [03 — Chunking long text + synthesizing summaries](03_chunking_synthesis.md)
- [04 — End-to-end capstone runner (one command)](04_capstone_runner.md)

## Recommended order

1. Read 01 and outline your pipeline stages.
2. Read 02/03 to handle context constraints.
3. Implement 04 to run everything with one command.

Use [practice.ipynb](practice.ipynb) for extra work.

Why this order works:

1. **Pipeline stages first**
    - If you don’t define stages and artifacts, debugging becomes “rerun everything and hope”.
    - What to verify: each stage has an input/output and writes an artifact you can inspect.

2. **Context constraints second**
    - Most capstone failures are context-budget failures (too much input, not enough output budget).
    - What to verify: you can generate a bounded `compressed_input.json` that is stable across reruns.

3. **One-command runner last**
    - A single entrypoint is the reproducibility test: can someone else run it without “magic steps”?
    - What to verify: one command produces `report.json` + `report.md` in a predictable location.
