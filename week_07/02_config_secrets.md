# Week 7 — Part 02: Config management + secrets (.env)

## Overview

Keep configuration out of code.

Never hardcode or commit API keys.

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on environments and safe project habits:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Python and Environment Management](../self_learn/Chapters/2/Chapter2.md)

Why it matters here (Week 7):

- Config should be reproducible (safe to commit); secrets must not be committed.
- Fail early with a clear error if a required env var is missing.

---

## Minimal `.env` pattern

### Step 1: Create `.env` file

```bash
# .env (DO NOT COMMIT)
OPENAI_API_KEY=sk-...
DEFAULT_MODEL=gpt-4o-mini
DEBUG=false
```

**Critical**: Add to `.gitignore`:
```bash
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to gitignore"
```

**Verify it's ignored:**
```bash
git status
# Should NOT show .env as untracked
```

### Step 2: Create `.env.example` template

```bash
# .env.example (SAFE TO COMMIT)
OPENAI_API_KEY=your_api_key_here
DEFAULT_MODEL=gpt-4o-mini
DEBUG=false
```

This helps teammates know what secrets they need.

### Step 3: Load in Python

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

# Load .env at startup
load_dotenv()

# Now environment variables are available
api_key = os.getenv("OPENAI_API_KEY")
```

### Step 4: Validate required secrets

```python
import os
from typing import List


def require_env_vars(var_names: List[str]) -> None:
    """
    Fail fast if required environment variables are missing.
    """
    missing = [name for name in var_names if not os.getenv(name)]
    
    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"\n"
            f"To fix:\n"
            f"1. Copy .env.example to .env\n"
            f"2. Fill in the missing values\n"
            f"3. Re-run\n"
        )


# At startup
require_env_vars(["OPENAI_API_KEY"])
```

---

## Configuration layers

### Layer 1: Hard-coded defaults

```python
DEFAULT_CONFIG = {
    "model": "gpt-4o-mini",
    "temperature": 0.0,
    "max_retries": 3,
    "timeout_s": 30.0,
}
```

### Layer 2: Environment variables

```python
import os

def get_config() -> dict:
    """
    Load config with environment variable overrides.
    """
    return {
        "model": os.getenv("MODEL", DEFAULT_CONFIG["model"]),
        "temperature": float(os.getenv("TEMPERATURE", DEFAULT_CONFIG["temperature"])),
        "max_retries": int(os.getenv("MAX_RETRIES", DEFAULT_CONFIG["max_retries"])),
        "timeout_s": float(os.getenv("TIMEOUT", DEFAULT_CONFIG["timeout_s"])),
    }
```

### Layer 3: CLI arguments (highest priority)

```python
import argparse
import os

def build_config(args) -> dict:
    """
    Merge: defaults < env vars < CLI args.
    """
    config = get_config()  # Loads defaults + env vars
    
    # CLI args override everything
    if args.model:
        config["model"] = args.model
    if args.temperature is not None:
        config["temperature"] = args.temperature
    
    return config
```

**Priority order:**
1. CLI argument (highest)
2. Environment variable
3. Default value (lowest)

---

## Secrets vs config

### Secrets (NEVER commit)
- API keys
- Database passwords
- Private keys
- Tokens

**Storage**: `.env` file (gitignored)

### Config (safe to commit)
- Model names
- Feature flags
- Timeout values
- Retry counts

**Storage**: `config.py` or `config.json` (committed)

---

## Configuration file approach

### config.json (committed, no secrets)

```json
{
  "model": "gpt-4o-mini",
  "temperature": 0.0,
  "max_retries": 3,
  "sample_size": 5,
  "output_formats": ["json", "markdown"]
}
```

### Load config + secrets

```python
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Load config from file
config_path = Path("config.json")
config = json.loads(config_path.read_text())

# Add secrets from environment
config["api_key"] = os.getenv("OPENAI_API_KEY")

if not config["api_key"]:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")
```

---

## Common pitfalls and fixes

### Pitfall 1: Committing secrets

**Symptom**: `.env` appears in git history

**Prevention**:
```bash
# BEFORE first commit
echo ".env" >> .gitignore
```

**Already committed? Remove from history:**
```bash
git rm --cached .env
git commit -m "Remove .env from git"
# Then add to .gitignore
```

### Pitfall 2: Loading .env too late

**Bad:**
```python
import os
api_key = os.getenv("KEY")  # ← .env not loaded yet!

from dotenv import load_dotenv
load_dotenv()  # ← Too late
```

**Good:**
```python
from dotenv import load_dotenv
load_dotenv()  # ← First thing

import os
api_key = os.getenv("KEY")  # ← Now it works
```

### Pitfall 3: No .env.example

**Problem**: Teammates don't know what secrets they need

**Fix**: Commit `.env.example` with placeholder values

### Pitfall 4: Hardcoded secrets

**Bad:**
```python
api_key = "sk-hardcoded123"  # ← NEVER DO THIS
```

**Good:**
```python
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY in .env")
```

---

## Security checklist

- [ ] `.env` is in `.gitignore`
- [ ] `.env.example` exists (with placeholder values)
- [ ] No secrets in code
- [ ] Required secrets validated at startup
- [ ] Error messages don't leak secret values
- [ ] `.env` has restrictive permissions: `chmod 600 .env`

---

## Practice notebook

For hands-on config and secrets exercises, see:
- **[02_config_secrets.ipynb](./02_config_secrets.ipynb)** - Interactive configuration patterns
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## References

- Twelve-Factor config: https://12factor.net/config
- python-dotenv: https://github.com/theskumar/python-dotenv
