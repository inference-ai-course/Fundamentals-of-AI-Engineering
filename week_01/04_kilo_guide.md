# Week 1 — Part 04: Kilo Guide

## Overview

**Kilo** is an AI coding assistant that runs in your terminal. Unlike Cursor (GUI), Kilo is CLI-based — you interact through text commands.

In Week 1, use Kilo mainly for read-only project exploration. File edits and commits are instructor demos or Week 2+ practice.

---

## What is Kilo?

### Kilo vs other tools

| Aspect | ChatGPT | Cursor | Kilo |
|--------|---------|--------|------|
| Interface | Browser | GUI Editor | Terminal (CLI) |
| File access | No | Yes | Yes |
| Git awareness | No | Partial | Strong |
| Automation | No | Manual | Scriptable |

### Why learn Kilo?

1. **Terminal workflow**: Many developers prefer CLI over GUI
2. **Git integration**: Kilo understands your Git history
3. **Automation**: Can be scripted and integrated into workflows
4. **Local execution**: Can work with your local files and tools when configured

---

## How Kilo Works

### The interaction model

```text
You → Type command in terminal → Kilo processes → Kilo responds/acts → You see result
```

### Key capabilities

| Capability | Example |
|------------|---------|
| **Read files** | Understand project structure |
| **Write files** | Generate and modify code after confirmation |
| **Git operations** | Inspect status/history; commits should wait until you understand the change |
| **Search** | Find patterns across project |
| **Execute** | Run commands, scripts |

---

## Using Kilo (Basic Patterns)

### Pattern 1: Ask questions

Simply type your question in the terminal where Kilo is running:

```text
What files are in this directory?
```

```text
Explain what the file README.md contains.
```

### Pattern 2: Ask read-only file questions

```text
List the Week 1 tutorial files.
```

```text
Summarize week_01/tutorial.md in beginner-friendly language.
```

### Pattern 3: Git status and history

```text
Show the current git status.
```

```text
Show me the recent commit history.
```

```text
What changed in the last commit?
```

### Pattern 4: Search and analyze

```text
Find files that mention Cursor.
```

```text
Search for the phrase "AI Tool Declaration".
```

---

## Kilo's Strengths

### 1. Git awareness

Kilo can:
- See your Git history
- Understand diffs
- Create commits
- Analyze changes

**Example:**
```text
Explain what changed between the last two commits.
```

### 2. Project context

Like Cursor, Kilo reads your files. It understands:
- File structure
- Code relationships
- Project architecture

### 3. Autonomous execution

Kilo can perform actions after you understand and approve them:
- Edit files directly
- Run terminal commands
- Create commits

**Instructor demo or Week 2+ example:**

```text
Create a commit with message "Add utility functions" 
for the changes in utils.py.
```

---

## When to Use Kilo vs Other Tools

### Decision guide

| Your Situation | Recommended Tool |
|----------------|------------------|
| Quick question, no file context | ChatGPT |
| Visual file exploration | Cursor |
| Terminal workflow, prefer CLI | Kilo |
| Git-focused operations | Kilo |
| Automated/scripted operations | Kilo |

### Combining tools

You can use multiple tools together:

1. **ChatGPT**: Quick concepts and explanations
2. **Cursor**: Visual code browsing and editing
3. **Kilo**: Git operations and terminal workflows

---

## Common Kilo Commands

| Command Type | Example |
|--------------|---------|
| **Information** | "List the files in week_01" |
| **Explanation** | "Explain what README.md says about the course" |
| **Creation** | "Create a README.md file" (Week 2+ or scratch work) |
| **Modification** | "Add type hints to utils.py" (Week 2+ or scratch work) |
| **Git** | "Show current git status" |
| **Search** | "Find files that mention Cursor" |

---

## Practical Exercises

### Exercise 1: Explore the project (5 minutes)

In the terminal with Kilo:

```text
What is the structure of this project?
```

```text
List the files in week_01.
```

### Exercise 2: Understand a file (5 minutes)

```text
Explain what the file README.md contains.
```

```text
Summarize the key points in README.md.
```

### Exercise 3: Git exploration (5 minutes)

```text
Show me the current git status.
```

```text
Explain whether there are any changed files.
```

```text
Show me the recent commit history.
```

```text
What was changed in the most recent commit?
```

---

## Tips for Using Kilo

1. **Be specific**: "Explain the Week 1 section of README.md" vs "explain this"
2. **Use natural language**: No special syntax needed
3. **Provide context**: "In the ml_package folder, find..."
4. **Iterate**: If response isn't right, ask for clarification
5. **Verify**: Check files after modifications

---

## Kilo Configuration (Course Environment)

The course repository may include Kilo-related files such as:

- `.kilo/package.json`
- `.kilo/agent-manager.json`
- `.kilo/plans/`

Your instructor will confirm the exact startup command or classroom setup. You do not need to modify Kilo configuration for Week 1.

---

## Common Pitfalls

### Pitfall 1: Not providing enough context

**Symptom**: Kilo doesn't know which file you mean.

**Fix**: Specify the file:
- "In the file `README.md`, explain the Week 1 resources"

### Pitfall 2: Asking for actions without verification

**Symptom**: Kilo modifies something you didn't expect.

**Fix**: In Week 1, prefer read-only questions. If you do try edits, use a scratch file and always review changes before confirming.

### Pitfall 3: Mixing with regular terminal commands

**Symptom**: Unclear whether you're talking to Kilo or running shell commands.

**Fix**: Use clear natural language for Kilo; shell syntax for commands.

---

## Self-check

- Can you send a natural language command to Kilo?
- Can you ask Kilo about a file's contents?
- Can you ask Kilo about Git status or history without making changes?
- Do you understand when Kilo is better than Cursor/ChatGPT?

---

## References

- Kilo documentation: `.kilo/` directory in this repository
- Terminal basics: Week 2 tutorials
