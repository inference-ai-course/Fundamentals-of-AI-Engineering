# AI Engineering Fundamentals - Course Syllabus

## Course Information

| Attribute | Details |
|-----------|---------|
| **Course Name** | AI Engineering Fundamentals |
| **Version** | v2.0 (6-Week Program) |
| **Duration** | 6 weeks |
| **Weekly Hours** | 5 hours (3 hours lecture + 2 hours lab/workshop) |
| **Delivery Method** | In-person instruction + hands-on workshops |
| **Target Students** | Non-technical backgrounds; no prior programming experience required |

---

## Course Introduction

AI Engineering Fundamentals is specifically designed for students from non-technical backgrounds, employing an innovative three-stage progressive teaching model: **"Agent Tools Introduction → AI-Assisted Learning → Technical Hands-on Practice."**

The first two weeks require no programming background. Students will first learn to use AI Agent tools such as Cursor, ChatGPT, and Kilo, establishing an intuitive understanding of AI capabilities and developing effective methodologies for working with AI. Starting from Week 3, students will gradually learn core technical skills—including Python programming, local inference, API engineering, data processing, machine learning, and LLM applications—with the assistance of AI tools.

### Core Philosophy

**"Learn AI with AI"** — Make AI an accelerator for learning, not a replacement for understanding.

---

## Learning Objectives

Upon completing this course, students will be able to:

### 1. Proficiently Use AI Agent Tools
- Master mainstream AI tools including Cursor, ChatGPT, and Kilo
- Select appropriate AI tools based on task requirements
- Understand the capabilities and limitations of AI tools in various contexts

### 2. Use AI to Assist Programming and Learn Python
- Read, modify, and debug code with AI assistance
- Adopt AI-collaborative programming methods without learning every detail from scratch
- Develop foundational Python programming skills

### 3. Understand and Practice Local Inference & API Engineering
- Set up and run local models using Ollama
- Understand the differences between local inference and cloud APIs and their appropriate use cases
- Implement reliable LLM clients with timeout, retry, and rate-limiting mechanisms

### 4. Master Data Processing Fundamentals
- Use pandas for data loading, cleaning, and analysis
- Generate structured data profiling reports
- Understand how data quality impacts AI model performance

### 5. Complete ML Training Experiments and LLM Application Projects
- Train machine learning models and conduct experimental comparisons
- Design effective prompt templates
- Complete end-to-end AI application projects and present findings

---

## Weekly Schedule

### Week 1: Agent Tools Introduction

**Theme:** Using AI Without Writing Code

#### Learning Objectives
- Understand the concept of AI Agents and mainstream tools
- Master basic usage of Cursor, ChatGPT, Kilo, and similar tools
- Develop intuition for AI capabilities and establish usage methodologies

#### Session 1 (2h) - Agent Tools Overview and Demonstration
- What are AI Agents? (Concept explanation + analogies)
- Introduction to mainstream Agent tools:
  - **Cursor:** Code editor + AI assistant
  - **Kilo:** AI programming assistant
  - **ChatGPT/Claude:** General-purpose conversational AI
  - **GitHub Copilot Chat:** Code conversation assistant
- Live demonstrations: Using natural language to accomplish simple tasks
  - "Help me write a job application email"
  - "Explain what this code does"
  - "Organize this Excel data into a table"

#### Session 2 (2h) - Hands-on Experience
- Student registration and tool installation
- Practice tasks:
  - Write an article using ChatGPT
  - Open a project folder in Cursor and have AI explain the project structure
  - Complete a simple instruction using Kilo
- Sharing session: Most successful AI collaboration experiences

#### Session 3 (1h) - Discussion and Reflection
- Advantages and limitations of Agent tools
- When to use AI vs. doing it yourself
- Sharing usage tips and prompt insights

#### Deliverables
- Complete 3 different types of Agent tool experience tasks
- Write an "Agent Tools Usage Reflection" report (800-1000 words)

#### Assessment: 10%

#### Resources
- [week_01/README.md](week_01/README.md)
- [slides/week_01.md](slides/week_01.md)

---

### Week 2: IDE + Agent Practice

**Theme:** Starting to Work with Code

#### Learning Objectives
- Use AI assistants within IDE environments
- Learn to have AI help you read and modify code
- Understand the "AI-assisted programming" workflow
- Gain initial exposure to Python code

