# Week 2: AI-Assisted Python Setup, Running Code, and Debugging

## Week Overview

Building on Week 1, students now transition from general AI tool use to AI-assisted Python learning. This week focuses on using AI tools fluently: asking coding questions, setting up a Python environment, running simple code, reading functions, making small edits, and debugging real errors.

Week 2 is guided programming practice, not independent software development. Students are expected to use AI as a tutor while they personally run code and verify results.

## Learning Objectives

By the end of this week, you will be able to:

- Explain the basic landscape of IDEs, AI editor extensions, and command-line AI coding tools
- Install and configure VS Code or Cursor with AI assistant integrations
- Use ChatGPT, Claude, Cursor, Copilot Chat, or Claude Code-style tutor workflows to learn Python
- Create and activate a Python virtual environment for course work
- Run simple Python scripts and optional Jupyter notebooks
- Navigate basic IDE operations with AI-powered features
- Read and comprehend unfamiliar codebases using AI assistance
- Modify existing code with AI-guided suggestions and refactoring
- Debug common errors efficiently using AI-powered debugging tools

## Prerequisites

- **Week 1 completion**: Students must have completed Week 1 exercises and understand fundamental prompt engineering concepts
- No prior Python experience is required, but students will run guided Python commands in class
- Basic familiarity with command line operations is helpful, but the required commands are introduced in class
- Access to a computer capable of running VS Code or Cursor

## Sessions

### Optional: AI Coding Tools Landscape

If students feel lost in the tool names, they can first:

- Understand what an IDE is and why it matters.
- Compare VS Code, Cursor, AI extensions, and command-line coding tools.
- Identify which tools are required for Week 2 and which are optional awareness.
- Choose a beginner-friendly tool path for the hands-on exercises.

### Session 1: IDE Setup and AI Configuration

In this session, students will:

- Install VS Code or Cursor IDE
- Set up AI assistant extensions (GitHub Copilot, Cursor AI, or alternatives)
- Configure AI settings for optimal performance
- Explore the IDE interface and AI integration points
- Complete initial configuration exercises

### Session 2: Python Environment + Run Code First

In this session, students will:

- Create and activate a `.venv`
- Install Week 2 dependencies from `requirements.txt`
- Verify `python`, `pip`, and `pandas`
- Run `run_template_examples.py`
- Use AI to explain the command output

### Session 3: Code Reading and Modification with AI

In this session, students will:

- Learn techniques for using AI to understand unfamiliar code
- Practice asking AI to explain code functionality
- Use AI to identify patterns and architecture in codebases
- Apply AI suggestions for code modification and refactoring
- Work with provided templates to practice code changes

### Session 4: Debugging Workshop

In this session, students will:

- Learn AI-assisted debugging techniques
- Practice debugging common programming errors
- Use AI to analyze error messages and stack traces
- Implement fixes based on AI recommendations
- Develop a systematic approach to debugging with AI support

## Topics Covered

### AI Coding Tools Landscape

- IDEs and code editors.
- VS Code extension ecosystem.
- AI extensions such as Copilot Chat, Cline, Cursor, and Kilo Code.
- Command-line AI coding tools such as Claude Code, OpenAI Codex CLI, and Kilo.
- Workflow and project management tools for AI-assisted coding.

### Installing VS Code or Cursor

- Downloading and installing the IDE
- Initial setup and configuration
- Extension marketplace navigation
- Workspace and project management

### Configuring AI Assistants

- Setting up GitHub Copilot, Cursor AI, or alternative assistants
- Configuring API keys and authentication
- Customizing AI behavior and suggestions
- Privacy and security considerations

### Basic IDE Operations

- File navigation and project structure
- Code editing and navigation shortcuts
- Terminal integration
- Version control integration (Git)

### Python Environment Setup

- System Python vs project virtual environments
- Creating and activating `.venv`
- Installing dependencies from `requirements.txt`
- Verifying package imports
- Selecting the correct notebook kernel when using Jupyter

### Learning Python With AI

- Asking AI to explain variables, lists, dictionaries, functions, imports, and file paths
- Using tutor-style prompts that ask students to predict output and complete small changes
- Optional Claude Code Learning output style for learn-by-doing workflows
- Recording prompts and personal verification steps

### Reading Code with AI Help

- Using AI to explain function and class purposes
- Understanding complex algorithms with AI assistance
- Mapping code dependencies and relationships
- Documenting code using AI-generated explanations

