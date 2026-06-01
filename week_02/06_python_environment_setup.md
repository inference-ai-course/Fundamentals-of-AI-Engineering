# Week 2 — Part 06: Python Environment Setup

## Overview

Week 2 is where you prepare the Python environment you will use in Week 3. Do not install course packages into system Python. Use a virtual environment so your project is reproducible and does not conflict with other projects.

By the end of this part, you should be able to:

- create a `.venv`
- activate it
- confirm `python` and `pip` point to the environment
- install packages from `requirements.txt`
- verify `pandas` imports successfully

## Why This Moved To Week 2

Week 3 uses pandas for CSV profiling. If you wait until Week 3 to discover that pandas is missing, data work stops immediately. Week 2 now includes the setup step so Week 3 can focus on data.

## Step 1: Open A Terminal In `week_02`

```bash
cd week_02
```

Ask an AI tool if you are unsure what the command means:

```text
Explain what `cd week_02` does. I am new to terminal commands.
```

## Step 2: Create A Virtual Environment

```bash
python -m venv .venv
```

This creates an isolated Python environment inside the `.venv/` folder.

## Step 3: Activate The Environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

## Step 4: Verify Python And Pip

Run:

```bash
python --version
which python
pip --version
```

On Windows, use:

```bat
where python
```

Success means the path includes `.venv`.

If the path points to system Python, ask AI:

```text
I created a Python virtual environment but `which python` does not show `.venv`.
Here is my terminal output:
[paste output]

What should I check next?
```

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

The Week 2 requirements file is intentionally small. It installs pandas for Week 3 and ipykernel for notebook use.

## Step 6: Verify Pandas

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

If this prints a version number, your environment is ready for Week 3.

## Optional: Use The Environment In Jupyter

If you use notebooks, register the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name ai-eng-week2 --display-name "AI Engineering Week 2"
```

Then select **AI Engineering Week 2** as the notebook kernel.

## Required Evidence

Save the following in `environment_check.md`:

```text
python --version
which python
pip --version
python -c "import pandas as pd; print(pd.__version__)"
```

On Windows, replace `which python` with `where python`.

## Common Pitfalls

- Installing packages before activating `.venv`
- Running notebooks with the wrong kernel
- Pasting only the last error line instead of the full traceback
- Using system Python because it happens to work on one machine

## Self-Check

- Can you explain why system Python is not the course runtime?
- Can you activate `.venv` without copying a command from the instructor?
- Can you prove pandas is installed in the active environment?
