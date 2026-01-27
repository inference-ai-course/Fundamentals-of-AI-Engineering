# Level 2 — Week 8 Tutorials

## Overview

Week 8 focuses on productization:

- package as a demo-ready service
- add admin ingestion + feedback entry points
- keep UI and API boundaries clean

Underlying theory you should internalize this week:

- the UI is an untrusted client; the backend is the policy enforcement point
- admin endpoints have higher blast radius, so least privilege + audit logs matter
- reproducibility is an interface: behavior depends on (code, data, config)

## Navigation

- [01 — Endpoint map + product boundaries](01_endpoint_map_boundaries.md)
- [02 — Sessions, permissions, auditing (minimum viable)](02_sessions_permissions_audit.md)
- [03 — Demo packaging checklist (one-command run)](03_demo_packaging.md)

## Recommended order

1. Read 01 and define endpoint boundaries.
2. Read 02 and add minimal access control.
3. Read 03 and make demo reproducible.

Why this order works:

1. **Boundaries first**
    - If you don’t separate user vs admin capabilities, you can’t enforce policy correctly.
    - What to verify: you can list user endpoints vs admin endpoints and what each can do.

2. **Access control second**
    - Admin actions (ingest/eval) have high blast radius. Protect them early.
    - What to verify: admin endpoints reject unauthorized requests and create audit logs.

3. **Reproducible demo third**
    - Productization is only real if a teammate can run it from README.
    - What to verify: a one-command run works on a clean machine with only documented steps.

## What “done” looks like

- You have an endpoint map with:
  - user endpoints
  - admin endpoints
  - system endpoints
- Admin endpoints are protected (even a simple API key is acceptable for this course).
- Admin actions are logged (who/what/when, with a request_id).
- A teammate can run the demo from README without extra instructions.

## References

- FastAPI security tutorial: https://fastapi.tiangolo.com/tutorial/security/
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
