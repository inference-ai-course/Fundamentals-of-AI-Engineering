# Week 1 — Part 05: AI Tools Comparison

## Overview

Having explored ChatGPT, Claude, Cursor, and Kilo, this tutorial helps you decide which tool to use for different situations.

---

## Quick Reference Table

| Tool | Interface | File Access | Best Strength | Free Tier |
|------|-----------|-------------|---------------|-----------|
| **ChatGPT** | Browser | No | Versatility, speed | Yes |
| **Claude** | Browser | No | Long docs, reasoning | Yes |
| **Cursor** | GUI Editor | Yes | Code understanding and project navigation | Free/trial access varies |
| **Kilo** | Terminal | Yes | Git, automation | Yes |

---

## Decision Framework

### Question 1: Where is your content?

| Content Location | Recommended Tool |
|------------------|------------------|
| In your head (ideas, questions) | ChatGPT or Claude |
| In a file you want to understand | Cursor or Kilo |
| In a file you want to modify | Cursor or Kilo |
| In Git (commits, history) | Kilo |

### Question 2: What's your interface preference?

| Preference | Recommended Tool |
|------------|------------------|
| Browser (no installation) | ChatGPT or Claude |
| Visual editor (GUI) | Cursor |
| Terminal (CLI) | Kilo |

### Question 3: What type of task?

| Task Type | Best Tool(s) |
|-----------|--------------|
| Write text (email, article) | ChatGPT or Claude |
| Explain a concept | ChatGPT or Claude |
| Understand code files | Cursor |
| Modify existing code | Cursor or Kilo |
| Git operations | Kilo |
| Debug with file context | Cursor or Kilo |
| Brainstorm ideas | ChatGPT or Claude |
| Analyze long documents | Claude |

---

## Detailed Tool Profiles

### ChatGPT

**Strengths:**
- Versatile — handles most tasks well
- Fast responses
- Good at generating code snippets
- Large user community, many examples

**Weaknesses:**
- No file access (browser-based)
- Limited context per conversation
- Can't execute anything

**Use when:**
- Quick questions and answers
- Generating text or code snippets
- Learning new concepts
- Brainstorming ideas

---

### Claude

**Strengths:**
- Handles longer documents better
- More detailed explanations
- Nuanced reasoning
- Often more thoughtful analysis

**Weaknesses:**
- Slightly slower than ChatGPT
- No file access (browser-based)
- Smaller user community

**Use when:**
- Analyzing long documents
- Complex reasoning tasks
- When you want detailed step-by-step explanations
- Getting honest assessments

---

### Cursor

**Strengths:**
- Reads your files automatically
- Visual file explorer
- Inline editing (Cmd+K)
- Project-wide context

**Weaknesses:**
- Requires installation
- Access limits may change
- More setup than browser-based tools

**Use when:**
- Exploring project files visually
- Understanding code in context
- Making code modifications
- Visual workflow preference

---

### Kilo

**Strengths:**
- Strong Git integration
- Terminal workflow
- Scriptable and automatable
- Open-source

**Weaknesses:**
- CLI interface (no GUI)
- Requires terminal familiarity
- Less intuitive for beginners

**Use when:**
- Terminal workflow preference
- Git-heavy operations
- Automating repetitive tasks
- Integrating into scripts

---

## Task-Based Selection Guide

### Writing Tasks

| Task | Tool | Why |
|------|------|-----|
| Email drafting | ChatGPT/Claude | Quick, good text generation |
| Article writing | Claude | Better for longer content |
| Documentation | Cursor | If docs are in project files |

### Analysis Tasks

| Task | Tool | Why |
|------|------|-----|
| Concept explanation | ChatGPT/Claude | Fast, clear explanations |
| Code explanation | Cursor | Has file context |
| Document analysis | Claude | Handles long docs |
| Error analysis | Cursor/Kilo | Can see error logs/files |

### Creation Tasks

| Task | Tool | Why |
|------|------|-----|
| Generate code snippet | ChatGPT | Fast, no context needed |
| Create new file | Cursor/Kilo | Can write to files |
| Design structure | ChatGPT/Claude | Brainstorming first |

### Modification Tasks

| Task | Tool | Why |
|------|------|-----|
| Edit code | Cursor/Kilo | File access, direct edit |
| Refactor code | Cursor/Kilo | Project context |
| Add comments | Cursor | Inline editing |

---

## Combining Tools

### Workflow example: New feature

1. **Brainstorm** with ChatGPT: "How should I implement feature X?"
2. **Plan** with Claude: "Review this plan, identify potential issues"
3. **Explore** with Cursor: "Explain which files would matter"
4. **Implement later** with Cursor/Kilo after you understand the plan

### Workflow example: Debugging

1. **Understand error** with ChatGPT: "What does this error mean?"
2. **Locate problem** with Cursor: "Find where this error might occur"
3. **Ask for options** with Cursor: "Suggest possible fixes"
4. **Verify** with a command or instructor-provided test before accepting changes

---

## Creating Your Personal Guide

### Exercise: Build a decision tree

Answer these questions for yourself:

1. **For quick questions:** I'll use ______ because ______
2. **For code understanding:** I'll use ______ because ______
3. **For code modification:** I'll use ______ because ______
4. **For Git operations:** I'll use ______ because ______
5. **For long documents:** I'll use ______ because ______

Write these down. Keep them as your reference.

---

## Week 1 Summary

### What you learned

1. **What AI agents are**: Tools that understand natural language
2. **The landscape**: ChatGPT, Claude, Cursor, Kilo — different tools for different tasks
3. **Core concepts**: Prompts, context, capabilities, limitations
4. **How to choose**: Match tool to task, interface preference, and content location

### Your toolkit

| Tool | You should be able to |
|------|----------------------|
| ChatGPT | Send prompts, iterate on responses, generate text |
| Claude | Send prompts, analyze longer content |
| Cursor | Open folder, ask about files, request modifications |
| Kilo | Send commands, ask about files, explore Git |

### What's next

**Week 2**: We'll dive deeper into AI-assisted programming:
- Setting up IDE environment
- Reading code with AI
- Modifying code with AI
- Debugging with AI

---

## Final Self-check

- Can you name all 4 tools and their primary strengths?
- Can you decide which tool to use for a given task?
- Have you completed hands-on tasks with each tool?
- Do you have accounts/access for all tools?
- Can you explain why prompt quality matters?

---

## What to Complete

By the end of Week 1, aim to finish:

- `report.md`: Agent Tool Usage Reflection Report (800-1000 words)
- `prompts.md`: Representative prompts and notes
- `output/`: Screenshots, copied outputs, or interaction notes
- `README.md`: Brief overview of your submission

Your 3 task examples should include at least two AI tools and at least one file/project or command-line observation.

---

## References

- ChatGPT: https://chatgpt.com
- Claude: https://claude.ai
- Cursor: https://cursor.sh
- Prompt Engineering Guide: https://www.promptingguide.ai
