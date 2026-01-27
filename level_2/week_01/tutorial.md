# Level 2 — Week 1 Tutorials

## Overview

Week 1 is about turning requirements into a runnable service skeleton.

You will practice:

- decomposing requirements into modules
- designing API contracts (request/response + errors)
- bootstrapping a FastAPI service with config + logging + health checks

## Navigation

- [01 — Requirements → architecture → API contracts](01_requirements_to_architecture.md)
- [02 — FastAPI service skeleton (config, logging, health check)](02_fastapi_service_skeleton.md)
- [03 — Error handling + request IDs (debuggability)](03_error_handling_request_ids.md)

## Recommended order

1. Read 01 and write the API contract first.
2. Read 02 and get the service running locally.
3. Read 03 and add debuggability.

Use [practice.ipynb](practice.ipynb) for additional work.

## What “done” looks like

- You can start the API locally and hit `GET /health`.
- `POST /search` and `POST /chat` have a written request/response example (even if not fully implemented yet).
- Errors are standardized (4xx vs 5xx) and responses include a `request_id`.
- You can open Swagger docs at `/docs` and see your endpoints.

## References

- FastAPI docs: https://fastapi.tiangolo.com/
- OpenAPI spec: https://spec.openapis.org/oas/latest.html
- Pydantic (models/validation): https://docs.pydantic.dev/
