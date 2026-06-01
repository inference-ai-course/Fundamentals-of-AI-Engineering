# Week 2 PPT Outline: AI-Assisted Python Setup, Running Code, and Debugging

## Deck Purpose

This deck introduces beginner students to AI coding tools and then moves them into hands-on Python practice. The goal is not to make students expert programmers in Week 2. The goal is to help them fluently use AI tools to learn Python, set up an environment, run code, debug errors, make small changes, and verify results.

---

## Slide 1: Title

**Title:** Week 2 — AI-Assisted Python Setup, Running Code, and Debugging
**Subtitle:** From AI conversations to working Python examples

**Speaker note:** Week 1 focused on general AI tools. Week 2 uses those same tools as Python tutors and coding assistants.

---

## Slide 2: Learning Objectives

By the end of this week, students should be able to:

- Explain the basic landscape of AI coding tools.
- Set up Cursor or VS Code with AI integration.
- Use AI tools to learn Python concepts.
- Create and verify a Python virtual environment.
- Run simple Python scripts or notebooks.
- Open and navigate a project folder.
- Use AI to read and explain simple code.
- Make small code modifications with AI help.
- Debug common errors using AI assistance.
- Apply the Ask -> Review -> Apply -> Verify workflow.

---

## Slide 3: Week 2 Learning Path

```text
Tool landscape
-> IDE setup
-> AI tutor prompts
-> Python environment setup
-> Run code first
-> AI-assisted workflow
-> Code reading
-> Code modification
-> Debugging
```

**Key message:** Students first understand the tools, then use them to learn, run, and verify Python.

---

## Slide 4: Why Week 2 Starts With Tools

**Problem:** Beginners often see many tool names and do not know which ones matter.

Examples:

- VS Code
- Cursor
- GitHub Copilot Chat
- Cline
- Kilo Code
- Claude Code
- OpenAI Codex CLI

**Key message:** You do not need all of them. For Week 2, Cursor or VS Code is enough.

---

## Slide 5: What Is an IDE?

An **IDE** is an application where you can:

- Browse project files.
- Read and edit code.
- Run terminal commands.
- Install extensions.
- Use AI tools with project context.

**Beginner framing:** An IDE is your workspace for technical projects.

---

## Slide 6: Browser AI vs IDE AI

| Browser AI | IDE AI |
|---|---|
| Good for general questions | Good for project files |
| You paste context manually | AI can read files directly |
| Separate from your workspace | Built into your editor |
| Useful for concepts | Useful for reading and changing code |

**Key message:** IDE AI is powerful because it can work with your actual files.

---

## Slide 7: VS Code and Cursor

| Tool | What it is | Beginner use |
|---|---|---|
| VS Code | Popular code editor | Flexible, extension-based |
| Cursor | AI-first code editor | Easier AI chat and inline edits |

**Recommendation for this course:** Use Cursor if you want the simplest AI-first experience. Use VS Code if you already know it or your instructor requires it.

---

## Slide 8: The VS Code Extension Ecosystem

Extensions add capabilities to your editor.

Common extension types:

- Python support
- Jupyter notebook support
- Git tools
- AI assistants
- Themes and readability tools

**Beginner warning:** Do not install too many extensions early. Start with what the course requires.

---

## Slide 9: AI Extensions Inside the IDE

| Tool | Best for beginners |
|---|---|
| Cursor | Explaining files and applying small edits |
| GitHub Copilot Chat | Asking code questions in VS Code |
| Cline | More autonomous multi-step tasks |
| Kilo Code | Fast AI-assisted coding workflow |

**Key message:** More autonomy means more responsibility to review changes.

---

## Slide 10: Command-Line AI Coding Tools

Some tools run in the terminal instead of an editor UI.

Examples:

- Claude Code
- OpenAI Codex CLI
- Kilo

**When they help:**

- Project exploration from the terminal
- Git-aware changes
- Agent-style coding tasks
- Automation

