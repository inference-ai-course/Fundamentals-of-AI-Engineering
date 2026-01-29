# Level 1 — Week 5 Tutorials

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 4: Hugging Face Platform and Local Inference](../../level_0/Chapters/4/Chapter4.md)

## Overview

This week you run LLMs locally (Ollama) and compare models with a consistent benchmark.

You will practice:

- installing + running a local model
- sending prompts via HTTP
- measuring latency
- saving outputs for comparison

## Navigation

- [01 — Local inference: concepts + setup checklist](01_local_inference_setup.md)
- [02 — Calling Ollama via HTTP (minimal client)](02_ollama_http_client.md)
- [03 — Benchmarking script: latency + quality artifacts](03_benchmarking_script.md)

## Recommended order

1. Read 01 and confirm Ollama runs.
2. Read 02 and run a single prompt end-to-end.
3. Read 03 and build a benchmark harness.

Use [practice.ipynb](practice.ipynb) for extra work.

Why this order works:

1. **Confirm the local runtime first**
    - Until the local server runs, any “client bug” is actually an environment/runtime issue.
    - What to verify: `ollama serve` works and you can run one model once.

2. **Single prompt end-to-end second**
    - Prove the HTTP contract: request → response → basic validation.
    - What to verify: you can send a prompt, get a response, and handle timeouts/errors cleanly.

3. **Benchmark harness last**
    - Once one request works, scale to many requests and measure latency distribution.
    - What to verify: your benchmark saves outputs and latency metrics so you can compare models later.
