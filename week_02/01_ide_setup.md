# Week 2 — Part 01: IDE Setup and AI Configuration

## Overview

Your first step is setting up an IDE (Integrated Development Environment) with AI integration. We recommend Cursor, but VS Code with Copilot is also an option.

If terms like IDE, extension, command-line coding tool, or AI editor are unfamiliar, start with [00_ai_coding_tools_landscape.md](00_ai_coding_tools_landscape.md) before installing anything.

---

## Why an IDE with AI?

### The difference from browser-based AI

| Browser-based AI (ChatGPT) | IDE with AI (Cursor) |
|---------------------------|----------------------|
| You paste code manually | AI reads files directly |
| No project context | AI knows your project |
| Manual file operations | AI can edit files |
| Separate window | Integrated in your workspace |

### What you gain

- **File awareness**: AI sees what you're working on
- **Project context**: AI understands relationships between files
- **Direct editing**: AI can modify code in your files
- **Integrated workflow**: Everything in one place

---

## Setup Checklist: Cursor

| Step | Action | Success looks like |
|------|--------|-------------------|
| 1 | Download from cursor.sh | Installer downloaded |
| 2 | Run installer | Cursor opens |
| 3 | Sign in (optional) | Can use AI features |
| 4 | Open project folder | Files visible in sidebar |
| 5 | Open AI chat (Cmd+L) | Chat panel appears |

### Detailed steps

**Step 1: Download**
- Go to [cursor.sh](https://cursor.sh)
- Download for your platform (Mac, Windows, Linux)

**Step 2: Install**
- Run the installer
- Follow prompts
- Cursor opens automatically after installation

**Step 3: Sign in (optional but recommended)**
- Cursor may prompt you to sign in
- This enables AI features
- Use the course-recommended account, license, or currently available plan

**Step 4: Open a folder**
- File → Open Folder
- Choose the course repository folder, then navigate to `week_02/code_templates`
- Files appear in the sidebar

**Step 5: Open AI chat**
- Press Cmd+L (Mac) or Ctrl+L (Windows)
- Chat panel opens on the right
- You can now interact with AI

---

## Alternative: VS Code + GitHub Copilot

If you prefer VS Code:

| Step | Action | Success looks like |
|------|--------|-------------------|
| 1 | Install VS Code | VS Code opens |
| 2 | Install Copilot extension | Copilot icon appears |
| 3 | Sign in to GitHub | Copilot activated |
| 4 | Open folder | Files visible |

**Note**: VS Code + Copilot features may differ from Cursor. Use the same Ask → Review → Apply → Verify workflow regardless of tool.

---

## Cursor Interface Tour

### Key areas

| Area | Shortcut | Purpose |
|------|----------|---------|
| **File explorer** | Cmd+B | Browse project files |
| **Editor** | — | View and edit files |
| **AI Chat** | Cmd+L | Conversational AI |
| **Terminal** | Cmd+J | Run commands |
| **AI Inline** | Cmd+K | Edit at cursor position |

### Two AI modes

1. **Chat mode** (Cmd+L)
   - Conversation with AI
   - Ask questions about your project
   - Request explanations
   - Plan modifications

2. **Inline mode** (Cmd+K)
   - Select code → press Cmd+K
   - Describe what you want
   - AI edits directly in the file

---

## Essential Shortcuts

| Shortcut (Mac) | Shortcut (Win) | Action |
|----------------|-----------------|--------|
| Cmd+L | Ctrl+L | Open AI chat |
| Cmd+K | Ctrl+K | Inline AI edit |
| Cmd+B | Ctrl+B | Toggle file explorer |
| Cmd+J | Ctrl+J | Toggle terminal |
| Cmd+S | Ctrl+S | Save file |
| Cmd+P | Ctrl+P | Quick file open |

**Practice these**: They're essential for efficient workflow.

---

## Configuring AI Behavior

### AI model selection

Cursor or other AI coding tools may let you choose a model. The exact names change over time, so use the instructor-recommended option or a currently available high-quality model.

| Option | When to use |
|--------|-------------|
| **Instructor-recommended model** | Best default for class exercises |
| **High-quality reasoning model** | Explaining code, debugging, reviewing changes |
| **Fast model** | Quick syntax questions or simple comments |

**Recommendation**: Use the instructor-recommended model first. If you are unsure, choose the most capable model available in your tool for learning exercises.

### AI settings (optional)

You can customize:
- **Context files**: Which files AI should prioritize
- **Response style**: More concise vs more detailed
- **Auto-suggestions**: Enable/disable inline suggestions

**For beginners**: Use default settings first.

---

## Verification: Is it working?

### Test your setup

1. Open Cursor
2. Open the course repository folder
3. Press Cmd+L to open AI chat
4. Send this prompt:
   ```text
   What files are in this folder?
   ```
5. You should receive a response listing the files

### Test the terminal

Open the integrated terminal with Cmd+J or Ctrl+J and run:

```bash
python --version
```

You should see a Python version number. If `python` is not recognized on your computer, try:

```bash
python3 --version
```

If this works, your setup is complete.

---

## Common Pitfalls

### Pitfall 1: Opening wrong folder

**Symptom**: AI doesn't see the files you expect.

**Fix**: Check which folder you opened:
- File explorer shows the folder contents
- If wrong, File → Open Folder → choose correct one

### Pitfall 2: AI chat not opening

**Symptom**: Cmd+L doesn't open chat panel.

**Fix**:
- Check if Cursor is the active window
- Try View → AI Chat from menu
- Restart Cursor if needed

### Pitfall 3: No AI response

**Symptom**: You send a prompt but get no response.

**Fix**:
- Check if you're signed in (required for AI)
- Check whether your account, course license, or selected model is available
- Try simpler prompt to test connectivity

### Pitfall 4: Can't find shortcuts

**Symptom**: Shortcuts don't work or you don't know them.

**Fix**:
- View → Command Palette (Cmd+Shift+P)
- Type "AI" to find AI-related commands
- Keyboard shortcuts are shown in menu

---

## Hands-on Exercises

### Exercise 1: Open and explore (5 minutes)

1. Open Cursor
2. Open the course repository folder
3. Browse the files in the sidebar
4. Click `week_02/code_templates/simple_math.py` to view its contents

### Exercise 2: First AI chat (5 minutes)

1. Press Cmd+L to open AI chat
2. Send: "What files are in this project?"
3. Review the response
4. Send: "Which file should I start with?"

### Exercise 3: Try inline editing (10 minutes)

1. Create a `modified_code/` folder for practice work
2. Copy `code_templates/simple_math.py` into `modified_code/simple_math.py`
3. Open `modified_code/simple_math.py`
4. Select a function
5. Press Cmd+K
6. Type: "Add a comment explaining what this function does"
7. Review the change

Keep `code_templates/simple_math.py` unchanged. It is the original reference copy.

---

## Self-check

- Have you installed Cursor?
- Can you open a folder and see files?
- Can you open the AI chat panel (Cmd+L)?
- Can you send a prompt and receive a response?
- Can you use inline editing (Cmd+K)?

---

## References

- Cursor: https://cursor.sh
- Cursor Docs: https://cursor.sh/docs
- VS Code: https://code.visualstudio.com
- GitHub Copilot: https://github.com/features/copilot
