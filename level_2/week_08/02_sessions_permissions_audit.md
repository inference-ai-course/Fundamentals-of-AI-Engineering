# Week 8 — Part 02: Sessions, permissions, auditing (minimum viable)

## Overview

When you add ingestion/admin endpoints, you must think about:

- permissions
- auditing
- cost control

---

## Underlying theory: authn, authz, and least privilege

### Authentication vs authorization

- authentication (authn): who are you?
- authorization (authz): what are you allowed to do?

Many systems fail because they implement authn (a token) but forget authz (which endpoints that token can call).

### Least privilege (why roles exist)

Admin endpoints have higher blast radius:

- `/ingest` can change the knowledge base
- `/eval` can spend tokens/cost and leak prompts in logs

So you want the minimal set of permissions needed for each role.

---

## Minimum viable roles

- user: chat
- admin: ingest/eval

Log admin actions:

- who
- what
- when

Practical rule:

- default deny for admin routes
- explicitly grant admin access via one mechanism (API key or auth)

---

## Minimal auth options (choose one)

For course scope, pick the simplest that is still real:

- **Static API key header** (easiest)
- **HTTP Basic auth** (ok for demos)
- **OAuth2 / JWT** (only if you already know it)

The important part is:

- admin endpoints are not publicly callable

---

## Audit log entry (example)

```json
{
  "request_id": "...",
  "actor": "admin",
  "action": "ingest",
  "resource": "data/manual.pdf",
  "timestamp": "2026-01-27T06:55:00Z",
  "status": "success"
}
```

Store it in logs at minimum. If you want extra credit, store it in a small file/db.

## Audit log theory (why it helps)

An audit log is useful when it is:

- append-only (or at least tamper-evident)
- attributable (you can identify the actor)
- time-ordered (timestamps)

This is how you can answer: “who changed the KB right before the system started failing?”

---

## Cost controls

- cap max tokens
- cap retrieved context size
- cap agent steps
- rate limit expensive endpoints

---

## References

- FastAPI security: https://fastapi.tiangolo.com/tutorial/security/
- HTTP 401: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
- HTTP 403: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
