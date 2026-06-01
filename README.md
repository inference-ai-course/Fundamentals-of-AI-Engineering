# Fundamentals of AI Engineering - 6-Week Beginner Program

## Course Overview

The **Fundamentals of AI Engineering** course is designed for AI beginners, including learners with non-technical backgrounds. It follows a progressive model:

**Agent Tools Introduction -> AI-Assisted Python Setup and Code Practice -> Technical Practice -> Capstone Delivery**

The course emphasizes practical confidence, conceptual intuition, AI-assisted learning, and reproducible project delivery. Students first learn how to collaborate with AI tools, then gradually use those tools to understand code, process data, call LLMs, run basic ML experiments, and complete a small end-to-end AI project.

## Target Students

- **Complete Beginners**: Learners with no programming experience who want to enter AI, data analytics, or AI-assisted development.
- **Tool Users**: Professionals already using AI tools who want stronger technical foundations.
- **Technical Learners**: Developers or analysts who want a beginner-friendly path through core AI engineering habits.

## Prerequisites

### Week 1: No Programming Required

- Ability to use a browser and create online accounts.
- Ability to install and open desktop software.
- Basic computer operation skills.

### Week 2: Guided Python With AI Assistance

- No prior Python experience is required.
- Students will run guided Python commands, create a virtual environment, and debug small examples with AI support.
- The focus is fluency with AI learning workflows, not independent programming from scratch.

### Weeks 3-6: Introductory Technical Practice With AI Assistance

- Basic terminal operations will be introduced in class.
- Python concepts are taught through guided examples and AI-assisted practice.
- Self-learn materials are optional refreshers, not required prerequisites.

## Learn AI With AI

The core philosophy is **"Learn AI with AI"**:

1. **Week 1**: Learn to use AI tools such as ChatGPT, Claude, Cursor, Kilo, and GitHub Copilot Chat for general tasks.
2. **Week 2**: Use those AI tools to learn Python, set up an environment, run code, and debug errors.
3. **Weeks 3-6**: Use AI tools to process data, build LLM workflows, run simple experiments, and deliver a capstone.

AI is a learning accelerator, not a replacement for understanding. Students are expected to explain their work, document how AI helped, and verify outputs before trusting them.

## Course Navigation

- [Pre-Study Guide](PRESTUDY.md) - Optional preparation before the course.
- [Course Syllabus](SYLLABUS.md) - Detailed 6-week schedule.
- [Capstone Project](capstone.md) - Final AI-assisted CSV data analyzer.

### Optional Self-Study References

Use these only when you want extra background or review:

- [Self-Study Schedule](self_learn/Schedule.md)
- [Chapter 1: Tool Preparation](self_learn/Chapters/1/Chapter1.md)
- [Chapter 2: Python and Environment Management](self_learn/Chapters/2/Chapter2.md)
- [Chapter 3: AI Engineering Basics](self_learn/Chapters/3/Chapter3.md)
- [Chapter 4: Hugging Face Platform and Local Inference](self_learn/Chapters/4/Chapter4.md)
- [Chapter 5: Resource Monitoring and Containerization](self_learn/Chapters/5/Chapter5.md)

The [old_v1/](old_v1/) directory contains the previous 8-week course and is kept as an archive/reference for deeper self-study.

## Course Duration

- **Total Duration**: 6 weeks
- **Weekly Hours**: 5 hours recommended
- **Suggested Rhythm**:
  - Session 1: Core concepts and examples
  - Session 2: Hands-on guided practice
  - Session 3: Q&A, review, and project support

## 6-Week Teaching Plan

| Week | Theme | Main Outcome |
|------|-------|------------------|
| Week 1 | Agent Tools Introduction | AI tool experience report, representative prompts, and reflection |
| Week 2 | AI-Assisted Python Setup + Code Practice | AI Python prompt log, environment check, code run evidence, modifications, and debugging record |
| Week 3 | Data Processing + Reproducible Outputs | CSV data profiling script with `profile.json` and `profile.md` |
| Week 4 | LLM Fundamentals + API Reliability | `profile.json` -> structured insights demo with validation and reliability notes |
| Week 5 | ML Training Loop | Two lightweight baseline runs and a short comparison report |
| Week 6 | Capstone: AI-Assisted CSV Data Analyzer | CSV -> real LLM call -> `report.json` + `report.md` + short demo |

## Learning Outcomes

By the end of the course, students will be able to:

1. **Use AI agent tools effectively**
   - Select appropriate tools for writing, research, code explanation, and debugging.
   - Document useful prompts and reflect on tool strengths and limits.

2. **Read, modify, and debug code with AI assistance**
   - Explain simple Python functions.
   - Make small changes safely.
   - Use error messages and AI feedback to debug.

3. **Process data reproducibly**
   - Create and verify a clean Python environment before data work.
   - Load and inspect CSV data with pandas.
   - Generate stable JSON and Markdown profiling reports.

4. **Build basic LLM workflows**
   - Explain tokens, context windows, and structured prompts.
   - Request JSON-like outputs and validate them.
   - Add beginner-friendly timeout, retry, and logging practices.
   - Convert a data profile into structured AI-style insights without requiring API access.

5. **Understand the ML training loop**
   - Train a basic baseline model.
   - Save metrics and compare two runs.
   - Explain results without relying on advanced math.

6. **Deliver a small end-to-end AI project**
   - Build a reproducible AI-assisted CSV data analyzer.
   - Combine data profiling, compression, real LLM interpretation, and report generation.
   - Demonstrate the project and explain key decisions.

## Technology Stack

### Week 1: Tool Usage Phase

- **AI Chat Tools**: ChatGPT / Claude

### Week 2: AI-Assisted Python Setup and Code Practice

- **AI Chat Tools**: ChatGPT / Claude
- **AI Editor**: Cursor or VS Code with AI assistant
- **AI Programming Assistants**: Kilo, GitHub Copilot Chat, or equivalents
- **Python Tools**: virtual environments, `pip`, optional Jupyter notebooks

### Weeks 3-6: Technical Practice Phase

- **Language**: Python 3.10+ (3.11 recommended)
- **Core Libraries**: `pandas`, `numpy`, `scikit-learn`
- **Engineering Tools**: virtual environments, `requirements.txt`, basic logging, optional `pytest`
- **LLM Options**: Week 4 required work uses an offline/mock path; hosted API or local inference is optional

## Weekly Resources

- [Week 1](week_01/README.md): Agent tools introduction
- [Week 2](week_02/README.md): AI-assisted Python setup, running code, and debugging
- [Week 3](week_03/README.md): Data processing and reproducible outputs
- [Week 4](week_04/README.md): LLM fundamentals and API reliability
- [Week 5](week_05/README.md): ML training loop
- [Week 6](week_06/README.md): Capstone project

## Learning Path After This Course

After finishing this beginner program, students can continue with:

- RAG fundamentals and vector databases
- Agent systems and tool use
- Production deployment with FastAPI or Docker
- Advanced local inference and model evaluation

## How to Ask for Help

When asking instructors, classmates, or AI tools for help, include:

1. Goal: what you are trying to do.
2. Context: which week and which step.
3. Exact command and full output.
4. Environment: OS, Python version, dependency file.
5. What you already tried.

This course values evidence-based debugging: reproduce the issue, capture the details, and then ask for help.

---

**Course Version**: v2.2 (6-Week Beginner Program)
**Last Updated**: 2026-05-11
**Major Changes**: Week 2 now includes AI-assisted Python learning and environment setup; Week 3 now focuses on data processing; Week 4 now covers LLM fundamentals and simplified API reliability; Week 6 is unified around the intelligent data analysis capstone.
