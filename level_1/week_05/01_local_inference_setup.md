# Week 5 — Part 01: Local inference concepts + setup checklist

## Overview

**Inference** = using a trained model to generate outputs.

**Local inference** = you run the model on your own machine.

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

For Level 1, focus on the practical effect:

- If it doesn’t fit, you can’t run it.

---

## References

- Ollama: https://ollama.com/
- Ollama GitHub: https://github.com/ollama/ollama
- Hugging Face model cards: https://huggingface.co/docs/hub/model-cards