**Beginner guidance:** Treat CLI tools as optional awareness unless used in class.

---

## Slide 11: Workflow and Project Management Tools

AI-assisted coding still needs structure.

Useful habits:

- Break work into small tasks.
- Keep notes on prompts.
- Track what AI changed.
- Verify every result.
- Use task boards only when the project becomes multi-step.

**Example tools:** Cline Kanban, issue trackers, Git history, prompt notes.

---

## Slide 12: Choosing the Right Tool

| Task | Good starting tool |
|---|---|
| Ask a general concept question | ChatGPT or Claude |
| Explain a file | Cursor or Copilot Chat |
| Make a small edit | Cursor inline edit |
| Debug an error | Cursor chat or ChatGPT |
| Review Git history | Kilo or another CLI tool |
| Manage a multi-step task | Cline, Kilo, or a task board |

**Key message:** Use the simplest tool that matches the task.

---

## Slide 13: Week 2 Recommended Tool Path

```text
Cursor or VS Code
-> create .venv and install requirements
-> run week_02/run_template_examples.py
-> open week_02/code_templates
-> ask AI to explain code
-> make small edits
-> run and inspect results
-> document what happened
```

**Key message:** Week 2 is guided practice, not a full programming project.

---

## Slide 14: IDE Setup Checklist

| Step | Action | Success looks like |
|---|---|---|
| 1 | Install Cursor or VS Code | Editor opens |
| 2 | Sign in or enable AI assistant | AI chat is available |
| 3 | Open `week_02/code_templates` | Files visible in sidebar |
| 4 | Open AI chat | Chat panel appears |
| 5 | Ask about files | AI can describe the folder |

---

## Slide 15: Cursor Interface Tour

Important areas:

- File explorer
- Editor
- AI chat
- Inline edit
- Terminal

Useful shortcuts:

| Action | Mac | Windows |
|---|---|---|
| AI chat | Cmd+L | Ctrl+L |
| Inline edit | Cmd+K | Ctrl+K |
| File explorer | Cmd+B | Ctrl+B |
| Terminal | Cmd+J | Ctrl+J |

---

## Slide 16: The Core Workflow

```text
Ask -> Review -> Apply -> Verify
```

| Step | Student responsibility |
|---|---|
| Ask | Give clear context |
| Review | Check if AI response makes sense |
| Apply | Use only the parts you understand |
| Verify | Test, inspect, or explain the result |

**Key message:** AI helps, but the student owns the final work.

---

## Slide 16A: From Week 1 Prompts To Python Prompts

Week 1 pattern:

```text
Explain [topic] for a beginner.
```

Week 2 coding version:

```text
Explain this Python function for a beginner.
Include inputs, output, one example, and one question to check my understanding.
```

**Key message:** Prompting is not a separate skill from coding. It is how beginners learn code safely.

---

## Slide 16B: Python Environment Check

Students run:

```bash
python --version
which python
pip --version
python -c "import pandas as pd; print(pd.__version__)"
```

**Success looks like:** Python and pip point to `.venv`, and pandas prints a version number.

---

## Slide 16C: Run Code Before Editing

Use:

```bash
python run_template_examples.py
```

Student task:

1. Run the command.
2. Copy the output.
3. Ask AI to explain one result.
4. Change one input value.
5. Rerun and verify the output changed.

---

## Slide 17: Good Prompts for Beginners

Use prompts that include context, goal, and format.

Examples:

```text
Explain this function step by step.
I am new to Python. Use simple language.
```

```text
List all functions in this file and explain what each one does.
Format the answer as a table.
```

```text
This error happened when I ran the code.
Explain what it means and suggest one small fix.
```

---

## Slide 18: Reading Code With AI

Recommended sequence:

```text
File overview
-> function list
-> one function in detail
-> unfamiliar terms
-> examples
```

Useful prompts:

- "What does this file do overall?"
- "Explain this function line by line."
- "What does `return` mean here?"
- "Give an example input and output."

