# Week 1 — Part 03: Error handling + request IDs (debuggability)

## Overview

In services, failures are normal. The difference between a demo and a production-ish system is:

- failures are explainable
- logs are searchable

A **request ID** is the simplest tracing tool.

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
