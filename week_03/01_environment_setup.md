# Week 3 - Part 01: Environment Preflight

## Overview

This short notebook checks that your Week 3 work is running in the intended Python environment. Environment setup itself is taught in [Week 2 Python Environment Setup](../week_02/06_python_environment_setup.md). Here, the focus is verification.

A Python environment is an isolated place where Python and installed packages live. Isolation matters because different projects often need different package versions. If you install packages into the wrong environment, your notebook may work today but fail when a teammate tries to reproduce it.

## Learning Objectives

By the end of this preflight, you should be able to:

- Identify which Python interpreter is active.
- Check which `pip` is connected to that interpreter.
- Explain why Jupyter kernels must match the project environment.
- Verify that pandas is installed before starting the data profiling lesson.
- Record enough dependency information to make the setup reproducible.

## Exercise 1: Verify Python and pip

Run these commands in a terminal or notebook cell:

```bash
python --version
which python
python -m pip --version
```

On Windows, use `where python` instead of `which python`.

The key idea is simple: `python` and `pip` must point to the same project environment. Prefer `python -m pip ...` because it runs pip through the active Python interpreter.

## Exercise 2: Verify the Jupyter kernel

Inside a notebook, run:

```python
import sys
print(sys.executable)
```

The path should match the environment you activated. If it does not, select the correct kernel in Jupyter or VS Code before continuing.

A Jupyter kernel is a separate Python process that executes notebook cells. The notebook UI can be open in one place while code runs in a different Python environment. That is why kernel verification is part of the lesson.

## Exercise 3: Check required packages

Week 3 requires pandas:

```python
import pandas as pd
print(pd.__version__)
```

If this import fails, activate the Week 2 environment and install dependencies before continuing.

## Exercise 4: Record dependencies

A reproducible project should tell another person how to rebuild the environment:

```bash
python -m pip freeze > requirements.txt
```

`requirements.txt` records installed package versions. It is not perfect for every production workflow, but it is enough for this course milestone.

## Self-check

- Can you show which Python executable is running notebook cells?
- Can you explain why `python -m pip` is safer than plain `pip`?
- Can you import pandas before starting the profiling notebook?
- Can another person recreate the package setup from your dependency file?

## References

- Week 2 Python Environment Setup: ../week_02/06_python_environment_setup.md
- Python `venv`: https://docs.python.org/3/library/venv.html
- Python packaging guide: https://packaging.python.org/
- pip user guide: https://pip.pypa.io/en/stable/user_guide/
- Conda environment management: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
