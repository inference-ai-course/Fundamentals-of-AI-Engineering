#!/usr/bin/env python3
"""
Minimal HTTP client for Ollama local inference.

Usage:
    python call_ollama.py --model llama3.1 --prompt "Say hello in one sentence"
"""

import argparse
import json
import time

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
        "options": {"temperature": 0.0},
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
                f"Pull it first: ollama pull {model}"
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
    parser.add_argument("--host", default="http://localhost:11434", help="Ollama host URL")
    parser.add_argument("--timeout", type=float, default=60.0, help="Timeout in seconds")
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
