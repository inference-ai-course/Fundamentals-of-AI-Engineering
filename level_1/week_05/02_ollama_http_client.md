# Week 5 — Part 02: Calling Ollama via HTTP (minimal client)

## Overview

Ollama exposes a local HTTP API. This lets you treat local inference like a normal service call.

---

## Underlying theory: local inference is still a distributed system (just smaller)

Even though the model is on your machine, your Python script is still making a network-style call:

- your client process sends a request
- the Ollama server process does work
- you receive a response (or a failure)

So the same engineering principles apply:

- always set timeouts
- log failures with enough context to debug
- treat response parsing as untrusted input (validate what you need)

We’ll implement a minimal `call_ollama.py` that:

- sends a prompt
- receives text output
- prints it

---

## Minimal client (Python)

Dependencies:

```txt
requests==2.32.3
```

Code:

```python
import argparse
import json
import time

import requests


def call_ollama(model: str, prompt: str, host: str = "http://localhost:11434") -> dict:
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    t0 = time.time()
    resp = requests.post(url, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    data["latency_s"] = time.time() - t0
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--host", default="http://localhost:11434")
    args = parser.parse_args()

    out = call_ollama(model=args.model, prompt=args.prompt, host=args.host)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
```

Two practical notes:

- `timeout=60` is a policy choice. Slower hardware or larger models may need longer.
- when you later build a benchmark, consider warmup: the first call can be slower due to model loading.

---

## How to run

```bash
python call_ollama.py --model llama3.1 --prompt "Say hello in one sentence"
```

If this works, you’ve proven local inference end-to-end.

---

## Common pitfalls

- Ollama service not running
- wrong model name
- timeouts for slow hardware

---

## References

- Ollama docs/issues: https://github.com/ollama/ollama
- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
