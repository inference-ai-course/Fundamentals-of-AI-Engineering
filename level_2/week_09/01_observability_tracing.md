# Week 9 — Part 01: Observability and tracing

## Overview

- Logs + request IDs answer: “what happened?”
- Traces answer: “where did time go?”

Instrument:

- retrieval queries
- model calls
- agent steps

---

## Underlying theory: SLIs, SLOs, and why observability exists

### SLIs (what you measure)

An SLI (service level indicator) is a measurable quantity like:

- request latency
- error rate
- availability

### SLOs (what you promise)

An SLO is a target on an SLI, for example:

- 99% of `/chat` requests complete within 2 seconds
- error rate under 1% over a day

You don’t need full SRE practice for the course, but you should think in these terms because it forces clarity.

### Why percentiles (p50/p95) matter

Average latency hides tail problems.

- p50 tells you the typical case
- p95 tells you whether a meaningful fraction of users are suffering

In LLM systems, tail latency is common (network calls + retries + variable model times), so percentiles are more informative than means.

---

## Minimum observability package

- structured logs including request_id + component
- key counters:
  - ingestion docs/chunks
  - retrieval top_k and context length
  - model calls count
  - refusal rate

---

## Minimum log fields (practical)

Log at least:

- `request_id`
- `path`
- `status_code`
- `latency_ms`
- `component` (ingest/search/chat/agent)

For chat/RAG specifically:

- `top_k`
- `n_chunks_returned`
- `context_chars` or `context_tokens`
- `model_name`

---

## Tracing mental model

A trace is a tree of spans:

- root span: the HTTP request
- child span: retrieval
- child span: model call
- child span: citation validation

Even if you don’t deploy a full tracing backend, logging span durations gives you 80% of the value.

Theory intuition:

- a trace decomposes total latency into span costs
- the slowest path through dependent spans is the critical path

This is how you decide whether to optimize retrieval, model calls, or validation.

---

## Concrete implementation examples

### Example 1: Structured logging with context

```python
import logging
import json
import time
from contextvars import ContextVar

# Context variable to store request_id across async calls
request_id_var: ContextVar[str] = ContextVar("request_id", default="")

def setup_logging():
    """Configure structured JSON logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )

class StructuredLogger:
    def __init__(self, component: str):
        self.component = component
        self.logger = logging.getLogger(component)
    
    def log(self, event: str, **kwargs):
        """Log structured event with automatic request_id."""
        entry = {
            "timestamp": time.time(),
            "request_id": request_id_var.get(),
            "component": self.component,
            "event": event,
            **kwargs
        }
        self.logger.info(json.dumps(entry))

# Usage
logger = StructuredLogger("chat")
logger.log("chat_request_received", question="What is RAG?", top_k=5)
logger.log("retrieval_complete", n_hits=3, top_score=0.87, latency_ms=45)
logger.log("model_call_complete", model="gpt-4", latency_ms=1200)
```

### Example 2: Manual span tracking (simple tracing)

```python
from dataclasses import dataclass
from typing import Optional
import time

@dataclass
class Span:
    name: str
    start_ms: float
    end_ms: Optional[float] = None
    parent: Optional['Span'] = None
    
    def duration_ms(self) -> float:
        if self.end_ms is None:
            return 0.0
        return self.end_ms - self.start_ms

class SimpleTracer:
    def __init__(self):
        self.spans: list[Span] = []
    
    def start_span(self, name: str, parent: Optional[Span] = None) -> Span:
        span = Span(name=name, start_ms=time.time() * 1000, parent=parent)
        self.spans.append(span)
        return span
    
    def end_span(self, span: Span):
        span.end_ms = time.time() * 1000
    
    def get_critical_path(self) -> list[Span]:
        """Find the slowest sequential path through spans."""
        # Simple version: return all spans sorted by duration
        return sorted(self.spans, key=lambda s: s.duration_ms(), reverse=True)

# Usage in /chat endpoint
tracer = SimpleTracer()

root = tracer.start_span("chat_request")

retrieval_span = tracer.start_span("retrieval", parent=root)
hits = retrieve(query="What is RAG?", top_k=5)
tracer.end_span(retrieval_span)

model_span = tracer.start_span("model_call", parent=root)
answer = call_llm(prompt="...")
tracer.end_span(model_span)

validation_span = tracer.start_span("citation_validation", parent=root)
is_valid = validate_citations(answer["citations"], hits)
tracer.end_span(validation_span)

tracer.end_span(root)

# Log trace summary
for span in tracer.spans:
    logger.log("span_complete", 
               span_name=span.name, 
               duration_ms=span.duration_ms())
```

