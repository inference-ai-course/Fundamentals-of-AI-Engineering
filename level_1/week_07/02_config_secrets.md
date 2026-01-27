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
    - Goal: keep secrets out of code while keeping local development convenient.
    - What to verify: `.env` is listed in `.gitignore` and does not show up in `git status`.
    - Common mistakes: forgetting to add `.env` to `.gitignore`, or accidentally committing it.

```env
OPENAI_API_KEY=...
```

2. Load it in Python:
    - Goal: load environment variables into the process before you read them.
    - What to verify: `load_dotenv()` is called near startup (before any API client initialization).
    - Common mistakes: loading `.env` too late, or not loading it at all.

```python
from dotenv import load_dotenv

load_dotenv()
```

3. Read via environment variables:
    - Goal: fail early with a clear error if a required secret is missing.
    - What to verify: the error message names the exact missing variable and tells the user how to set it.
    - Common mistakes: unclear error messages, or not checking for missing secrets at all.

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
