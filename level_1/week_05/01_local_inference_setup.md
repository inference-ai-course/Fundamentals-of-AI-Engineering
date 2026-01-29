# Week 5 — Part 01: Local inference concepts + setup checklist

## Overview

**Inference** = using a trained model to generate outputs.

**Local inference** = you run the model on your own machine.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on local inference and model/platform fundamentals:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 4: Hugging Face Platform and Local Inference](../../level_0/Chapters/4/Chapter4.md)

Why it matters here (Week 5):

- When you run locally, hardware constraints (RAM/VRAM/CPU/GPU) become part of your system design.
- The setup checklist below is the fastest way to prove the local runtime works before you debug client code.

---

## Setup checklist (practical)

1. Install Ollama
2. Start the Ollama service
3. Pull a model
4. Run a test prompt

What to do and what “success” looks like:

1. **Install Ollama**
    - Goal: have the `ollama` CLI available.
    - What to verify: running `ollama --version` prints a version.

2. **Start the Ollama service**
    - Goal: have a local server process ready to accept requests.
    - What to verify: `ollama serve` starts without immediately exiting.
    - Common failure: port conflicts or permission issues; if the service won’t start, fix that before touching your client code.

3. **Pull a model**
    - Goal: download at least one model so you can run an end-to-end request.
    - What to verify: `ollama list` shows the model.
    - Practical note: start small (a smaller model/quantization) to avoid memory failures.

4. **Run a test prompt**
    - Goal: confirm that request → generation works locally.
    - What to verify: `ollama run <model_name>` produces output quickly and doesn’t crash.
    - If this step is slow, it may still be “working”; your hardware and model choice dominate latency.

---

## What “model size / context window / quantization” mean

- **Size (e.g. 7B, 13B)**: larger often means better quality but slower and more memory.
- **Context window**: how much text you can include per request.
- **Quantization**: smaller memory footprint (quality may change slightly).

More concrete intuition:

- model “size” (e.g. 7B) is roughly the number of parameters
- more parameters typically means more compute per generated token
- quantization stores weights with fewer bits, reducing memory and often increasing speed on constrained hardware

Practical rule of thumb: local inference is often bottlenecked by memory bandwidth and/or VRAM capacity, not just CPU speed.

For Level 1, focus on the practical effect:

- If it doesn’t fit, you can’t run it.

---

## References

- Ollama: https://ollama.com/
- Ollama GitHub: https://github.com/ollama/ollama
- Hugging Face model cards: https://huggingface.co/docs/hub/model-cards
