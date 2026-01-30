# Week 1 — Part 02: FastAPI service skeleton (config, logging, health check)

## Overview

A “runnable service” means:

- another developer can follow README steps
- start the API
- call `/health`
- see a successful response

This section gives a minimal FastAPI skeleton you can reuse.

---

## Underlying theory: “liveness” vs “readiness” are different contracts

In a service, health endpoints are *contracts* that other systems (humans, scripts, deployers) rely on.

### Liveness (process-level)

**Definition**: liveness answers “is the process running and able to respond to HTTP at all?”

Practical intuition:

- liveness should be cheap and rarely fail
- it’s used to detect crashes / deadlocks
- it should not depend on external services

`GET /health` is commonly used as liveness.

### Readiness (dependency-level)

**Definition**: readiness answers “is the process *ready to serve real traffic*?”

Readiness checks often validate:

- vector store connectivity
- required environment variables exist (API keys)
- model provider is reachable (optional; can be too slow)

`GET /ready` is commonly used as readiness.

Practical warning:

- if readiness is too strict or slow, it becomes flaky and noisy
- if readiness is too lax, you ship a service that returns 500s for all real requests

---

## Underlying theory: configuration is an interface (not a pile of globals)

Configuration is how you connect the same code to different environments.

Practical rule:

- code should be identical between dev and prod
- config selects behavior (keys, endpoints, persistence paths, log level)

Intuition:

- when config is scattered (`os.environ.get(...)` everywhere), you can’t easily audit what the service depends on
- when config is centralized (a `Settings` object), you can validate it once at startup and fail fast

This is why Pydantic settings is a common pattern: a typed “config contract”.

---

## Suggested minimal project layout

For Level 2, a simple layout is enough:

- `app/main.py` (FastAPI entrypoint)
- `app/schemas.py` (Pydantic request/response models)
- `app/settings.py` (config/env)
- `app/logging_config.py` (optional: logging setup)

---

## Minimal `app/main.py`

```python
import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI(title="Level2 Service")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

You can also add a “ready” endpoint later (e.g., checks vector DB connectivity):

- `GET /ready`

This helps you separate “process is up” from “dependencies are working”.

---

## Run locally

You typically run with Uvicorn:

```bash
uvicorn app.main:app --reload --port 8000
```

Then:

- open `http://localhost:8000/health`
- open `http://localhost:8000/docs`

---

## Config via `.env`

A minimal approach:

- keep secrets in environment variables
- load `.env` in development

```python
import os

MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o-mini")
```

A more scalable pattern is to use Pydantic settings.

Example `app/settings.py`:

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_name: str = "gpt-4o-mini"
    log_level: str = "INFO"


settings = Settings()
```

Then in `app/main.py` you can read `settings.model_name`.

This avoids scattered `os.environ.get(...)` calls and makes configuration testable.

---

## Practical usage: minimum structured logging fields

The goal of logging in this course is debuggability, not “logging everything”.

Minimum fields worth standardizing early:

- `request_id`
- `path`
- `method`
- `status_code`
- `latency_ms`
- `component` (e.g., `api`, `ingest`, `search`, `chat`)

Why this matters:

- if a user reports a failure with a `request_id`, you can find the exact log lines
- if latency spikes, you can separate “slow model call” from “slow vector store” later (Week 9 tracing)

---

## References

- FastAPI: https://fastapi.tiangolo.com/
- Uvicorn: https://www.uvicorn.org/
- Python logging: https://docs.python.org/3/library/logging.html
- python-dotenv: https://github.com/theskumar/python-dotenv
- Pydantic settings: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
