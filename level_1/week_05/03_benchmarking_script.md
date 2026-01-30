# Week 5 — Part 03: Benchmarking script (latency + quality artifacts)

## Overview

A benchmark must be consistent:

- same prompt set
- same measurement method
- same saved outputs

We will write `benchmark_local_llm.py` that:

- loops over prompts
- loops over models
- records latency
- saves outputs to disk

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on local inference + practical evaluation:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 4: Hugging Face Platform and Local Inference](../../level_0/Chapters/4/Chapter4.md)

Why it matters here (Week 5):

- Benchmarks only work if you control variables (same prompt set, same settings, same measurement method).
- Treat latency as a distribution (average and tail) and keep artifacts so you can compare quality later.

---

## Benchmark harness (example)

```python
import json
import time
from pathlib import Path

import requests


def call_ollama(host: str, model: str, prompt: str) -> dict:
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    t0 = time.time()
    resp = requests.post(url, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    return {
        "model": model,
        "prompt": prompt,
        "response": data.get("response", ""),
        "latency_s": time.time() - t0,
    }


def main() -> None:
    host = "http://localhost:11434"
    models = ["llama3.1", "qwen2.5"]
    prompts = [
        "Summarize: Large language models are useful but require careful evaluation.",
        "Extract JSON with keys {name, email} from: 'Name: Sam, Email: sam@example.com'",
        "Write 3 bullet points about caching.",
    ]

    out_dir = Path("benchmark_outputs")
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for model in models:
        for i, prompt in enumerate(prompts):
            r = call_ollama(host=host, model=model, prompt=prompt)
            results.append(r)
            (out_dir / f"{model}_prompt_{i:02d}.json").write_text(json.dumps(r, indent=2))

    (out_dir / "summary.json").write_text(json.dumps(results, indent=2))
    print(f"Wrote {len(results)} results to {out_dir}")


if __name__ == "__main__":
    main()
```

Benchmark hygiene notes:

- consider a warmup run per model (do not record it) to avoid counting model load time
- keep prompts short enough that you are comparing models, not just comparing how long tokenization takes
- avoid changing the prompt set while you compare models (version your prompt list)

---

## Warmup runs

First request to a model is often slower (model loading):

```python
def warmup_model(host: str, model: str) -> None:
    """
    Warm up model by making a throwaway request.
    """
    try:
        call_ollama(host=host, model=model, prompt="test")
        print(f"Warmed up {model}")
    except Exception as e:
        print(f"Warmup failed for {model}: {e}")


# Before benchmarking:
for model in models:
    warmup_model(host, model)
    time.sleep(1)  # Brief pause between warmups
```

---

## Analyzing results

```python
import json
import statistics
from pathlib import Path


def analyze_benchmark(results_dir: Path) -> None:
    """
    Compute latency statistics and quality metrics.
    """
    summary_path = results_dir / "summary.json"
    results = json.loads(summary_path.read_text())
    
    # Group by model
    by_model = {}
    for r in results:
        model = r["model"]
        if model not in by_model:
            by_model[model] = []
        by_model[model].append(r)
    
    # Compute stats
    print("## Latency Statistics\n")
    for model, runs in by_model.items():
        latencies = [r["latency_s"] for r in runs]
        print(f"**{model}**:")
        print(f"  - Mean: {statistics.mean(latencies):.2f}s")
        print(f"  - Median: {statistics.median(latencies):.2f}s")
        print(f"  - P95: {sorted(latencies)[int(len(latencies)*0.95)]:.2f}s")
        print(f"  - Max: {max(latencies):.2f}s")
        print()
    
    # Quality checks
    print("## Quality Checks\n")
    for model, runs in by_model.items():
        json_failures = 0
        for r in runs:
            # Try parsing response as JSON if prompt requested JSON
            if "JSON" in r["prompt"]:
                try:
                    json.loads(r["response"])
                except json.JSONDecodeError:
                    json_failures += 1
        
        print(f"**{model}**: {json_failures}/{len(runs)} JSON parse failures")


# Usage
analyze_benchmark(Path("benchmark_outputs"))
```

---

## How to compare models

Compare:

