# Week 7 — Part 02: Config management + secrets (.env)

## Overview

Keep configuration out of code.

Never hardcode or commit API keys.

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

---

## References

- Twelve-Factor config: https://12factor.net/config
- python-dotenv: https://github.com/theskumar/python-dotenv
