# Week 1 — Part 01: Environment setup + dependency management

## Overview

Your first engineering win is making your project runnable **from a clean state**.

That means:

- You can create an isolated environment.
- You can install dependencies consistently.
- You can run your script with one command.

---

## Pre-study (Self-learn)

Foundamental Course assumes you do a lot self-study. Refer to self-study materials for refresher on environments or Jupyter:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Conda environment management](../../self_learn/Chapters/2/03_conda_environments.md)
- [Self-learn — Chapter 1: Conda environments and packages](../../self_learn/Chapters/1/04_conda_environment_management.md)
- [Self-learn — Chapter 1: Jupyter](../../self_learn/Chapters/1/05_jupyter_interactive_computing.md)

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

## Why environments matter (concrete example)

Without isolated environments, you get version conflicts:

**Scenario**: 
- Project A needs `pandas==1.5.0`
- Project B needs `pandas==2.0.0`
- Both install to system Python

**Result**: whichever installs last "wins", breaking the other project.

**With environments**:
- Project A has `.venv_a/` with `pandas==1.5.0`
- Project B has `.venv_b/` with `pandas==2.0.0`
- Both work independently

This is why production systems use containers (Docker) or virtual environments.

---

## "Fresh machine" test (the real standard)

To prove your project is reproducible, recreate your environment from scratch using only your recorded dependency file.

Example (venv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -c "import pandas as pd; print(pd.__version__)"
```

If this works, your environment setup is repeatable.

### Alternative: conda approach

```bash
conda create -n myproject python=3.11 -y
conda activate myproject
pip install -r requirements.txt
```

Why some teams prefer conda:
- Can manage non-Python dependencies (e.g., system libraries)
- Better handling of scientific/numerical packages
- Cross-platform consistency

---

## Common pitfalls and troubleshooting

### Pitfall 1: Installing packages outside the environment

**Symptom**: "It works on my machine" but fails elsewhere.

**Diagnosis**:
```bash
which python
# Should show: /path/to/your/.venv/bin/python
# NOT: /usr/bin/python or /usr/local/bin/python
```

**Fix**: Always activate your environment before `pip install`.

---

### Pitfall 2: Forgetting to record dependencies

**Symptom**: You can't recreate the environment because you installed packages ad-hoc.

**Fix**: Record immediately after installing:
```bash
pip install pandas scikit-learn
pip freeze > requirements.txt
```

Better: use a "known good" requirements file and only add intentionally.

---

### Pitfall 3: Version drift

**Symptom**: "It worked last week" but now fails.

**Cause**: `pip install pandas` without pinning fetches the newest version, which may have breaking changes.

**Fix**: Pin versions in `requirements.txt`:
```txt
pandas==2.2.3
scikit-learn==1.5.2
```

Not:
```txt
pandas
scikit-learn
```

---

### Pitfall 4: Platform-specific dependencies

**Symptom**: `requirements.txt` works on Linux but fails on Windows (or vice versa).

**Cause**: Some packages compile differently per OS.

**Mitigation**:
- Use `requirements.txt` for pip-installable packages only
- Document system dependencies separately (e.g., in README)
- Consider Docker if cross-platform consistency is critical

---

## Verification checklist

Run these commands in sequence to verify your setup:

```bash
# 1. Deactivate any active environment
deactivate  # or `conda deactivate`

# 2. Delete your environment
rm -rf .venv

# 3. Recreate from scratch
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Verify imports work
python -c "import pandas; import numpy; print('OK')"

# 6. Run your script
python your_script.py
```

If all steps succeed, your environment is reproducible.

---

## Self-check

- Can you recreate your environment from scratch using only `requirements.txt`?
- Can you explain *why* environments prevent dependency conflicts?
- If you delete `.venv`, can you recreate it and still run the project with the same commands?
- What happens if you run `pip install` outside your environment?

---

## References

- Python `venv`: https://docs.python.org/3/library/venv.html
- Python packaging: https://packaging.python.org/
- pip user guide: https://pip.pypa.io/en/stable/user_guide/
- Conda environments: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
