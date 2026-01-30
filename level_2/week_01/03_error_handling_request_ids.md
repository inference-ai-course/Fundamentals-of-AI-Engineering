# Week 1 — Part 03: Error handling + request IDs (debuggability)

## Overview

In services, failures are normal. The difference between a demo and a production-ish system is:

- failures are explainable
- logs are searchable

A **request ID** is the simplest tracing tool.

---

## Underlying theory: request IDs are correlation, not “distributed tracing” (yet)

In Week 1, a request ID is mainly a *correlation key*:

- the client receives a `request_id`
- the server logs the same `request_id`
- you can join “user-reported failure” to “what the server saw”

Intuition:

- correlation answers “which log lines belong to this request?”
- tracing (later) answers “which internal steps happened, in what order, and how long did each take?”

In later weeks, you’ll often have multiple IDs:

- `request_id` (edge correlation)
- `trace_id` (span-based tracing)
- `session_id` / `user_id` (auth context)

For now, request ID alone gives you most of the debugging benefit with minimal complexity.

---

## Standardize error behavior

Two categories:

- **4xx**: client sent bad input
- **5xx**: server failed internally

Good practice:

- return a short error message
- include `request_id` in the response
- log the full stack trace server-side

Also decide:

- when to return 422 (validation errors) vs 400 (bad request)
- whether you return one standard error shape for all endpoints

---

## Practical usage: when to use 422 vs 400 (FastAPI reality)

FastAPI + Pydantic will typically return:

- **422 Unprocessable Entity** when the request body is syntactically valid JSON, but fails schema validation
  - example: missing required field, wrong type, `top_k` out of range
- **400 Bad Request** when the request cannot be parsed as expected
  - example: invalid JSON, wrong content-type, malformed payload

Practical guidance for this course:

- don’t fight the framework: accept 422 for schema errors
- standardize your *own* error shape for domain failures (e.g., “collection not found”, “provider timeout”), typically as 4xx/5xx with your JSON error payload

The goal is consistency for the client and debuggability for you.

---

## Minimal request-id middleware pattern

```python
import uuid

from fastapi import Request


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("x-request-id") or str(uuid.uuid4())
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    return response
```

After this, you can include `request.state.request_id` in logs and error responses.

---

## Practical usage: propagate request IDs across boundaries

If a client provides `x-request-id`, you should honor it.

Why:

- your frontend / gateway / load balancer might already generate a request id
- keeping it stable across hops makes incidents easier to debug

Minimum propagation rules:

- accept incoming `x-request-id` if present
- otherwise generate a new UUID
- echo it back in the response header and error payload

Later (optional): support W3C Trace Context (`traceparent`) when you add full tracing.

---

## Minimal exception handler (example)

This pattern makes sure all “unexpected” errors return a stable JSON shape.

```python
from fastapi import Request
from fastapi.responses import JSONResponse


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    request_id = getattr(request.state, "request_id", None)
    # In real projects: log stack trace here.
    return JSONResponse(
        status_code=500,
        content={
            "error": {"type": "internal_error", "message": "Unexpected server error"},
            "request_id": request_id,
        },
    )
```

You can add more specific handlers (e.g., for timeouts) later.

---

## Underlying theory: error taxonomies reduce ambiguity

Even in a small course project, a tiny finite set of error types pays off.

Suggested (starter) error types:

- `invalid_request` (client fixable)
- `not_found` (missing resource)
- `rate_limited` (client should retry later)
- `provider_timeout` (upstream slow)
- `internal_error` (bug / unexpected)

Intuition:

- clients can implement consistent behavior (retry vs fix input vs show message)
- you can dashboard error counts by `error.type`

---

## Logging fields to standardize early

A useful minimum set:

- `request_id`
- `path`
- `component` (ingest/search/chat)
- `latency_ms`
- `status_code`
- `error_type` (optional but useful)
- `user_id` or `session_id` (if applicable)

---

## References

- W3C trace context: https://www.w3.org/TR/trace-context/
- Python errors/exceptions: https://docs.python.org/3/tutorial/errors.html
- RFC 7807 (Problem Details): https://www.rfc-editor.org/rfc/rfc7807
