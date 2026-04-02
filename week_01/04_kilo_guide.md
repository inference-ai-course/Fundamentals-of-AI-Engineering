# Week 1 — Part 04: Kilo Guide

## Overview

**Kilo** is an open-source AI coding assistant that runs in your terminal. Unlike Cursor (GUI), Kilo is CLI-based — you interact through text commands.

Kilo is already configured in your course environment.

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
4. **Local execution**: Works with your local files and tools

---

## How Kilo Works

### The interaction model

```
You → Type command in terminal → Kilo processes → Kilo responds/acts → You see result
```

### Key capabilities

| Capability | Example |
|------------|---------|
| **Read files** | Understand project structure |
| **Write files** | Generate and modify code |
| **Git operations** | Create commits, understand diffs |
| **Search** | Find patterns across project |
| **Execute** | Run commands, scripts |

---

## Using Kilo (Basic Patterns)

### Pattern 1: Ask questions

Simply type your question in the terminal where Kilo is running:

```
What files are in this directory?
```

```
Explain what the file train.py does.
```

### Pattern 2: Request modifications

```
Add a comment to the first function in main.py explaining what it does.
```

```
Create a new file called utils.py with a helper function for data loading.
```

### Pattern 3: Git operations

```
Show me the recent commit history.
```

```
What changed in the last commit?
```

### Pattern 4: Search and analyze

```
Find all files that import pandas.
```

```
Search for the function definition of process_data.
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
```
Explain what changed between the last two commits.
```

### 2. Project context

Like Cursor, Kilo reads your files. It understands:
- File structure
- Code relationships
- Project architecture

### 3. Autonomous execution

Kilo can perform actions:
- Edit files directly
- Run terminal commands
- Create commits

**Example:**
```
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
| **Information** | "List all Python files" |
| **Explanation** | "Explain the function train_model" |
| **Creation** | "Create a README.md file" |
| **Modification** | "Add type hints to utils.py" |
| **Git** | "Show recent commits" |
| **Search** | "Find where process_data is defined" |

---

## Practical Exercises

### Exercise 1: Explore the project (5 minutes)

In the terminal with Kilo:

```
What is the structure of this project?
```

```
List all Python files.
```

### Exercise 2: Understand a file (5 minutes)

```
Explain what the file README.md contains.
```

```
Summarize the key points in README.md.
```

### Exercise 3: Git exploration (5 minutes)

```
Show me the recent commit history.
```

```
What was changed in the most recent commit?
```

---

## Tips for Using Kilo

1. **Be specific**: "Explain lines 10-20 of train.py" vs "explain train.py"
2. **Use natural language**: No special syntax needed
3. **Provide context**: "In the ml_package folder, find..."
4. **Iterate**: If response isn't right, ask for clarification
5. **Verify**: Check files after modifications

---

## Kilo Configuration (Course Environment)

Kilo is pre-configured in your course environment:

- Configuration file: `.kilo/kilo.json`
- Instructions: `.kilo/agent/*.md`
- Commands: `.kilo/command/*.md`

You don't need to configure anything for this course.

---

## Common Pitfalls

### Pitfall 1: Not providing enough context

**Symptom**: Kilo doesn't know which file you mean.

**Fix**: Specify the file:
- "In the file `train.py`, explain the first function"

### Pitfall 2: Asking for actions without verification

**Symptom**: Kilo modifies something you didn't expect.

**Fix**: Always review changes before confirming.

### Pitfall 3: Mixing with regular terminal commands

**Symptom**: Unclear whether you're talking to Kilo or running shell commands.

**Fix**: Use clear natural language for Kilo; shell syntax for commands.

---

## Self-check

- Can you send a natural language command to Kilo?
- Can you ask Kilo about a file's contents?
- Can you ask Kilo about Git history?
- Do you understand when Kilo is better than Cursor/ChatGPT?

---

## References

- Kilo documentation: `.kilo/` directory in this repository
- Terminal basics: Week 2 tutorials