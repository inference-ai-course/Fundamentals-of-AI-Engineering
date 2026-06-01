# Week 1 — Part 03: Cursor Editor Introduction

## Overview

**Cursor** is a code editor with built-in AI. Unlike ChatGPT (browser-based), Cursor runs locally and can read your files.

This means AI understands your project context, not just your prompt.

---

## Why Cursor Matters

### Browser-based AI vs Editor-based AI

| ChatGPT/Claude | Cursor |
|----------------|--------|
| Runs in browser | Runs on your machine |
| No file access | Reads your files |
| Manual context provision | Automatic project context |
| Good for text tasks | Good for code tasks |

### The key advantage: Context awareness

When you ask Cursor a question, it can:
- See your file structure
- Read file contents
- Understand project relationships
- Make context-aware suggestions

**Example:**

In ChatGPT: "Explain this code: [paste code]"

In Cursor: "Explain this file" (Cursor reads it automatically)

---

## Setup Checklist

| Step | Action | Success looks like |
|------|--------|-------------------|
| 1. Download | Go to cursor.sh, download for your OS | Installer downloaded |
| 2. Install | Run installer | Cursor opens |
| 3. Explore | Open this course folder | Files visible in sidebar |
| 4. Chat | Press Cmd+L (Mac) or Ctrl+L (Windows) | AI chat panel opens |

### Installation

**Download:** [cursor.sh](https://cursor.sh)

**Platforms:** macOS, Windows, Linux

---

## Interface Overview

### Key elements

| Element | Shortcut | Purpose |
|---------|----------|---------|
| **File explorer** | Cmd+B / Ctrl+B | Navigate project files |
| **AI Chat** | Cmd+L / Ctrl+L | Chat with AI about your project |
| **AI Inline** | Cmd+K / Ctrl+K | AI edits at cursor position |
| **Terminal** | Cmd+J / Ctrl+J | Run commands |
| **Command palette** | Cmd+Shift+P | Search all commands |

### Two AI modes

1. **Chat mode** (Cmd+L): Conversation with AI about your project
2. **Inline mode** (Cmd+K): AI edits code directly where your cursor is

---

## Your First Cursor Tasks

### Task 1: Open the course folder

1. Open Cursor
2. File → Open Folder
3. Choose the `Fundamentals-of-AI-Engineering` course folder
4. Files appear in the sidebar

### Task 2: Ask about the folder

Press Cmd+L (Mac) or Ctrl+L (Windows) to open AI chat.

Try:
```text
What files and folders are in this directory? 
Can you summarize what this folder contains?
```

Cursor can see your file structure and will describe it.

### Task 3: Ask about a file

1. Click `README.md`, `SYLLABUS.md`, or `week_01/tutorial.md` in the sidebar
2. In the AI chat:
```text
Can you explain what this file does? 
Summarize its contents.
```

Cursor reads the file and explains it.

### Task 4: Run a read-only command

Open the terminal in Cursor with Cmd+J (Mac) or Ctrl+J (Windows/Linux), then run:

```bash
pwd
ls
python --version
```

Record what each command shows. These commands only display information.

---

## Core Features

### Feature 1: Project understanding

Cursor indexes your project. It knows:
- File names and structure
- File contents
- Relationships between files

**Prompt example:**
```text
What is the overall purpose of this project?
Which files are most important?
```

### Feature 2: Code explanation

Even if you don't know programming, Cursor can explain code.

**Prompt example:**
```text
Walk me through this file step by step. 
Explain what each section does in simple terms.
```

### Feature 3: Code modification (Week 2+ or scratch files)

Request changes, Cursor generates them.

**Prompt example:**
```text
Add a function that prints "Hello World".
Put it at the end of the file.
```

Use this only in a scratch file during Week 1.

### Feature 4: Inline editing (Cmd+K, Week 2+ or scratch files)

Select code, press Cmd+K, describe your change:

```text
Add error handling to this function.
```

Cursor edits directly in your file.

---

## Practical Examples (Non-Programmer Perspective)

### Example 1: Understanding a README

Open this course `README.md` file:

```text
Summarize what this project does.
What are the main features?
```

### Example 2: Understanding configuration

Open `requirements.txt` or another simple project file:

```text
Explain what each setting in this file controls.
Which ones are most important?
```

### Example 3: Understanding structure

```text
Draw a simple diagram showing how files in this 
folder relate to each other.
```

---

## Common Pitfalls

### Pitfall 1: Not specifying which file

**Symptom**: AI doesn't know what you're asking about.

**Fix**: Either:
- Click the file first (Cursor uses active file)
- Or specify in prompt: "In the file `config.json`, explain..."

### Pitfall 2: Expecting execution

**Symptom**: You ask AI to "run this code".

**Reality**: Cursor can generate and modify code, but doesn't execute it.

**Fix**: Use the terminal (Cmd+J) to run code yourself.

### Pitfall 3: Too abstract questions

**Symptom**: "What should I do?" gives vague answers.

**Fix**: Be specific:
- "Explain the Week 1 section in `README.md`"
- "Summarize `week_01/tutorial.md` in five bullets"

### Pitfall 4: Not reviewing changes

**Symptom**: Accepting all AI edits without checking.

**Fix**: Always review generated code. Ask AI to explain changes.

---

## Cursor vs ChatGPT for Code Tasks

| Task | Better Tool |
|------|-------------|
| Generate a function from scratch | Either works |
| Understand existing code | Cursor (has file context) |
| Modify code in a project | Cursor (can edit directly) |
| Debug with error context | Cursor (can see error logs) |
| General programming questions | ChatGPT (often faster) |

---

## Hands-on Exercises

### Exercise 1: Folder exploration (10 minutes)

1. Open Cursor
2. Open the `Fundamentals-of-AI-Engineering` course folder
3. Ask AI: "What's in this folder?"
4. Ask: "Which files would be most interesting to read?"

### Exercise 2: File explanation (10 minutes)

1. Open `README.md` or `week_01/tutorial.md`
2. Ask AI: "Summarize this file"
3. Ask: "What are the key points?"

### Exercise 3: Optional scratch-file modification (15 minutes)

Only do this in a scratch file, not in the main course materials.

1. Create a new folder named `week_01/scratch/`
2. Create a new file: `week_01/scratch/notes.md`
3. Write: "My learning notes"
4. Ask AI: "Add a section about what I learned today"
5. Review the changes before saving

---

## Tips for Success

1. **Click the file first**: Cursor uses your active file for context
2. **Be specific**: "Explain the first 20 lines" vs "explain the file"
3. **Use Cmd+K for edits**: Inline editing is often faster than chat
4. **Review changes**: Always check what AI modified
5. **Save frequently**: Save before asking for modifications

---

## Access and Limits

- **Free or trial access**: Usually enough for Week 1 exploration
- **Usage limits**: May change over time
- **Paid access**: Often provides higher limits or newer features

**For this course**: Use any available free, trial, or instructor-provided access.

---

## Self-check

- Have you installed Cursor?
- Can you open a folder and see files?
- Can you open the AI chat (Cmd+L)?
- Can you ask AI about a file's contents?
- Can you run `pwd`, `ls`, or `python --version` in the terminal?
- If you modified a file, did you use a scratch file and review the change?

---

## References

- Cursor: https://cursor.sh
- Cursor Docs: https://cursor.sh/docs
- Cursor YouTube: https://www.youtube.com/@cursorofficial
