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

## Underlying theory: benchmarking is measurement under controlled conditions

You are trying to estimate two things:

- **speed** (latency / throughput)
- **quality** (correctness, format adherence, completeness)

The key rule is controlling variables:

- same prompts
- same settings
- same machine state as much as possible

Latency is a distribution, not a single number. Two useful summaries:

- average latency (typical case)
- slowest case / tail latency (worst case)

Practical implication: a model that is “fast on average” but has very slow worst cases may still feel bad in a demo.

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

## How to compare models

Compare:

- **Speed**: average latency + slowest case
- **Quality**: read saved outputs for:
  - correctness
  - adherence to format
  - completeness

If you want a simple “quality heuristic” without heavy math:

- for JSON prompts: count parse failures
- for extraction: check if required keys exist
- for summaries: check length caps and whether key facts are present

---

## References

- Python `time`: https://docs.python.org/3/library/time.html
- Python `timeit`: https://docs.python.org/3/library/timeit.html
