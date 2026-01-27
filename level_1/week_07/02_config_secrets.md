# Week 7 — Part 02: Config management + secrets (.env)

## Overview

Keep configuration out of code.

Never hardcode or commit API keys.

---

## Underlying theory: config is an input, secrets are a trust boundary

Treat configuration as a runtime input that can change across environments:

- dev vs demo vs CI
- different datasets
- different models

Secrets are special because they grant access. So the boundary is:

- code can be public (GitHub)
- secrets must stay private

Practical implication:

- if you commit an API key once, assume it is leaked and rotate it
- `.env` is a local convenience, not a secure secret manager (but it’s fine for Level 1)

---

## Minimal `.env` pattern

1. Create a `.env` file (do not commit it):

```env
OPENAI_API_KEY=...
```

2. Load it in Python:

```python
from dotenv import load_dotenv

load_dotenv()
```

3. Read via environment variables:

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY. Put it in .env or set env var.")
```

Common pitfalls:

- putting `.env` in git by accident (fix: ensure `.gitignore` includes it)
- mixing config and secrets in code defaults (fix: read from env, fail with a clear message)
- unclear error messages when secrets are missing (fix: say exactly which variable is required)

---

## References

- Twelve-Factor config: https://12factor.net/config
- python-dotenv: https://github.com/theskumar/python-dotenv