- **Speed**: average latency + slowest case (P95/P99)
- **Quality**: read saved outputs for:
  - correctness
  - adherence to format
  - completeness

### Speed comparison

Create a comparison table:

| Model | Mean (s) | P95 (s) | Max (s) | Requests/min |
|-------|----------|---------|---------|--------------|
| llama3.2:1b | 0.8 | 1.2 | 1.5 | 75 |
| llama3.1:8b | 3.2 | 4.5 | 5.1 | 19 |

### Quality heuristics (no heavy math required)

For JSON prompts:
```python
def check_json_quality(response: str) -> dict:
    """
    Simple quality checks for JSON responses.
    """
    try:
        data = json.loads(response)
        return {
            "valid_json": True,
            "has_required_keys": all(k in data for k in ["name", "email"]),
            "no_extra_text": response.strip().startswith("{"),
        }
    except json.JSONDecodeError:
        return {
            "valid_json": False,
            "has_required_keys": False,
            "no_extra_text": False,
        }
```

For extraction tasks:
- Count how many required keys are present
- Check for hallucinated values (e.g., "N/A", "Unknown")

For summaries:
- Check if within length limit
- Verify key facts are mentioned (simple substring search)

---

## Full benchmark script with analysis

```python
import json
import statistics
import time
from pathlib import Path
from typing import List

import requests


def call_ollama(host: str, model: str, prompt: str) -> dict:
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    t0 = time.time()
    resp = requests.post(url, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    return {
        "model": model,
        "prompt": prompt,
        "response": data.get("response", ""),
        "latency_s": time.time() - t0,
    }


def warmup_model(host: str, model: str) -> None:
    try:
        call_ollama(host=host, model=model, prompt="test")
        print(f"✓ Warmed up {model}")
    except Exception as e:
        print(f"✗ Warmup failed for {model}: {e}")


def run_benchmark(
    host: str,
    models: List[str],
    prompts: List[str],
    output_dir: Path,
    warmup: bool = True
) -> None:
    """
    Run benchmark with warmup and analysis.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Warmup
    if warmup:
        print("Warming up models...")
        for model in models:
            warmup_model(host, model)
            time.sleep(1)
        print()
    
    # Benchmark
    print("Running benchmark...")
    results = []
    for model in models:
        for i, prompt in enumerate(prompts):
            print(f"  {model} prompt {i+1}/{len(prompts)}...", end=" ")
            try:
                r = call_ollama(host=host, model=model, prompt=prompt)
                results.append(r)
                print(f"{r['latency_s']:.2f}s")
                
                # Save individual result
                (output_dir / f"{model}_prompt_{i:02d}.json").write_text(
                    json.dumps(r, indent=2)
                )
            except Exception as e:
                print(f"FAILED: {e}")
    
    # Save summary
    (output_dir / "summary.json").write_text(json.dumps(results, indent=2))
    print(f"\nWrote {len(results)} results to {output_dir}")


def main() -> None:
    host = "http://localhost:11434"
    models = ["llama3.2:1b", "llama3.1:8b"]
    prompts = [
        "Summarize: Large language models are useful but require careful evaluation.",
        "Extract JSON with keys {name, email} from: 'Name: Sam, Email: sam@example.com'",
        "Write 3 bullet points about caching.",
    ]
    
    run_benchmark(
        host=host,
        models=models,
        prompts=prompts,
        output_dir=Path("benchmark_outputs"),
        warmup=True
    )


if __name__ == "__main__":
    main()
```

---

## Interpreting results

**Speed vs Quality tradeoff:**
- Smaller models (1B-3B): fast but may have lower quality
- Larger models (7B-13B): slower but often better quality

**When to prefer smaller models:**
- Latency is critical
- Simple tasks (classification, short extraction)
- High throughput needed

**When to prefer larger models:**
- Quality is critical
- Complex reasoning required
- Can tolerate higher latency

---

## Practice notebook

For hands-on benchmarking exercises and statistical analysis, see:
- **[03_benchmarking_script.ipynb](./03_benchmarking_script.ipynb)** - Interactive benchmarking
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## References

- Python `time`: https://docs.python.org/3/library/time.html
- Python `statistics`: https://docs.python.org/3/library/statistics.html
- NumPy percentiles (for larger datasets): https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
