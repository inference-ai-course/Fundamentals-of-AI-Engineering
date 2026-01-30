# Week 5 — Part 02: Calling Ollama via HTTP (minimal client)

## Overview

Ollama exposes a local HTTP API. This lets you treat local inference like a normal service call.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on local inference and model/platform fundamentals:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 4: Hugging Face Platform and Local Inference](../../level_0/Chapters/4/Chapter4.md)

Why it matters here (Week 5):

- Even “local” inference is still a client/server boundary (your script calls a local service).
- Use timeouts and treat responses as untrusted input (parse/validate what you depend on).

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

Expected output:
```json
{
  "model": "llama3.1",
  "created_at": "2024-01-30T03:15:22.123Z",
  "response": "Hello! Nice to meet you!",
  "done": true,
  "latency_s": 2.34
}
```

---

## Enhanced client with error handling

```python
import argparse
import json
import time
from typing import Optional

import requests


def call_ollama(
    model: str,
    prompt: str,
    host: str = "http://localhost:11434",
    timeout_s: float = 60.0
) -> dict:
    """
    Call Ollama API with timeout and error handling.
    
    Returns:
        Response dict with added latency_s field
        
    Raises:
        ConnectionError: If Ollama service is not reachable
        TimeoutError: If request exceeds timeout
        ValueError: If model not found
    """
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    
    t0 = time.time()
    
    try:
        resp = requests.post(url, json=payload, timeout=timeout_s)
        resp.raise_for_status()
        
    except requests.ConnectionError:
        raise ConnectionError(
            f"Cannot connect to Ollama at {host}. "
            "Is the service running? Run: ollama serve"
        )
    except requests.Timeout:
        raise TimeoutError(
            f"Request timed out after {timeout_s}s. "
            "Try a smaller model or increase timeout."
        )
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            raise ValueError(
                f"Model '{model}' not found. "
                "Pull it first: ollama pull {model}"
            )
        raise
    
    data = resp.json()
    data["latency_s"] = time.time() - t0
    return data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Call Ollama API with a prompt"
    )
    parser.add_argument("--model", required=True, help="Model name (e.g., llama3.1)")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--host", default="http://localhost:11434")
    parser.add_argument("--timeout", type=float, default=60.0)
    args = parser.parse_args()

    try:
        out = call_ollama(
            model=args.model,
            prompt=args.prompt,
            host=args.host,
            timeout_s=args.timeout
        )
        print(json.dumps(out, indent=2))
    except (ConnectionError, TimeoutError, ValueError) as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
```

---

## Streaming responses (optional)

For real-time output, use streaming:

```python
def call_ollama_stream(model: str, prompt: str, host: str = "http://localhost:11434"):
    """
    Stream responses token-by-token.
    """
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,  # Enable streaming
    }
    
    resp = requests.post(url, json=payload, stream=True, timeout=120)
    resp.raise_for_status()
    
    for line in resp.iter_lines():
        if line:
            chunk = json.loads(line)
            if chunk.get("response"):
                print(chunk["response"], end="", flush=True)
            if chunk.get("done"):
                print()  # Newline at end
                return chunk
```

**When to use streaming:**
- Interactive applications (show progress)
- Long responses (user sees partial results)

**When not to use streaming:**
- Benchmarking (need total latency)
- Batch processing (need complete response)

---

## Common pitfalls

### Pitfall 1: Ollama service not running

**Symptom**: `ConnectionError: Cannot connect to http://localhost:11434`

**Diagnosis**:
```bash
curl http://localhost:11434/api/tags
# If fails: service not running
```

**Fix**:
```bash
# Start Ollama in a separate terminal
ollama serve
```

---

### Pitfall 2: Wrong model name

**Symptom**: `404 error` or "model not found"

**Diagnosis**:
```bash
ollama list
# Check available models
```

**Fix**:
```bash
# Pull the model first
ollama pull llama3.1
```

---

### Pitfall 3: Timeouts on slow hardware

**Symptom**: Request times out after 60s

**Diagnosis**: Model is too large or hardware too slow

**Fix**:
- Increase timeout: `--timeout 120`
- Use smaller model: `llama3.2:1b` instead of `llama3.1:8b`
- First request is slow (model loading) - subsequent ones faster

---

### Pitfall 4: JSON parsing errors

**Symptom**: `json.JSONDecodeError`

**Diagnosis**: Response format unexpected

**Fix**:
```python
try:
    data = resp.json()
except json.JSONDecodeError:
    print("Raw response:", resp.text[:500])
    raise
```

---

## Practice notebook

For hands-on HTTP client exercises and benchmarking, see:
- **[02_ollama_http_client.ipynb](./02_ollama_http_client.ipynb)** - Interactive client development
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## References

- Ollama API docs: https://github.com/ollama/ollama/blob/main/docs/api.md
- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
- Requests error handling: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