#### Session 1 (2h) - IDE + AI Environment Setup
- Install VS Code or Cursor
- Configure GitHub Copilot / Cursor AI
- Learn basic IDE operations:
  - Opening files
  - Running terminal commands
  - Viewing output
- AI-assisted programming workflow:
  - Using AI to explain code
  - Using AI to modify code
  - Using AI to generate code

#### Session 2 (2h) - Code Reading and Modification Practice
- Use provided Python project templates
- Task 1: Have AI explain what each code segment does (at least 5 functions)
- Task 2: Request modifications and have AI help you change the code (at least 3 modifications)
  - "Modify this function to accept user input"
  - "Add comments to this function"
- Task 3: Run the code and observe results

#### Session 3 (1h) - Problem-Solving Workshop
- Common errors and how to debug with AI
- What to do when AI gives incorrect answers
- Student showcase: Code modifications completed with AI assistance

#### Deliverables
- Complete code explanation exercise (explain at least 5 functions)
- Complete code modification tasks (at least 3 modifications)
- Write an "AI-Assisted Programming Reflection" report (800-1000 words)

#### Assessment: 10%

#### Resources
- [week_02/README.md](week_02/README.md)
- [slides/week_02.md](slides/week_02.md)

---

### Week 3: Local Inference & API Engineering

**Theme:** From Local to Cloud - Understanding LLM Invocation

#### Learning Objectives
- Set up local Python development environments
- Install and run Ollama local models
- Understand the differences between local inference and cloud APIs
- Master reliability engineering for LLM APIs
- Implement robust LLM clients

#### Session 1 (2h) - Environment Setup and Local Inference
- Python environment installation (using Anaconda for simplicity)
- Virtual environment concepts and creation
- Install Ollama
- Download and run local models (llama3.2:1b)
- Interact with models via command line

#### Session 2 (2h) - API Calls and Reliability Engineering
- Local inference vs. cloud API comparison
- API failure modes: timeouts, rate limiting, errors
- Implement timeout settings and retry strategies
- Add caching and logging
- Build a simple LLM client

#### Session 3 (1h) - Integration Practice
- Unified interface: Using the same calling method for local and cloud models
- Model comparison experiments (local vs. cloud quality, speed)
- Troubleshooting and optimization

#### Deliverables
- Successfully run Ollama local model
- Implement a reliable LLM client (supporting local + cloud)
- Complete model comparison experiment report (1000-1500 words)

#### Assessment: 15%

#### Resources
- [week_03/README.md](week_03/README.md)
- [slides/week_03.md](slides/week_03.md)

---

### Week 4: Data Processing Fundamentals

**Theme:** The Foundation of AI — Data

#### Learning Objectives
- Understand the importance of data for AI
- Learn to use pandas for basic data processing
- Generate data profiling reports
- Master CSV data loading, cleaning, and analysis

#### Session 1 (2h) - The Relationship Between Data and AI
- Why data quality determines AI effectiveness
- Pandas basics: reading CSV, viewing data
- Data types and basic statistics
- Practice: Load a dataset and view basic information

#### Session 2 (2h) - Data Cleaning and Exploration
- Handling missing values
- Identifying outliers
- Data distribution analysis
- Generate data profiles (JSON/Markdown output)

#### Session 3 (1h) - Data Report Workshop
- Students generate reports using their own datasets
- Share data discoveries
- Discussion: How data issues affect AI models

#### Deliverables
- Complete a data profiling report (JSON + Markdown format)
- Clean a real-world dataset
- Write a data quality analysis report (800-1200 words)

#### Assessment: 10%

#### Resources
- [week_04/README.md](week_04/README.md)
- [slides/week_04.md](slides/week_04.md)

---

### Week 5: ML Training Loop

**Theme:** Understanding the Machine Learning Workflow

#### Learning Objectives
- Understand the basic machine learning workflow
- Master train/validation split concepts
- Train a basic classification model
- Learn to compare results from different experiments

#### Session 1 (2h) - ML Fundamentals
- What is training? What is inference?
- Train/Validation/Test splits
- Overfitting and underfitting (intuitive explanations)
- Basic evaluation metrics: accuracy, F1 score

#### Session 2 (2h) - Train Your First Model
- Train classifiers using scikit-learn
- Save models and experiment configurations
- Evaluate model performance
- Run multiple experiments and compare results

#### Session 3 (1h) - Experiment Comparison Workshop
- Change parameters and observe performance changes
- Write experiment comparison reports
- Discussion: Under what conditions do models perform better?

