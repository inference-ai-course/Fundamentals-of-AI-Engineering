#!/usr/bin/env python3
"""
Benchmark script for comparing local LLM models via Ollama.

Usage:
    python benchmark_local_llm.py --models llama3.2:1b llama3.1:8b --output-dir benchmark_outputs

This script:
- Runs the same prompt set across multiple models
- Records latency for each run
- Saves individual outputs and a summary JSON
"""

import argparse
import json
import statistics
import time
from pathlib import Path
from typing import Any, Dict, List

import requests


# Default prompt set for benchmarking
DEFAULT_PROMPTS = [
    "Summarize: Large language models are useful but require careful evaluation.",
    "Extract JSON with keys {name, email} from: 'Name: Sam, Email: sam@example.com'",
    "Write 3 bullet points about caching.",
    "What is the capital of France? Answer in one sentence.",
    "Translate to Spanish: 'Hello, how are you?'",
]


def call_ollama(
    host: str,
    model: str,
    prompt: str,
    timeout_s: float = 120.0
) -> Dict[str, Any]:
    """Call Ollama API and return result with latency."""
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    
    t0 = time.time()
    resp = requests.post(url, json=payload, timeout=timeout_s)
    resp.raise_for_status()
    data = resp.json()
    
    return {
        "model": model,
        "prompt": prompt,
        "response": data.get("response", ""),
        "latency_s": time.time() - t0,
    }


def warmup_model(host: str, model: str) -> bool:
    """Warm up model by making a throwaway request."""
    try:
        call_ollama(host=host, model=model, prompt="test", timeout_s=120.0)
        print(f"  ✓ Warmed up {model}")
        return True
    except Exception as e:
        print(f"  ✗ Warmup failed for {model}: {e}")
        return False


def list_local_models(host: str) -> List[str]:
    """List available models from Ollama."""
    url = f"{host}/api/tags"
    resp = requests.get(url, timeout=5.0)
    resp.raise_for_status()
    data = resp.json()
    return [m.get("name") for m in data.get("models", []) if m.get("name")]


def run_benchmark(
    host: str,
    models: List[str],
    prompts: List[str],
    output_dir: Path,
    warmup: bool = True
) -> List[Dict[str, Any]]:
    """Run benchmark across all models and prompts."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Warmup
    if warmup:
        print("\n## Warming up models...")
        for model in models:
            warmup_model(host, model)
            time.sleep(0.5)
    
    # Benchmark
    print("\n## Running benchmark...")
    results = []
    
    for model in models:
        for i, prompt in enumerate(prompts):
            print(f"  {model} prompt {i+1}/{len(prompts)}...", end=" ", flush=True)
            try:
                r = call_ollama(host=host, model=model, prompt=prompt)
                results.append(r)
                print(f"{r['latency_s']:.2f}s")
                
                # Save individual result
                safe_model = model.replace(":", "_")
                out_path = output_dir / f"{safe_model}_prompt_{i:02d}.json"
                out_path.write_text(json.dumps(r, indent=2), encoding="utf-8")
                
            except Exception as e:
                print(f"FAILED: {e}")
                results.append({
                    "model": model,
                    "prompt": prompt,
                    "response": "",
                    "latency_s": None,
                    "error": str(e),
                })
    
    return results


def compute_summary(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute latency statistics grouped by model."""
    by_model: Dict[str, List[float]] = {}
    
    for r in results:
        model = r["model"]
        if r.get("latency_s") is not None:
            if model not in by_model:
                by_model[model] = []
            by_model[model].append(r["latency_s"])
    
    summary = {"models": {}}
    for model, latencies in by_model.items():
        if latencies:
            summary["models"][model] = {
                "n": len(latencies),
                "mean_latency_s": round(statistics.mean(latencies), 3),
                "median_latency_s": round(statistics.median(latencies), 3),
                "min_latency_s": round(min(latencies), 3),
                "max_latency_s": round(max(latencies), 3),
                "p95_latency_s": round(sorted(latencies)[int(len(latencies) * 0.95)], 3) if len(latencies) > 1 else latencies[0],
            }
    
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Benchmark local LLM models via Ollama"
    )
    parser.add_argument(
        "--models", 
        nargs="+", 
        help="Model names to benchmark (default: auto-detect from Ollama)"
    )
    parser.add_argument(
        "--prompts-file",
        type=Path,
        help="JSON file with list of prompts (optional)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("benchmark_outputs"),
        help="Output directory for results"
    )
    parser.add_argument(
        "--host",
        default="http://localhost:11434",
        help="Ollama host URL"
    )
    parser.add_argument(
        "--no-warmup",
        action="store_true",
        help="Skip warmup runs"
    )
    args = parser.parse_args()
    
    # Get models
    if args.models:
        models = args.models
    else:
        try:
            models = list_local_models(args.host)
            if not models:
                print("No models found. Pull a model first: ollama pull <model>")
                exit(1)
            print(f"Auto-detected models: {models}")
        except Exception as e:
            print(f"Error listing models: {e}")
            print("Ensure Ollama is running: ollama serve")
            exit(1)
    
    # Get prompts
    if args.prompts_file:
        prompts = json.loads(args.prompts_file.read_text())
    else:
        prompts = DEFAULT_PROMPTS
    
    print(f"Models: {models}")
    print(f"Prompts: {len(prompts)}")
    print(f"Output: {args.output_dir}")
    
    # Run benchmark
    results = run_benchmark(
        host=args.host,
        models=models,
        prompts=prompts,
        output_dir=args.output_dir,
        warmup=not args.no_warmup
    )
    
    # Compute and save summary
    summary = compute_summary(results)
    summary["config"] = {
        "models": models,
        "n_prompts": len(prompts),
        "host": args.host,
    }
    
    summary_path = args.output_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    
    # Print summary
    print("\n## Summary\n")
    print(f"Total runs: {len(results)}")
    print(f"Results saved to: {args.output_dir}")
    print()
    
    for model, stats in summary.get("models", {}).items():
        print(f"**{model}**:")
        print(f"  - Mean: {stats['mean_latency_s']:.2f}s")
        print(f"  - Median: {stats['median_latency_s']:.2f}s")
        print(f"  - P95: {stats['p95_latency_s']:.2f}s")
        print(f"  - Max: {stats['max_latency_s']:.2f}s")
        print()


if __name__ == "__main__":
    main()
