# Week 8 — Part 01: Endpoint map + product boundaries

## Overview

Keep the backend as the source of truth.

UI should:

- call APIs
- render results

Backend should:

- implement retrieval/chat/eval logic

---

## Underlying theory: trust boundaries and sources of truth

### Backend as the policy enforcement point

The backend is where you can enforce invariants:

- grounding and citation rules
- authz/authn
- rate limits and budgets
- consistent evaluation

If business logic is duplicated in UI and API, you create two divergent “truths”.

### UI is an untrusted environment

Even if you wrote the UI:

- users can modify front-end code in the browser
- requests can be replayed with curl/Postman

So any rule that matters must be enforced server-side.

---

## Endpoint map (example)

- User:
  - `/chat`
  - `/search` (debug)

- Admin:
  - `/ingest`
  - `/eval`

- System:
  - `/health`
  - `/ready` (optional: dependency checks)

---

## Boundary rule of thumb

- UI is responsible for:
  - gathering user input
  - calling APIs
  - rendering results (including citations)
- API is responsible for:
  - retrieval correctness
  - grounding + citations enforcement
  - evaluation and metrics

If logic exists in UI *and* API, it will diverge and you’ll debug two systems.

Practical implication:

- treat the UI as a client of an API, not as a place to “implement retrieval logic”

---

## Why `/search` should remain exposed (at least in dev)

`/search` is your debugging endpoint.

When a chat answer is wrong, `/search` lets you answer:

- did retrieval return the right evidence?
- did chat ignore good evidence?

Keep it protected in production, but don’t delete it.

Theory intuition:

- `/chat` is a composite pipeline (retrieve → pack → generate)
- `/search` isolates the retrieval component so you can attribute failures

---

## Example OpenAPI-driven workflow

* Define API endpoints and schema using OpenAPI spec
* Use OpenAPI-driven tools to generate client and server code
* Implement backend logic using the generated server code
* Use the generated client code to call APIs from the UI

---

## References

- OpenAPI spec: https://spec.openapis.org/oas/latest.html

---

## Self-check

- Can you test backend without the UI?
- Can you swap UI without changing backend?
