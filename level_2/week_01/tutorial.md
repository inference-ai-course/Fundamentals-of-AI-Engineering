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

1. Read 01 and draft architecture for your project.
2. Read 02 and get the service running locally.
3. Read 03 and add debuggability.

Why this order works:

1. **Architecture first**
    - A written contract prevents “coding into ambiguity”. It forces you to decide schemas and error behavior up front.
    - What to verify: you can write an example request/response for `/search` and `/chat` without looking at code.

2. **Runnable service second**
    - Once the skeleton starts, you can test incrementally and avoid building everything in a vacuum.
    - What to verify: `GET /health` works locally and `/docs` shows your endpoints.

3. **Debuggability third**
    - If something breaks, you need to locate the failure quickly (request_id + structured logs).
    - What to verify: every error response includes a `request_id` and you can find the matching logs.

## What “done” looks like

- You can start the API locally and hit `GET /health`.
- `POST /search` and `POST /chat` have a written request/response example (even if not fully implemented yet).
- Errors are standardized (4xx vs 5xx) and responses include a `request_id`.
- You can open Swagger docs at `/docs` and see your endpoints.

## References

- FastAPI docs: https://fastapi.tiangolo.com/
- OpenAPI spec: https://spec.openapis.org/oas/latest.html
- Pydantic (models/validation): https://docs.pydantic.dev/
