# Week 1 — Part 01: Environment setup + dependency management

## Overview

Your first engineering win is making your project runnable **from a clean state**.

That means:

- You can create an isolated environment.
- You can install dependencies consistently.
- You can run your script with one command.

---

## Mental model: why environments exist

A Python project depends on libraries (e.g., `pandas`). Different projects often require different versions.

A **virtual environment** isolates dependencies per project so:

- Project A can use `pandas==x`.
- Project B can use `pandas==y`.
- You avoid “it works on my machine” surprises.

---

## Option A (recommended): `venv`

### 1) Create an environment

From your project folder:

```bash
python -m venv .venv
```

### 2) Activate it

```bash
source .venv/bin/activate
```

You should now see `(.venv)` in your terminal prompt.

### 3) Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4) Install packages

For this week:

```bash
pip install pandas
```

### 5) Save your dependency list

```bash
pip freeze > requirements.txt
```

This turns your environment setup into something repeatable.

---

## Option B: Conda (acceptable)

If you already use conda:

```bash
conda create -n level1-week1 python=3.11
conda activate level1-week1
pip install pandas
pip freeze > requirements.txt
```

---

## “Fresh machine” test (the real standard)

To prove your project is reproducible:

- Copy the project to a new folder (or delete `.venv` and recreate it).
- Re-run setup using `requirements.txt`.

Example:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -c "import pandas as pd; print(pd.__version__)"
```

If this works, you’ve done real engineering.

---

## Common failures and fixes

- **`pip install` installed into system Python**
  - Fix: activate your environment first and re-run install.

- **`python` points to a different interpreter than expected**
  - Fix: run `which python` (Linux/macOS) and confirm it points inside `.venv`.

- **You forgot to record dependencies**
  - Fix: run `pip freeze > requirements.txt` after installs.

---

## Self-check

- Can you recreate your environment from scratch using only `requirements.txt`?
- Can you explain *why* environments prevent dependency conflicts?

---

## References

- Python `venv`: https://docs.python.org/3/library/venv.html
- Python packaging: https://packaging.python.org/
- pip user guide: https://pip.pypa.io/en/stable/user_guide/
