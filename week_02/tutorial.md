# Week 2 Tutorials: AI-Assisted Python Setup, Running Code, and Debugging

## Overview

Week 2 transitions from browser-based AI tools to guided Python work with AI assistance. You'll use AI as a tutor while you set up a Python environment, run code, explain code, modify code, and debug errors.

You will practice:

- Understanding the AI coding tool landscape before choosing a setup
- Setting up VS Code or Cursor with AI integrations
- Reusing Week 1 prompt patterns to learn Python
- Creating a virtual environment and verifying pandas for Week 3
- Running simple Python scripts or notebooks
- Using AI to read and understand unfamiliar code
- Using AI to modify existing code
- Using AI to debug common errors

## Navigation

Required path:

- [01 — IDE Setup and AI Configuration](01_ide_setup.md)
- [AI Prompts for Learning Python](ai_python_learning_prompts.md)
- [06 — Python Environment Setup](06_python_environment_setup.md)
- [Run Template Examples](run_template_examples.py)
- [02 — AI-Assisted Programming Workflow](02_ai_assisted_workflow.md)
- [03 — Reading Code with AI Help](03_reading_code_with_ai.md)
- [04 — Modifying Code with AI Help](04_modifying_code_with_ai.md)
- [05 — Debugging Common Errors with AI](05_debugging_with_ai.md)
- [Debugging Exercise Scripts](debugging_exercises/README.md)
- [Sample Runtime Debugging Walkthrough](debugging_exercises/sample_runtime_debugging_walkthrough.md)

Optional support:

- [00 — AI Coding Tools Landscape](00_ai_coding_tools_landscape.md)
- [Notebook — Python With AI Basics](01_python_with_ai_basics.ipynb)
- [Notebook — Debugging With AI Lab](02_debugging_with_ai_lab.ipynb)
- [Mixed Debugging Challenge](code_templates/debugging_practice.py)

## Recommended order

1. Set up your IDE with AI integration.
2. Read the AI Python prompt guide and practice tutor-style prompting.
3. Complete the Python environment setup and verify pandas.
4. Run normal code first with `python run_template_examples.py`.
5. Use the Python basics notebook if you want extra practice with variables, lists, dictionaries, functions, imports, and errors.
6. Read 02 to understand the AI-assisted workflow.
7. Read 03 and practice explaining code with AI.
8. Read 04 and practice modifying code with AI.
9. Read 05 and the sample runtime walkthrough, then complete the remaining `debug_02_runtime.py` cases and `debug_03_logic.py`.
10. Optional: use the debugging notebook for extra practice, then try the mixed challenge.

Why this order works:

1. **IDE first**
    - Your IDE must be properly configured before you can practice.
    - What to verify: you can open Cursor, see AI chat panel, and send a prompt.

2. **AI tutor prompts second**
    - Week 1 prompt patterns now become coding prompts.
    - What to verify: you can ask AI to explain Python without accepting changes blindly.

3. **Environment third**
    - Week 3 data work requires pandas, so the environment must be ready now.
    - What to verify: `python -c "import pandas as pd; print(pd.__version__)"` works.

4. **Run code fourth**
    - Run normal code before debugging broken code.
    - What to verify: `python run_template_examples.py` prints function outputs.

5. **Workflow fifth**
    - Understand the pattern before practicing specific skills.
    - What to verify: you can explain the "ask → review → apply" pattern.

6. **Reading sixth**
    - Learn to understand code before modifying it.
    - What to verify: you can have AI explain at least 5 functions from templates.

7. **Modification seventh**
    - Now you can make changes with understanding.
    - What to verify: you can successfully complete 2-3 small modifications in copied files.

8. **Debugging eighth**
    - Errors are inevitable — learn to handle them.
    - Start only after the normal-code checkpoint succeeds.
    - What to verify: you can use AI to understand, fix, and document at least one error.

## Submission Structure

Create your own Week 2 practice folder with this structure:

```text
week_02_submission/
|-- README.md
|-- report.md
|-- prompts.md
|-- debugging_record.md
`-- modified_code/
    |-- simple_math.py
    |-- data_processing.py
    `-- debugging_practice_fixed.py
```

Copy files from `code_templates/` into `modified_code/` before editing. Keep the original template files unchanged so you can compare your work against the starting point.

Basic commands you should be able to run during the week:

```bash
python --version
python -B -m py_compile modified_code/simple_math.py
cd modified_code
python -c "from simple_math import add_numbers; print(add_numbers(2, 3))"
```

For debugging practice, `code_templates/debugging_practice.py` is intentionally broken. Copy it to `modified_code/debugging_practice_fixed.py`, fix one issue at a time, and record the error message, prompt, fix, and verification.
