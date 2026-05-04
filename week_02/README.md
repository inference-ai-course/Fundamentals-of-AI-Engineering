# Week 2: IDE + AI-Assisted Code Practice

## Week Overview

Building on the foundation established in Week 1, students will now transition from browser-based AI interactions to using AI directly within an Integrated Development Environment (IDE). This week focuses on integrating AI assistants into your daily coding workflow to enhance productivity, code understanding, and debugging capabilities.

## Learning Objectives

By the end of this week, you will be able to:

- Install and configure VS Code or Cursor with AI assistant integrations
- Configure AI assistants for optimal coding assistance
- Navigate basic IDE operations with AI-powered features
- Read and comprehend unfamiliar codebases using AI assistance
- Modify existing code with AI-guided suggestions and refactoring
- Debug common errors efficiently using AI-powered debugging tools

## Prerequisites

- **Week 1 completion**: Students must have completed Week 1 exercises and understand fundamental prompt engineering concepts
- Basic familiarity with command line operations is helpful, but the required commands are introduced in class
- Access to a computer capable of running VS Code or Cursor

## Sessions

### Session 1: IDE Setup and AI Configuration

In this session, students will:

- Install VS Code or Cursor IDE
- Set up AI assistant extensions (GitHub Copilot, Cursor AI, or alternatives)
- Configure AI settings for optimal performance
- Explore the IDE interface and AI integration points
- Complete initial configuration exercises

### Session 2: Code Reading and Modification with AI

In this session, students will:

- Learn techniques for using AI to understand unfamiliar code
- Practice asking AI to explain code functionality
- Use AI to identify patterns and architecture in codebases
- Apply AI suggestions for code modification and refactoring
- Work with provided templates to practice code changes

### Session 3: Debugging Workshop

In this session, students will:

- Learn AI-assisted debugging techniques
- Practice debugging common programming errors
- Use AI to analyze error messages and stack traces
- Implement fixes based on AI recommendations
- Develop a systematic approach to debugging with AI support

## Topics Covered

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

1. **Code Exploration Exercise**: Use AI to understand a provided codebase and document its functionality
2. **Code Modification Exercise**: Implement specific changes to existing code with AI guidance
3. **Debugging Challenge**: Identify and fix bugs in provided code samples using AI assistance
4. **IDE Proficiency Exercise**: Complete a series of IDE tasks incorporating AI features

### Safe Practice Rule

Do not edit the original files in `code_templates/`. Copy the files you want to modify into a `modified_code/` folder first, then make all changes in the copied files.

Recommended setup from the `week_02/` folder:

```bash
mkdir -p modified_code
cp code_templates/simple_math.py modified_code/simple_math.py
cp code_templates/data_processing.py modified_code/data_processing.py
cp code_templates/debugging_practice.py modified_code/debugging_practice_fixed.py
```

Quick verification commands:

```bash
python --version
python -B -m py_compile modified_code/simple_math.py
cd modified_code
python -c "from simple_math import add_numbers; print(add_numbers(2, 3))"
```

Complete exercise instructions are available in this week's tutorial files:

- [01_ide_setup.md](01_ide_setup.md)
- [02_ai_assisted_workflow.md](02_ai_assisted_workflow.md)
- [03_reading_code_with_ai.md](03_reading_code_with_ai.md)
- [04_modifying_code_with_ai.md](04_modifying_code_with_ai.md)
- [05_debugging_with_ai.md](05_debugging_with_ai.md)

## Deliverables

Students must submit the following by the end of Week 2:

| Deliverable | What it should contain |
|-------------|------------------------|
| `report.md` | Explanations for at least 5 functions or code blocks, plus a short reflection |
| `modified_code/` | Copies of template files with 2-3 small AI-assisted modifications |
| `debugging_record.md` | One complete debugging record: error, AI prompt, fix, verification |
| `prompts.md` | Prompts used for explanation, modification, and debugging |
| `README.md` | How to open the work, what was modified, and how to verify it |

Use the blank templates in [`submission_template/`](submission_template/) if you want a starting structure.

Your submission must also include an AI use declaration: which tool you used, what suggestions you accepted or rejected, and how you personally verified the result.

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
- Forgetting to save your copied files before making AI-assisted changes

---

*For questions or support, reach out in the course discussion forum or during office hours.*