### Modifying Code with AI Help

- Requesting code refactoring suggestions
- Implementing AI-generated code changes
- Reviewing and validating AI suggestions
- Maintaining code quality while using AI assistance

### Debugging Common Errors with AI

- Interpreting error messages with AI assistance
- Identifying root causes of bugs
- Generating and testing fixes
- Learning debugging patterns through AI explanations

## Exercises

All exercises use provided templates found in the `code_templates/` directory. Students will:

1. **AI Python Learning Exercise**: Use Week 1-style prompts to learn Python concepts needed for Week 3.
2. **Environment Setup Exercise**: Create `.venv`, install dependencies, and verify pandas.
3. **Run Code Exercise**: Run template functions from a script or notebook and explain the output.
4. **Code Exploration Exercise**: Use AI to understand a provided codebase and document its functionality.
5. **Code Modification Exercise**: Implement specific changes to existing code with AI guidance.
6. **Debugging Challenge**: Fix one runtime error and one logic error using the isolated scripts in `debugging_exercises/`.
7. **Mixed Debugging Challenge (Optional)**: Try `code_templates/debugging_practice.py` after the isolated exercises.

Complete exercise instructions are available in this week's tutorial files:

- [01_ide_setup.md](01_ide_setup.md)
- [ai_python_learning_prompts.md](ai_python_learning_prompts.md)
- [06_python_environment_setup.md](06_python_environment_setup.md)
- [02_ai_assisted_workflow.md](02_ai_assisted_workflow.md)
- [03_reading_code_with_ai.md](03_reading_code_with_ai.md)
- [04_modifying_code_with_ai.md](04_modifying_code_with_ai.md)
- [05_debugging_with_ai.md](05_debugging_with_ai.md)
- [debugging_exercises/README.md](debugging_exercises/README.md)

Optional support materials:

- [00_ai_coding_tools_landscape.md](00_ai_coding_tools_landscape.md)
- [01_python_with_ai_basics.ipynb](01_python_with_ai_basics.ipynb)
- [02_debugging_with_ai_lab.ipynb](02_debugging_with_ai_lab.ipynb)
- [code_templates/debugging_practice.py](code_templates/debugging_practice.py) - final mixed challenge

## What to Complete

By the end of Week 2, aim to finish:

### 1. AI Python Learning Log

A short log covering:
- 5 useful Python-learning or debugging prompts derived from Week 1 patterns
- Tool used for each prompt
- What the AI helped explain
- What you personally ran or verified

### 2. Environment Check

A short file containing:
- `python --version`
- `which python` or `where python`
- `pip --version`
- `python -c "import pandas as pd; print(pd.__version__)"`

### 3. Code Running Evidence

A record of commands or notebook cells used to run sample code, with at least 3 successful function outputs.

### 4. Code Explanation Exercise

A detailed explanation document covering:
- Analysis of the provided template codebase
- AI-assisted breakdown of key functions and components
- Architecture and design pattern identification
- Personal observations and learning notes

### 5. Code Modification and Debugging Report

A report documenting:
- Description of modifications made to the template code
- AI suggestions used and how they were implemented
- Challenges encountered and how they were resolved
- Before/after comparison of code quality and functionality
- At least one runtime error and one logic error debugged with AI
- Optional: one pandas/data debugging case

## Resources and Tips

### Recommended Resources

- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Cursor Documentation](https://cursor.sh/docs)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- Week 1 review materials for prompt engineering fundamentals

### Tips for Success

1. **Start with small tasks**: Begin with simple AI requests before tackling complex refactoring
2. **Verify AI suggestions**: Always review and understand AI-generated code before accepting it
3. **Use specific prompts**: Apply Week 1 prompt engineering skills for better AI responses
4. **Practice regularly**: Spend time daily using the IDE with AI to build muscle memory
5. **Keep notes**: Document useful AI interactions and IDE shortcuts for future reference
6. **Ask for explanations**: When AI suggests code changes, ask it to explain why
7. **Maintain code ownership**: Use AI as a tool, not a replacement for understanding your code

### Common Pitfalls to Avoid

- Blindly accepting AI suggestions without understanding them
- Over-relying on AI for simple tasks you should learn to do manually
- Neglecting to test AI-generated code thoroughly
- Forgetting to commit code before making AI-assisted changes

---

*For questions or support, reach out in the course discussion forum or during office hours.*