---

## Slide 19: Reading Practice

Use `week_02/code_templates/simple_math.py`.

Student task:

1. Open the file.
2. Ask AI to list the functions.
3. Pick one function.
4. Ask for a simple explanation.
5. Write a two-sentence explanation in your own words.

**Checkpoint:** Students can explain at least one function without reading the AI response aloud.

---

## Slide 20: Modifying Code With AI

Modification workflow:

```text
Understand first
-> specify one small change
-> review the proposed edit
-> apply the edit
-> verify the behavior
```

Good beginner modifications:

- Add a comment.
- Improve a printed message.
- Add handling for empty input.
- Rename a variable for clarity.
- Add one simple example.

---

## Slide 21: Modification Practice

Use `week_02/code_templates/text_processing.py` or `data_processing.py`.

Student task:

1. Ask AI to explain one function.
2. Ask AI for one small improvement.
3. Review the suggested change.
4. Apply only if it makes sense.
5. Record what changed.

**Checkpoint:** Students can explain before/after behavior.

---

## Slide 22: Debugging With AI

Debugging prompt should include:

- Exact error message
- File name
- What you were trying to do
- Relevant code
- What you already tried

Template:

```text
I got this error:
[paste full error]

I was trying to:
[goal]

Please explain the likely cause and suggest one small fix.
```

---

## Slide 23: Debugging Practice

Use `week_02/code_templates/debugging_practice.py`.

Student task:

1. Run or inspect the file.
2. Capture one error or suspected bug.
3. Ask AI to explain the issue.
4. Apply one fix.
5. Verify the fix.
6. Write a debugging record.

**Checkpoint:** Students document error, prompt, fix, and verification.

---

## Slide 24: Common Beginner Pitfalls

| Pitfall | Better habit |
|---|---|
| Installing many tools at once | Start with Cursor or VS Code |
| Asking vague prompts | Include file, goal, and format |
| Accepting AI changes blindly | Review every change |
| Not testing | Verify after each edit |
| Hiding error messages | Paste the full error |
| Treating AI as always correct | Ask follow-up questions |

---

## Slide 25: Week 2 What to Complete

Students aim to finish:

- AI Python learning prompt log.
- Environment check output.
- Code run evidence from script or notebook cells.
- Code explanation notes for at least 5 functions or code blocks.
- 2-3 small code modifications.
- One debugging record.
- Representative prompts.
- A short reflection on what AI helped with and what they verified.

**Reminder:** Focus on understanding, verification, and documentation.

---

## Slide 26: Week 2 Self-Check

Students should be able to answer:

- Which tool am I using for Week 2 and why?
- Can I activate `.venv` and verify pandas?
- Can I run `python run_template_examples.py`?
- Can I open the `code_templates` folder?
- Can I ask AI to explain a file?
- Can I review and apply a small edit?
- Can I debug one error with AI help?
- Can I explain what I personally verified?

---

## Slide 27: Transition to Week 3

Week 2 builds the habits needed for Week 3:

| Week 2 habit | Week 3 use |
|---|---|
| Open project files | Work with scripts and data files |
| Activate `.venv` | Use pandas without relying on system Python |
| Run simple code | Run the data profiler |
| Ask AI to explain code | Understand pandas examples |
| Make small edits | Adapt data profiling scripts |
| Verify outputs | Check `profile.json` and `profile.md` |
| Document prompts | Record AI-assisted work |

**Closing message:** Week 3 begins technical data work, but the workflow stays the same.

---

## Source Materials

- `week_02/00_ai_coding_tools_landscape.md`
- `week_02/01_ide_setup.md`
- `week_02/02_ai_assisted_workflow.md`
- `week_02/03_reading_code_with_ai.md`
- `week_02/04_modifying_code_with_ai.md`
- `week_02/05_debugging_with_ai.md`
- `week_02/ai_coding_tools_outline.csv`
