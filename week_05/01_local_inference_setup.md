# Week 5 — Part 01: Local inference concepts + setup checklist

## Overview

**Inference** = using a trained model to generate outputs.

**Local inference** = you run the model on your own machine.

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on local inference and model/platform fundamentals:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 4: Hugging Face Platform and Local Inference](../self_learn/Chapters/4/Chapter4.md)

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
    
    **Installation commands:**
    
    ```bash
    # macOS/Linux
    curl -fsSL https://ollama.com/install.sh | sh
    
    # Or download from https://ollama.com/download
    ```
    
    **Verify:**
    ```bash
    ollama --version
    # Expected: ollama version 0.x.x
    ```

2. **Start the Ollama service**
    - Goal: have a local server process ready to accept requests.
    - What to verify: `ollama serve` starts without immediately exiting.
    - Common failure: port conflicts or permission issues; if the service won’t start, fix that before touching your client code.
    
    **Start the service:**
    ```bash
    ollama serve
    # Should show: Ollama is running on http://localhost:11434
    ```
    
    **In a new terminal, verify it's running:**
    ```bash
    curl http://localhost:11434/api/tags
    # Expected: {"models": [...]}
    ```

3. **Pull a model**
    - Goal: download at least one model so you can run an end-to-end request.
    - What to verify: `ollama list` shows the model.
    - Practical note: start small (a smaller model/quantization) to avoid memory failures.
    
    **Pull a small model first:**
    ```bash
    ollama pull llama3.2:1b
    # Or for better quality but larger:
    ollama pull llama3.1:8b
    ```
    
    **Verify:**
    ```bash
    ollama list
    # Should show your downloaded model
    ```

4. **Run a test prompt**
    - Goal: confirm that request → generation works locally.
    - What to verify: `ollama run <model_name>` produces output quickly and doesn’t crash.
    - If this step is slow, it may still be “working”; your hardware and model choice dominate latency.
    
    **Test:**
    ```bash
    ollama run llama3.2:1b "Say hello in one sentence"
    # Expected: A short greeting response
    ```

---

## Troubleshooting

### Issue 1: "ollama: command not found"

**Symptom**: After installation, `ollama` command not found.

**Diagnosis**:
```bash
which ollama
# If empty, Ollama not in PATH
```

**Fix**:
- Restart terminal (installation may have updated PATH)
- Or manually add Ollama to PATH
- Verify installation completed successfully

---

### Issue 2: Port 11434 already in use

**Symptom**: `ollama serve` fails with "address already in use"

**Diagnosis**:
```bash
lsof -i :11434
# Shows what's using the port
```

**Fix**:
- If another Ollama instance is running, use that one
- Or kill the process: `kill <PID>`
- Or change Ollama port (check Ollama docs)

---

### Issue 3: Model download fails or is very slow

**Symptom**: `ollama pull` hangs or fails

**Common causes**:
- Slow/unstable internet
- Insufficient disk space
- Model too large for connection

**Fix**:
- Check disk space: `df -h`
- Try smaller model first
- Resume: re-run `ollama pull` (it resumes)

---

### Issue 4: Out of memory during inference

**Symptom**: Model loads but crashes during generation

**Diagnosis**: Model requires more RAM/VRAM than available

**Fix**:
- Use smaller model (3B instead of 7B)
- Use more aggressive quantization
- Close other applications
- Check system resources

---

## What "model size / context window / quantization" mean

- **Size (e.g. 7B, 13B)**: larger often means better quality but slower and more memory.
- **Context window**: how much text you can include per request.
- **Quantization**: smaller memory footprint (quality may change slightly).

More concrete intuition:

- model "size" (e.g. 7B) is roughly the number of parameters
- more parameters typically means more compute per generated token
- quantization stores weights with fewer bits, reducing memory and often increasing speed on constrained hardware

Practical rule of thumb: local inference is often bottlenecked by memory bandwidth and/or VRAM capacity, not just CPU speed.

### Memory requirements (rough — total runtime, including KV cache & activations)

| Model Size | 4-bit Quantized | 8-bit Quantized | Full Precision (FP32) |
|------------|----------------|----------------|----------------|
| 1B params  | ~1 GB          | ~2 GB          | ~4 GB          |
| 3B params  | ~2 GB          | ~4 GB          | ~12 GB         |
| 7B params  | ~4 GB          | ~8 GB          | ~28 GB         |
| 13B params | ~8 GB          | ~16 GB         | ~52 GB         |

**Note**: These are total runtime estimates (weights + KV cache + activations). Weight-only memory is roughly half the 8-bit column.

**Practical recommendations:**

- **8GB RAM**: Start with 1B-3B models, 4-bit quantized
- **16GB RAM**: Can run 7B models comfortably
- **32GB+ RAM**: Can run 13B+ models

For Foundations Course, focus on the practical effect:

- If it doesn't fit, you can't run it
- Smaller models = faster iteration during development

---

## Hardware selection guide

**CPU-only inference:**
- Slower but works on any machine
- Good for: development, testing, small models
- Not good for: production, real-time, large models

**GPU-accelerated inference:**
- Much faster (10-100x for large models)
- Requires: NVIDIA GPU with CUDA, or Apple Silicon with Metal
- Good for: production, benchmarking, larger models

**Recommendation for Foundations Course:**
- Start CPU-only with small models (1B-3B)
- Measure latency for your use case
- Upgrade hardware only if needed

---

## Practice notebook

For hands-on exercises and health check implementations, see:
- **[practice.ipynb](./practice.ipynb)** - Interactive Ollama setup verification

---

## References

- Ollama: https://ollama.com/
- Ollama GitHub: https://github.com/ollama/ollama
- Hugging Face model cards: https://huggingface.co/docs/hub/model-cards
