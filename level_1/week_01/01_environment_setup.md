# Week 1 — Part 01: Environment setup + dependency management

## Overview

Your first engineering win is making your project runnable **from a clean state**.

That means:

- You can create an isolated environment.
- You can install dependencies consistently.
- You can run your script with one command.

---

## Underlying theory: reproducibility is an interface

Treat “running your project” like a function:

$$
\text{result} = f(\text{code}, \text{data}, \text{config}, \text{dependencies})
$$

If any input is implicit (unrecorded packages, hidden OS assumptions, manual clicks), then $f$ is not repeatable.

Practical implication:

- your `requirements.txt` (or `pyproject.toml`) is part of your project’s public interface
- the goal is not “it runs once” but “it runs again tomorrow, and on someone else’s machine”

---

## Mental model: why environments exist

A Python project depends on libraries (e.g., `pandas`). Different projects often require different versions.

A **virtual environment** isolates dependencies per project so:

- Project A can use `pandas==x`.
- Project B can use `pandas==y`.
- You avoid “it works on my machine” surprises.

You can view dependency management as keeping a consistent *snapshot* of a dependency graph:

- your code imports packages
- those packages import other packages
- package versions change over time

If you do not record versions, re-installing later may silently pull different packages and change behavior.

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
python -m pip install pandas
```

Using `python -m pip` reduces confusion when your system has multiple Python interpreters installed.

### 5) Save your dependency list

```bash
pip freeze > requirements.txt
```

This turns your environment setup into something repeatable.

Note: `pip freeze` captures the *full resolved set* of installed packages. This is good for reproducing a working environment, but it can be noisy. In later levels you may learn about tools that separate:

- “direct” dependencies you chose
- “transitive” dependencies pulled in automatically

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

- **`requirements.txt` exists, but results still differ across machines**
  - Explanation: OS differences (Windows vs Linux), CPU architecture, and binary wheels can change what gets installed.
  - Fix: record OS + Python version in your README; if needed later, learn Docker to fully standardize runtime.

- **You forgot to record dependencies**
  - Fix: run `pip freeze > requirements.txt` after installs.

---

## Self-check

- Can you recreate your environment from scratch using only `requirements.txt`?
- Can you explain *why* environments prevent dependency conflicts?
- If you delete `.venv`, can you recreate it and still run the project with the same commands?

---

## References

- Python `venv`: https://docs.python.org/3/library/venv.html
- Python packaging: https://packaging.python.org/
- pip user guide: https://pip.pypa.io/en/stable/user_guide/