### Example 3: Percentile calculation for latency

```python
import statistics

def calculate_percentiles(latencies: list[float]) -> dict:
    """Calculate p50, p95, p99 from latency samples."""
    if not latencies:
        return {"p50": 0, "p95": 0, "p99": 0, "count": 0}
    
    sorted_latencies = sorted(latencies)
    n = len(sorted_latencies)
    
    def percentile(p: float) -> float:
        idx = int(n * p)
        return sorted_latencies[min(idx, n - 1)]
    
    return {
        "p50": percentile(0.50),
        "p95": percentile(0.95),
        "p99": percentile(0.99),
        "count": n
    }

# Example usage
chat_latencies = [1200, 1350, 980, 2100, 1150, 1400, 3200, 1050]
stats = calculate_percentiles(chat_latencies)
print(stats)
# Output: {"p50": 1200, "p95": 2100, "p99": 3200, "count": 8}
```

### Example 4: SLO monitoring (simple alert)

```python
def check_slo_breach(latencies: list[float], slo_ms: float, target_percentile: float = 0.95) -> dict:
    """Check if we're meeting our SLO."""
    stats = calculate_percentiles(latencies)
    p95 = stats["p95"]
    
    breach = p95 > slo_ms
    
    return {
        "slo_target_ms": slo_ms,
        "actual_p95_ms": p95,
        "breach": breach,
        "margin_ms": slo_ms - p95,
        "sample_count": stats["count"]
    }

# Usage
result = check_slo_breach(chat_latencies, slo_ms=2000)
if result["breach"]:
    logger.log("slo_breach", **result)
    # Trigger alert/investigation
```

### Worked example: debugging slow requests

**Scenario:** Users report `/chat` is slow.

**Step 1: Check logs for latency breakdown**
```bash
$ grep '"event":"span_complete"' logs.jsonl | grep '"request_id":"req_123"'
{"event":"span_complete","span_name":"retrieval","duration_ms":45}
{"event":"span_complete","span_name":"model_call","duration_ms":3200}
{"event":"span_complete","span_name":"citation_validation","duration_ms":12}
```

**Finding:** Model call took 3200ms (3.2s) - much longer than typical 1-1.5s.

**Step 2: Check model logs**
```bash
$ grep '"component":"llm"' logs.jsonl | grep '"request_id":"req_123"'
{"component":"llm","event":"model_call","model":"gpt-4","input_tokens":7800,"output_tokens":450}
```

**Finding:** Input was 7800 tokens - likely too much context.

**Step 3: Check retrieval**
```bash
$ grep '"event":"retrieval_complete"' logs.jsonl | grep '"request_id":"req_123"'
{"event":"retrieval_complete","n_hits":25,"context_chars":32000}
```

**Root cause:** Retrieved 25 chunks (too high `top_k`), creating 32k character context.

**Action:** Reduce `top_k` from 25 to 5-8, or implement context budget.

---

## References

- OpenTelemetry Python: https://opentelemetry.io/docs/languages/python/
- W3C trace context: https://www.w3.org/TR/trace-context/
- Logging in Python: https://docs.python.org/3/library/logging.html
