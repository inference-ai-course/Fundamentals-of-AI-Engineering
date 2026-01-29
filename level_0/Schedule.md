# 8-Week AI Engineering Course Schedule

## Overview
This schedule organizes the AI Engineering Starter Tutorial into 6 weeks of structured teaching followed by 2 weeks of project work to consolidate all knowledge points.

### Quick View Schedule

| Week | Theme | Key Topics | Learning Materials | Project Milestone |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Development Tools** | Shell, Git, SSH, Conda, Jupyter | [Chapter 1](./Chapters/1/Chapter1.md) | - |
| **2** | **Python Foundation** | Python Basics, Modules, Adv Environments | [Chapter 2](./Chapters/2/Chapter2.md) | - |
| **3** | **AI Fundamentals I** | Function Calling, Structured Outputs | [Chapter 3](./Chapters/3/Chapter3.md) (Part 1) | - |
| **4** | **AI Fundamentals II** | Prompt Engineering, Evaluation | [Chapter 3](./Chapters/3/Chapter3.md) (Part 2) | - |
| **5** | **Cloud Inference** | Model Interfaces, Hugging Face | [Chapter 3](./Chapters/3/Chapter3.md) (Part 3), [Chapter 4](./Chapters/4/Chapter4.md) (Part 1) | - |
| **6** | **Local Inference** | Ollama, vLLM, Resource Monitoring | [Chapter 4](./Chapters/4/Chapter4.md) (Parts 3-4), [Chapter 5](./Chapters/5/Chapter5.md) (Part 1) | **Proposal Start** |
| **7** | **Production** | Docker, Containerization | [Chapter 5](./Chapters/5/Chapter5.md) (Part 2) | Implementation |
| **8** | **Capstone** | Integration, Deployment, Demo | All Chapters | **Final Completion** |

---

## Week 1: Development Tools and Environment Setup
**Focus:** Mastering essential development tools and workflows

### Topics Covered:
- Shell/Command Line Fundamentals
- Git - Version Control and Collaboration  
- SSH - Secure Remote Development
- Conda - Environment and Package Management
- Jupyter - Interactive Computing

### Learning Materials:
- [Chapter 1: Tool Preparation](./Chapters/1/Chapter1.md)
- All hands-on practice labs in Chapter 1

### Key Outcomes:
- Set up professional development environment
- Navigate command-line interfaces confidently
- Manage code versions with Git
- Create isolated Python environments
- Run interactive notebooks with Jupyter

---

## Week 2: Python Fundamentals and Environment Management
**Focus:** Building strong Python foundations and professional environment management

### Topics Covered:
- Python Basics - Concepts (variables, data structures, control flow, functions)
- Python Basics - Interactive Exercises
- Conda Environment Management
- Advanced Environment Topics

### Learning Materials:
- [Chapter 2: Python and Environment Management](./Chapters/2/Chapter2.md)
- All hands-on practice sections in Chapter 2

### Key Outcomes:
- Write clean, idiomatic Python code
- Create and manage reproducible environments
- Debug code effectively
- Handle configuration and secrets securely

---

## Week 3: AI Engineering Fundamentals - Function Calling and Structured Outputs
**Focus:** Building reliable AI systems with structured responses

### Topics Covered:
- JSON Schema for structured responses
- Tool/function calling paradigms
- Cross-provider compatibility
- Validation and reliability techniques

### Learning Materials:
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md)
- Part 1: Function Calling and Structured Outputs

### Key Outcomes:
- Design reliable function calling systems
- Create structured output formats
- Ensure cross-platform compatibility
- Implement validation mechanisms

---

## Week 4: Prompt Engineering and Evaluation
**Focus:** Creating effective, consistent prompts for AI systems

### Topics Covered:
- System prompts and role design
- Few-shot learning patterns
- Guardrails against hallucinations
- Parameter tuning (temperature, top_p)
- Evaluation frameworks
- Production-ready prompt templates

### Learning Materials:
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md)
- Part 2: Prompt Engineering and Evaluation

### Key Outcomes:
- Design effective system prompts
- Implement few-shot learning patterns
- Prevent hallucinations and errors
- Create production-ready prompt templates
- Evaluate prompt performance systematically

