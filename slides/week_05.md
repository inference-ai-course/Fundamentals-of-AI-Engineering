---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 5 — Local Inference (Ollama) & Model Comparison"
style: |
  section { font-size: 24px; }
  pre { font-size: 18px; }
  code { font-size: 18px; }
  h1 { color: #0f3460; border-bottom: 3px solid #00d2ff; padding-bottom: 8px; }
  h2 { color: #16213e; }
  table { font-size: 20px; }
  img { max-height: 420px; display: block; margin: 0 auto; }
  section.lead { text-align: center; background: linear-gradient(135deg, #0f3460, #16213e); color: #e8e8e8; }
  section.lead h1 { color: #00d2ff; border: none; font-size: 48px; }
  section.lead h2 { color: #e8e8e8; font-weight: 400; }
---

<!-- _class: lead -->

# Week 5

## Local Inference (Ollama) & Model Comparison

---

# Learning Objectives

By the end of this week, you should be able to:

- Run at least one model locally using Ollama
- Compare 2–3 models on the same task using a consistent benchmark script
- Explain the practical constraints: speed, memory (VRAM/RAM), context limits, and output quality

---

# What is Inference?

![bg right:50%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtUcmFpbmluZyBQaGFzZV0gLS0-IEJbRmVlZCBkYXRhIHRvIG1vZGVsXQogIEIgLS0-IENbTW9kZWwgbGVhcm5zIHBhdHRlcm5zXQogIEMgLS0-IERbU2F2ZSB0cmFpbmVkIG1vZGVsXQogIEQgLS0-IEVbSW5mZXJlbmNlIFBoYXNlXQogIEUgLS0-IEZbTmV3IGlucHV0IGRhdGFdCiAgRiAtLT4gR1tNb2RlbCBwcmVkaWN0cyBvdXRwdXRd)

- **Training**: learn from data (expensive, done once)
- **Inference**: make predictions (fast, done many times)
- GPT-4, Ollama = **inference**

---

# Cloud vs Local Inference

### Cloud (Hosted API)

![Cloud](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtZb3VyIGFwcF0gLS0-IEJbSW50ZXJuZXRdCiAgQiAtLT4gQ1tDbG91ZCBwcm92aWRlcl0KICBDIC0tPiBEW0xhcmdlIEdQVSBjbHVzdGVyXQogIEQgLS0-IEVbUmVzcG9uc2VdCiAgRSAtLT4gQgogIEIgLS0-IEE=)

---

# Local Inference with Ollama

![bg right:50%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtZb3VyIGFwcF0gLS0-IEJbbG9jYWxob3N0OjExNDM0XQogIEIgLS0-IENbT2xsYW1hIHNlcnZlcl0KICBDIC0tPiBEW1lvdXIgQ1BVL0dQVSArIFJBTV0KICBEIC0tPiBFW1Jlc3BvbnNlXQogIEUgLS0-IEE=)

Your app talks to Ollama on `localhost:11434` — same HTTP pattern as cloud APIs, but everything runs on your hardware.

---

# Cloud vs Local: Comparison

| | Cloud API | Local Inference |
|---|----------|-----------------|
| **Privacy** | Data leaves your machine | Data stays local |
| **Cost** | Pay per token | Free (your hardware) |
| **Model size** | Large (GPT-4, Claude) | Smaller (1B–13B) |
| **Setup** | API key only | Install Ollama + pull model |
| **Offline** | No | Yes |

---

# Setup Checklist

| Step | Command | Success looks like |
|------|---------|-------------------|
| 1. Install Ollama | `curl -fsSL https://ollama.com/install.sh \| sh` | `ollama --version` prints version |
| 2. Start service | `ollama serve` | Running on `http://localhost:11434` |
| 3. Pull a model | `ollama pull llama3.2:1b` | `ollama list` shows model |
| 4. Test prompt | `ollama run llama3.2:1b "Say hello"` | Produces output |

**Tip**: Start with a small model (1B–3B) to avoid memory issues.

---

# Model Size, Context, and Quantization

- **Size (7B, 13B)**: more parameters = better quality, slower, more memory
- **Context window**: how much text fits per request
- **Quantization**: fewer bits = less memory, slightly lower quality

### Memory Requirements (rough)

| Model Size | 4-bit | 8-bit | Full |
|------------|-------|-------|------|
| 1B params  | ~1 GB | ~2 GB | ~4 GB |
| 3B params  | ~2 GB | ~4 GB | ~12 GB |
| 7B params  | ~4 GB | ~8 GB | ~28 GB |
| 13B params | ~8 GB | ~16 GB | ~52 GB |

**Rule**: If it doesn't fit in memory, you can't run it.

---

# Error Handling for Local Inference

| Error | Cause | Fix |
|-------|-------|-----|
| `ConnectionError` | Ollama not running | Run `ollama serve` |
| `404` | Model not pulled | `ollama pull <model>` |
| `Timeout` | Model too large / slow HW | Use smaller model or increase timeout |
| OOM crash | Model exceeds RAM/VRAM | Use smaller model or quantization |

**First request is always slow** (model loading) — subsequent requests are faster.

---

# Benchmarking: Consistent Comparison

![bg right:50%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgTVtNb2RlbHMgbGlzdF0gLS0-IFJbUnVuIHByb21wdCBzZXRdCiAgUFtQcm9tcHQgc2V0XSAtLT4gUgogIFIgLS0-IExbUmVjb3JkIGxhdGVuY3ldCiAgUiAtLT4gUVtTYXZlIG91dHB1dHNdCiAgTCAtLT4gU1tzdW1tYXJ5Lmpzb25dCiAgUSAtLT4gUw==)

**Benchmark hygiene**:
- Same prompt set for all models
- Warmup run per model
- Save all outputs to disk

---

# Analyzing Results

### Speed comparison

| Model | Mean (s) | P95 (s) | Max (s) |
|-------|----------|---------|---------|
| llama3.2:1b | 0.8 | 1.2 | 1.5 |
| llama3.1:8b | 3.2 | 4.5 | 5.1 |

### Quality heuristics

| Task type | What to check |
|-----------|--------------|
| **JSON prompts** | Valid JSON? Required keys present? |
| **Extraction** | Correct values? Hallucinated placeholders? |
| **Summaries** | Within length limit? Key facts mentioned? |

**Speed vs Quality tradeoff**: smaller = faster but lower quality.

---

# When to Choose What

| Scenario | Recommendation |
|----------|---------------|
| Latency critical, simple task | Small local model (1B–3B) |
| Quality critical, complex reasoning | Large model or hosted API |
| Privacy / offline required | Local inference |
| High throughput batch processing | Small local model |
| Rapid prototyping | Hosted API (easiest setup) |

---

# Workshop / Deliverables

- Install Ollama and run one model successfully
- Implement `benchmark_local_llm.py`:
  - Define a small prompt set (5–20 items)
  - Run each prompt on each model
  - Record latency and store outputs
- Write a short conclusion:
  - Best model for quality
  - Best model for speed
  - "Best-fit scenarios" (when you would choose each)

---

# Self-Check Questions

- Can you run the same benchmark twice and get comparable latency distributions?
- Can you justify why one model is "best" for a specific use case?
- What is the biggest limiting factor on your machine (RAM, VRAM, CPU/GPU)?

---

# References

- Ollama: https://ollama.com/
- Ollama API docs: https://github.com/ollama/ollama/blob/main/docs/api.md
- Scaling AI with Ollama: https://inference.net/content/ollama
- LLM Inference Battle: https://dev.to/worldlinetech/the-ultimate-llm-inference-battle-vllm-vs-ollama-vs-zml-m97
