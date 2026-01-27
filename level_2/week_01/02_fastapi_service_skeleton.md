# Week 1 — Part 02: FastAPI service skeleton (config, logging, health check)

## Overview

A “runnable service” means:

- another developer can follow README steps
- start the API
- call `/health`
- see a successful response

This section gives a minimal FastAPI skeleton you can reuse.

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

## References

- FastAPI: https://fastapi.tiangolo.com/
- Uvicorn: https://www.uvicorn.org/
- Python logging: https://docs.python.org/3/library/logging.html
- python-dotenv: https://github.com/theskumar/python-dotenv
- Pydantic settings: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