---

## Week 5: Model Interfaces and Hugging Face Platform
**Focus:** Deploying AI models using cloud infrastructure

### Topics Covered:
- OpenAI-compatible interfaces
- HuggingFace Inference Providers
- Authentication and security best practices
- Provider selection and performance comparison
- Failover and timeout strategies

### Learning Materials:
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md)
- Part 3: Model Interfaces and Deployment
- [Chapter 4: Hugging Face Platform and Local Inference](./Chapters/4/Chapter4.md)
- Part 1: Hugging Face Platform

### Key Outcomes:
- Deploy models using various interfaces
- Implement authentication and security
- Select optimal inference providers
- Build robust deployment architectures

---

## Week 6: Local Inference and Resource Management
**Focus:** Running AI models locally and managing system resources

### Topics Covered:
- Local inference with Ollama and vLLM
- Performance optimization strategies
- Resource monitoring and troubleshooting
- GPU/CUDA compatibility
- Performance profiling and optimization

### Learning Materials:
- [Chapter 4: Hugging Face Platform and Local Inference](./Chapters/4/Chapter4.md)
- Part 2: Local Inference Endpoints
- [Chapter 5: Resource Monitoring and Containerization](./Chapters/5/Chapter5.md)
- Part 1: Resource Monitoring and Troubleshooting

### Key Outcomes:
- Run local inference with Ollama and vLLM
- Optimize model performance and cost
- Monitor and troubleshoot system resources
- Handle GPU/CUDA compatibility issues

### Project Start:
- Begin defining your Capstone Project
- Draft your project proposal
- Review [Week 8 Project Requirements](#week-8-capstone-project-demo)

---

## Week 7: Containerization and Production Deployment
**Focus:** Containerizing AI applications for production deployment

### Topics Covered:
- Docker fundamentals (images, containers, Dockerfile)
- Building custom images for AI/ML projects
- Multi-service orchestration with Docker Compose
- GPU support and CUDA configuration in containers
- Reproducible deployment workflows

### Learning Materials:
- [Chapter 5: Resource Monitoring and Containerization](./Chapters/5/Chapter5.md)
- Part 2: Dockerization

### Key Outcomes:
- Create production-ready Docker images
- Configure GPU support in containers
- Orchestrate multi-service applications
- Implement reproducible deployment workflows

---

## Week 8: Capstone Project Demo
**Focus:** Integrating all knowledge points into a comprehensive AI application

### Project Requirements:
Build a complete AI application that demonstrates mastery of all course concepts:

1. **Development Environment Setup**
   - Use proper version control (Git)
   - Create isolated environments (Conda)
   - Set up remote development (SSH)

2. **Python Implementation**
   - Clean, well-structured Python code
   - Proper error handling and debugging
   - Configuration management

3. **AI System Design**
   - Function calling with structured outputs
   - Effective prompt engineering
   - Model deployment (cloud and/or local)

4. **Production Considerations**
   - Containerization (Docker)
   - Resource monitoring
   - Security best practices

### Project Options (Choose One):
- **AI Assistant Application**: Build a conversational AI assistant with tool calling capabilities
- **Data Processing Pipeline**: Create an automated system for processing and analyzing data with AI
- **Model Deployment Service**: Build a service that deploys and manages multiple AI models
- **Custom Project**: Design your own AI application (must incorporate all core concepts)

### Deliverables:
- Complete source code with documentation
- Docker configuration for deployment
- README with setup and usage instructions
- Presentation/demo of the working application

### Assessment Criteria:
- **Technical Implementation** (40%): Correct use of all course concepts
- **Code Quality** (20%): Clean, maintainable, well-documented code
- **Innovation** (20%): Creative application of concepts
- **Presentation** (20%): Clear demonstration and explanation


## Success Tips

1. **Stay Consistent**: Complete each week's materials before moving forward
2. **Practice Hands-on**: All labs and exercises are essential for mastery
3. **Ask Questions**: Use community resources and documentation
4. **Build Incrementally**: Apply concepts as you learn them
5. **Focus on Quality**: Prioritize understanding over speed
