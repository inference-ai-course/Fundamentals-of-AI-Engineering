# Week 5 — Part 01: Local inference concepts + setup checklist

## Overview

**Inference** = using a trained model to generate outputs.

**Local inference** = you run the model on your own machine.

---

## Underlying theory: moving the boundary changes your constraints

When you use a hosted API, the provider owns the compute and you mostly worry about:

- request formatting
- rate limits
- latency and cost

When you run locally, you become the provider. That means **hardware is now part of your system design**.

You can think of local inference performance as a function:

$$
\text{latency} = f(\text{model size},\ \text{context length},\ \text{hardware},\ \text{quantization})
$$

Practical implication:

- if a model does not fit in RAM/VRAM, it won’t run (or will thrash)
- even if it fits, throughput/latency can vary dramatically across machines

This is useful for:

- privacy (data stays local)
- cost control (no per-request billing)
- offline capability

Trade-offs:

- quality may be lower than top hosted models
- performance depends on your CPU/GPU/RAM/VRAM

---

## Setup checklist (practical)

1. Install Ollama
2. Start the Ollama service
3. Pull a model
4. Run a test prompt

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
