# Week 2 — Part 00: AI Coding Tools Landscape

## Overview

Before you start using an IDE with AI, it helps to understand the tool landscape.

Week 1 introduced general AI tools. Week 2 narrows the focus to tools used for reading, modifying, and debugging code:

- IDEs and code editors
- AI extensions inside editors
- command-line AI coding tools
- workflow and project management helpers

This section is a tool map. You do not need to install every tool listed here.

---

## What Is an IDE?

An **IDE** is an Integrated Development Environment: an application where you can open project files, edit code, run commands, and inspect errors.

For beginners, the most important IDE features are:

| Feature | Why it matters |
|---|---|
| File explorer | See project files and folders |
| Editor | Read and modify code |
| Terminal | Run commands without switching apps |
| Extensions | Add tools such as Python support or AI assistants |
| Search | Find files, functions, and error text |

In this course, you can use **Cursor** or **VS Code**.

---

## VS Code and the Extension Ecosystem

**VS Code** is a popular code editor because it is lightweight, customizable, and has a large extension marketplace.

Common extension categories:

| Extension type | Example use |
|---|---|
| Language support | Python syntax highlighting, linting, formatting |
| Notebook support | Open and run Jupyter notebooks |
| Git tools | View changes and commit history |
| AI assistants | Ask questions, generate edits, explain code |
| Themes and usability | Make the editor easier to read |

For this course, do not optimize extensions too early. Start with the minimum needed to open files, ask AI questions, and run simple Python examples.

---

## AI Extensions for Your IDE

AI extensions bring chat, inline editing, and code suggestions into your editor.

| Tool | Interface | Beginner use case |
|---|---|---|
| Cursor | AI-first editor | Read files, ask questions, apply small edits |
| GitHub Copilot Chat | VS Code extension | Explain code and suggest changes |
| Cline | Autonomous coding agent extension | Plan and apply multi-step project changes |
| Kilo Code | Speed-focused AI coding assistant | AI-assisted edits and project navigation |

Use these tools with the same workflow you practice in Week 2:

```text
Ask -> Review -> Apply -> Verify
```

The tool can suggest changes, but you are responsible for checking what changed and whether it works.

---

## Command-Line AI Coding Tools

Some AI coding tools run in the terminal instead of a visual editor.

| Tool | What it is | When it helps |
|---|---|---|
| Claude Code | Command-line coding assistant from Anthropic | Terminal-based project exploration and edits |
| OpenAI Codex CLI | Command-line coding assistant from OpenAI | Agent-style coding tasks in a local repo |
| Kilo | Open-source coding assistant | Terminal workflow, Git-aware changes, automation |

CLI tools are powerful, but they can feel less friendly for beginners because you need to be comfortable with terminal commands, file paths, and Git status.

For Week 2, treat CLI tools as optional awareness unless your instructor specifically uses them in class.

---

## Workflow and Project Management Tools

Some tools focus less on writing code and more on organizing work.

Examples:

- Cline Kanban or task boards for breaking work into steps
- issue trackers for recording bugs and tasks
- Git history for reviewing what changed
- prompt notes for recording useful AI interactions

These tools matter because AI-assisted work still needs structure. A useful beginner habit is to write down:

- what you asked AI to do
- what it changed or explained
- what you verified yourself
- what still needs review

---

## Choosing the Right Tool

Use the simplest tool that matches the task.

| Your task | Good starting tool |
|---|---|
| Ask a general question | ChatGPT or Claude |
| Explain a file in this course | Cursor |
| Make a small code edit | Cursor inline edit or Copilot Chat |
| Debug an error message | Cursor chat, ChatGPT, or Claude |
| Explore Git history | Kilo or another CLI coding tool |
| Manage a multi-step coding task | Cline, Kilo, or a task board |

For most Week 2 students, the recommended path is:

```text
Cursor or VS Code -> open code_templates -> ask AI to explain -> make small edits -> verify
```

---

## Self-check

- Can you explain the difference between a browser AI tool and an IDE AI tool?
- Can you name one reason VS Code became popular?
- Can you explain what an extension does?
- Can you explain why CLI coding tools may be more advanced for beginners?
- Can you choose a tool for reading, modifying, and debugging code?

---

## Source Note

This lesson is based on the local outline file `ai_coding_tools_outline.csv`.
