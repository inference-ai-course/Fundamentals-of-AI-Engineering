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

## Concrete permission checking example

```python
from enum import Enum
from fastapi import HTTPException, Header

class Role(Enum):
    USER = "user"
    ADMIN = "admin"

# Simple role mapping (in production, use a real auth system)
API_KEYS = {
    "user_key_123": Role.USER,
    "admin_key_456": Role.ADMIN,
}

def get_role(api_key: str = Header(alias="x-api-key")) -> Role:
    """Extract role from API key header."""
    role = API_KEYS.get(api_key)
    if not role:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return role

def require_admin(role: Role):
    """Require admin role or raise 403."""
    if role != Role.ADMIN:
        raise HTTPException(status_code=403, detail="Admin access required")

# Example protected endpoint
@app.post("/ingest")
def ingest_endpoint(role: Role = Depends(get_role)):
    require_admin(role)
    # ... ingest logic
    make_audit_entry(actor=role.value, action="ingest", resource="...")
    return {"status": "ingested"}
```

### Worked example: permission flow

**User tries to call /ingest:**
1. Request includes `x-api-key: user_key_123`
2. `get_role()` resolves to `Role.USER`
3. `require_admin()` sees `Role.USER != Role.ADMIN`
4. Returns HTTP 403: "Admin access required"

**Admin calls /ingest:**
1. Request includes `x-api-key: admin_key_456`
2. `get_role()` resolves to `Role.ADMIN`
3. `require_admin()` passes
4. Ingest proceeds and audit entry is logged

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

### Minimal audit logging implementation

```python
import json
import logging
from datetime import datetime

audit_logger = logging.getLogger("audit")

def make_audit_entry(actor: str, action: str, resource: str, status: str = "success", metadata: dict = None):
    """Log an audit entry for admin actions."""
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "actor": actor,
        "action": action,
        "resource": resource,
        "status": status,
        "metadata": metadata or {}
    }
    # Log as structured JSON
    audit_logger.info(json.dumps(entry))
    
    # Optional: also append to audit file
    with open("audit.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
```

### Why audit logs help during incidents

**Scenario:** System started returning wrong answers at 3pm.

**Question:** What changed?

**Audit log investigation:**
```bash
$ grep '"action": "ingest"' audit.jsonl | grep "2026-01-27T14"
{"timestamp":"2026-01-27T14:47:00Z","actor":"admin","action":"ingest","resource":"data/updated_docs.pdf","status":"success"}
```

**Finding:** Someone ingested new docs at 2:47pm, right before failures started.

**Next step:** Inspect `data/updated_docs.pdf` for bad chunking or conflicting content.

## Audit log theory (why it helps)

An audit log is useful when it is:

- append-only (or at least tamper-evident)
- attributable (you can identify the actor)
- time-ordered (timestamps)

This is how you can answer: "who changed the KB right before the system started failing?"

---

## Cost controls

- cap max tokens
- cap retrieved context size
- cap agent steps
- rate limit expensive endpoints

### 1. Cap max tokens per request
```python
MAX_OUTPUT_TOKENS = 1000

def call_llm_with_budget(prompt: str, max_tokens: int = MAX_OUTPUT_TOKENS) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=min(max_tokens, MAX_OUTPUT_TOKENS)  # Enforce cap
    )
    return response.choices[0].message.content
```

### 2. Cap retrieved context size
```python
MAX_CHUNKS_PER_REQUEST = 10

def retrieve_with_budget(query: str, top_k: int) -> list:
    # Enforce hard cap on retrieval
    actual_k = min(top_k, MAX_CHUNKS_PER_REQUEST)
    return vector_db.query(query=query, top_k=actual_k)
```

### 3. Rate limit expensive endpoints
```python
from fastapi_limiter.depends import RateLimiter

@app.post("/chat", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
def chat_endpoint(req: ChatRequest):
    # Max 10 requests per minute per user
    ...
```

---

## References

- FastAPI security: https://fastapi.tiangolo.com/tutorial/security/
- HTTP 401: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
- HTTP 403: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/