#### Deliverables
- Train at least 2 different models
- Complete model comparison experiment report (1000-1500 words)
- Explain experimental design decisions

#### Assessment: 10%

#### Resources
- [week_05/README.md](week_05/README.md)
- [slides/week_05.md](slides/week_05.md)

---

### Week 6: LLM Application Practice

**Theme:** Integrating Knowledge to Complete End-to-End Projects

#### Learning Objectives
- Understand tokens and context window concepts
- Master basic prompt engineering techniques
- Apply pipeline thinking to integrate knowledge from Weeks 1-5
- Complete a simplified end-to-end project
- Course review and future outlook

#### Session 1 (2h) - LLM Basics and Prompt Engineering
- Tokenization introduction and context window limitations
- Prompt design best practices
- Structured prompts and JSON output
- Introduction to validation and retry mechanisms

#### Session 2 (2h) - End-to-End Project Practice
- Project introduction: Data Analysis Assistant (simplified version)
- Use provided project templates
- Data sampling and compression (using Week 4 skills)
- Build prompts to call LLM (using Week 3 skills)
- Generate reports (JSON + Markdown)

#### Session 3 (1h) - Project Presentation and Course Review
- Student project demonstrations (3-5 minutes each)
- Course highlights review
- Learning path recommendations (Level 2 preview)
- Closing ceremony

#### Deliverables
- Design 2-3 effective prompt templates
- Complete simplified data analysis project
- Project presentation (3-5 minutes)
- Project reflection report (500-800 words)

#### Assessment: 25%

#### Resources
- [week_06/README.md](week_06/README.md)
- [slides/week_06.md](slides/week_06.md)

---

## Assessment Breakdown

### Weekly Assessment Details

#### Week 1: Agent Tools Experience Report (10%)

**Evaluation Criteria:**
- Complete 3 different types of AI tasks (30%)
- Report content quality (50%):
  - Tool selection rationale
  - Usage process description
  - Success/failure case analysis
  - Reflections on AI capabilities
- Report format and expression (20%)

#### Week 2: AI-Assisted Programming Practice Report (10%)

**Evaluation Criteria:**
- Code explanation exercise completion (30%)
- Code modification task completion (30%)
- Report content quality (30%):
  - Summary of AI-assisted programming methods
  - Problems encountered and solutions
  - Reflections on AI-assisted learning
- Report format and expression (10%)

#### Week 3: Local Inference & API Engineering (15%)

**Evaluation Criteria:**
- LLM client code quality (40%):
  - Supports local and cloud calling
  - Timeout and retry mechanisms implemented
  - Clear code structure
  - Includes basic comments
- Model comparison experiment report (40%):
  - Reasonable experimental design
  - Adequate data analysis
  - Evidence-based conclusions
- Code executability (20%)

#### Week 4: Data Profiling Report (10%)

**Evaluation Criteria:**
- Data processing completeness (40%):
  - Correct data loading
  - Reasonable missing value handling
  - Accurate outlier identification
- Report quality (40%):
  - Clear data overview
  - Accurate statistical analysis
  - Valuable insights
- Output format compliance (20%)

#### Week 5: ML Experiment Comparison Report (10%)

**Evaluation Criteria:**
- Model training correctness (30%)
- Experiment comparison analysis (40%):
  - Compare at least 2 models or 2 parameter sets
  - In-depth analysis
  - Reasonable conclusions
- Experiment reproducibility (20%):
  - Complete configuration records
  - Traceable results
- Report format and expression (10%)

#### Week 6: LLM Application Project (25%)

**Evaluation Criteria:**
- Project completion (40%):
  - Complete end-to-end workflow
  - Functions run normally
  - Output results meet expectations
- Prompt design quality (20%):
  - Clear and effective prompts
  - Well-structured output
- Project presentation (20%):
  - Clear expression
  - Complete demonstration
  - Ability to answer questions
- Project reflection (20%):
  - Summary of learning gains
  - Identification of shortcomings
  - Proposal of improvement directions

#### Participation (20%)

**Evaluation Criteria:**
- Attendance rate (40%)
- Class discussion participation (30%)
- Peer evaluation quality (30%)

---

### Level 1: This Course (6 Weeks)

After completing this course, students will have:
- AI Agent tool usage capabilities
- AI-assisted programming learning abilities
- Python programming fundamentals
- Local inference and API calling capabilities
- Data processing fundamentals
- Machine learning basic concepts
- LLM application development capabilities

