# Week 1 — Part 01: Environment setup + dependency management

## Overview

Your first engineering win is making your project runnable **from a clean state**.

That means:

- You can create an isolated environment.
- You can install dependencies consistently.
- You can run your script with one command.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on environments or Jupyter:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 2: Conda environment management](../../level_0/Chapters/2/03_conda_environments.md)
- [Level 0 — Chapter 1: Conda environments and packages](../../level_0/Chapters/1/04_conda_environment_management.md)
- [Level 0 — Chapter 1: Jupyter](../../level_0/Chapters/1/05_jupyter_interactive_computing.md)

---

## Checklist (repo-specific)

1. Create or activate your project environment (venv/conda).
2. Verify you are using the intended Python:
   - `python --version`
   - `which python` (Linux/macOS)
3. Install the packages needed for Week 1 (at minimum `pandas`).
4. Record dependencies for reproducibility:
   - `pip freeze > requirements.txt`

---

## “Fresh machine” test (the real standard)

To prove your project is reproducible, recreate your environment from scratch using only your recorded dependency file.

Example (venv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -c "import pandas as pd; print(pd.__version__)"
```

If this works, your environment setup is repeatable.

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
