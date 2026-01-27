# Week 8 — Part 03: Demo packaging checklist (one-command run)

## Overview

A demo is successful when another person can reproduce it.

---

## Underlying theory: reproducibility is an interface

You can treat “running your system” as a function of configuration:

$$
\text{behavior} = f(\text{code}, \text{data}, \text{config})
$$

If `config` is implicit (hidden local env vars, manual steps), then $f$ is not repeatable.

Practical implication:

- your README is part of the product interface
- one-command run is a reliability feature, not just convenience

---

## Checklist

- README has:
  - setup
  - config
  - run
  - expected outputs

- One command starts the service.

- One test request proves it works.

---

## Example: one-command run

Your README can include something like:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

And a test call:

```bash
curl -s http://localhost:8000/health
```

If you require an API key for admin endpoints, include it as an env var:

```bash
export ADMIN_API_KEY="..."
```

Don’t commit secrets. Use `.env` locally.

Common pitfall:

- mixing dev and prod configs and then not knowing which one the demo used

---

## References

- Twelve-Factor config: https://12factor.net/config

---

## Self-check

- Can a teammate run without asking you questions?