### Level 2: RAG and Agent Advanced (Recommended Follow-up Course)

**Prerequisites:**
- Completion of this course
- Mastery of Python programming fundamentals
- Familiarity with LLM API calls

**Level 2 Content Preview:**

#### Weeks 1-2: RAG Fundamentals
- Vector databases (Pinecone/Chroma)
- Embeddings and semantic search
- Retrieval strategies and reranking
- RAG system construction

#### Weeks 3-4: Agent System Design
- Tool use
- Planning and reasoning
- Multi-agent collaboration
- Agent frameworks (LangChain/AutoGPT)

#### Weeks 5-6: Production Deployment
- FastAPI service development
- Monitoring and logging
- Performance optimization
- Security considerations

#### Weeks 7-8: Advanced Topics
- Multimodal AI
- Fine-tuning methods
- Model optimization
- Capstone project

---

## Study Tips & FAQ

### Time Management

- **Weekly Investment:** At least 5 hours of class time + 3-5 hours of after-class practice
- **Practice First:** Implement concepts immediately after understanding them
- **Use AI Assistance:** Fully utilize Cursor, ChatGPT, and other tools to accelerate learning

### Study Methods

#### 1. Pre-Class Preparation
- Register required accounts in advance
- Install necessary software
- Browse materials for the upcoming week

#### 2. In-Class Participation
- Ask questions and participate in discussions actively
- Complete in-class exercises promptly
- Pair up with classmates for collaborative learning

#### 3. Post-Class Consolidation
- Review class content
- Complete homework assignments
- Read recommended materials

### Frequently Asked Questions

**Q: I have absolutely no programming experience. Can I still learn this?**  
**A:** Yes. The first two weeks of this course require no programming background. Through AI tool assistance, you can gradually learn Python through practice.

**Q: What can I learn in Weeks 1-2 without writing code?**  
**A:** Learning to use AI tools is a core skill. Even in technical roles, proficiency with AI tools is an important capability. The methodology established in these two weeks will run through the entire course.

**Q: Do I need to purchase ChatGPT Plus?**  
**A:** Not required. The free version of ChatGPT is sufficient for the course. Cursor has a free trial period that can be used during the course.

**Q: What if I can't keep up starting Week 3?**  
**A:** Provide timely feedback to the instructor, and we will offer additional tutoring. You can also use tools like Cursor to accelerate your learning of programming concepts.

**Q: Is the course project very difficult?**  
**A:** The Week 6 project is a simplified version with provided templates. The focus is on experiencing the end-to-end workflow rather than developing from scratch.

---

## Resources and Support

### Official Resources

- **Course Repository:** [GitHub Repository]
- **Issue Reporting:** [GitHub Issues]
- **Discussion Forum:** [Course Forum Link]

### Learning Resources

#### Official Documentation
- Python Official Tutorial
- Pandas Documentation
- OpenAI API Documentation
- Ollama Documentation

#### Recommended Reading
- "Python Crash Course" by Eric Matthes
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron
- Prompt Engineering Guide (promptingguide.ai)

### Getting Help

1. **In-Class Questions:** Make full use of class time to ask questions
2. **AI Assistance:** Use Cursor, ChatGPT, and other tools to answer questions
3. **Peer Learning:** Pair up with classmates and help each other
4. **Office Hours:** Fixed Q&A time each week

---

## Course Changelog

### v2.0 (2026-04-01)
- Compressed from 8 weeks to 6 weeks
- Added Week 1-2 Agent Tools Introduction content
- Lowered programming barrier, emphasizing AI-assisted learning
- Combined original Week 5 (Local Inference) and Week 4 (API Engineering) into new Week 3
- Combined original Week 3 (Prompt Engineering) and Week 6 (Project) into new Week 6
- Removed original Weeks 7-8, simplified Capstone project

### v1.0 (Original Version)
- 8-week course structure
- Traditional technical learning path
- Complete Capstone project workflow

---

## Course Team

- **Lead Instructor:** [Instructor Name]
- **Teaching Assistants:** [TA Names]
- **Course Design:** AI Engineering Education Team

### Contact Information

- **Email:** [Course Email]
- **WeChat Group:** [Course WeChat Group QR Code]
- **GitHub:** [Course Repository Link]

---

**Last Updated:** 2026-04-01  
**Version:** v2.0
