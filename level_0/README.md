# Fundamentals of AI Engineering

A comprehensive, hands-on tutorial series for learning AI engineering fundamentals, from development tools to production-ready AI systems. This course emphasizes practical skills using open-source tools and platforms.

## 📚 Course Overview

This tutorial is designed for developers who want to build production-ready AI applications. Each chapter combines theoretical concepts with hands-on coding exercises, real-world examples, and practical labs.

**Target Audience:**
- Software engineers transitioning to AI engineering
- Data scientists wanting to productionize AI models
- Developers building AI-powered applications
- Students learning modern AI development workflows

**Learning Approach:**
- 📖 Conceptual explanations with real-world context
- 💻 Interactive Jupyter notebooks with coding exercises
- 🔬 Hands-on labs with step-by-step implementations
- ✅ Assessment checkpoints to verify understanding
- ⚠️ Common pitfalls and troubleshooting guides

---

## 📖 Chapter Structure

### [Chapter 1: Tool Preparation](./Chapters/1/Chapter1.md)

**Focus:** Development environment setup and essential tools

Master the foundational tools for modern AI development workflows:
- **Shell/SSH**: Command-line operations and remote access
- **VS Code**: Remote development with SSH integration
- **Git**: Version control and collaboration
- **Conda**: Environment and package management
- **Jupyter**: Interactive computing for AI experimentation

**Key Outcomes:**
- Set up a complete development environment
- Connect to remote servers securely
- Navigate command-line interfaces confidently
- Manage code with Git version control

**Prerequisites:** Basic computer literacy, no prior programming experience required

---

### [Chapter 2: Python and Environment Management](./Chapters/2/Chapter2.md)

**Focus:** Python fundamentals and reproducible environments

Build a solid Python foundation and learn professional environment management:

**Part 1: Python Basics - Concepts**
- Variables, data structures, control flow
- Functions, modules, and packages
- File I/O and JSON processing
- Exception handling and debugging

**Part 2: Python Basics - Interactive Exercises**
- 20+ hands-on coding exercises
- Real-world programming scenarios
- Immediate feedback and testing

**Part 3: Conda Environment Management**
- Creating isolated Python environments
- Package installation and dependency management
- Environment files for reproducibility
- Best practices and troubleshooting

**Part 4: Advanced Environment Topics**
- Mixed Conda/Pip workflows
- Jupyter kernel integration
- Environment variables and secrets management
- Docker containerization basics

**Part 5: Hands-on Labs**
- JSON data processing project
- Production-ready environment setup
- Debugging practice scenarios
- Reproducible research workflows

**Key Outcomes:**
- Write clean, idiomatic Python code
- Create and manage reproducible environments
- Debug code effectively
- Handle configuration and secrets securely

**Prerequisites:** Chapter 1 completion recommended

---

### [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md)

**Focus:** Function calling, prompt engineering, and model interfaces

Learn to build reliable, production-ready AI systems:

**Part 1: Function Calling and Structured Outputs**
- JSON Schema for structured responses
- Tool/function calling paradigms
- Cross-provider compatibility
- Validation and reliability techniques

**Part 2: Prompt Engineering and Evaluation**
- System prompts and role design
- Few-shot learning patterns
- Guardrails against hallucinations
- Parameter tuning (temperature, top_p)
- Evaluation frameworks (LLM-as-judge, human-in-the-loop)
- Production-ready prompt templates

**Why Prompt Engineering Matters:**
- **Consistency**: Eliminate unpredictable outputs (40% fewer follow-ups)
- **Cost Efficiency**: Reduce token usage by 50%
- **Reliability**: Prevent hallucinations and errors
- **User Experience**: Deliver the right tone and format
- **Scalability**: Templates that work across thousands of requests

**Part 3: Model Interfaces and Deployment**
- OpenAI-compatible interfaces
- HuggingFace Inference Providers
- Local inference with Ollama and vLLM
- Performance optimization strategies
- Authentication and security best practices

**Key Outcomes:**
- Design reliable function calling systems
- Create production-ready prompts with measurable quality
- Deploy AI models using various interfaces
- Optimize performance and cost
- Build scalable AI applications

**Prerequisites:** Python proficiency (Chapter 2)

**Technology Stack:** Python 3.10+, PyTorch 2.6.0+, CUDA 12.4+

---

### [Chapter 4: Hugging Face Platform and Local Inference](./Chapters/4/Chapter4.md)

**Focus:** Cloud-based and local AI model deployment

Master both cloud and local inference strategies:

**Part 1: Hugging Face Platform (4 hours)**
- Inference API and provider selection
- Authentication and security
- OpenAI-compatible interfaces
- Provider performance comparison
- Failover and timeout strategies

**Part 2: Local Inference Endpoints (6 hours)**
- Ollama installation and operation
- vLLM deployment and configuration
- OpenAI-compatible local servers
- Performance benchmarking
- Memory and hardware optimization

**Key Outcomes:**
- Deploy models on Hugging Face infrastructure
- Run local inference with Ollama and vLLM
- Implement failover and error handling
- Compare cloud vs. local trade-offs
- Optimize throughput and latency

**Prerequisites:** Chapter 3 completion

**Hardware Requirements:**
- Minimum: 4+ cores, 16GB RAM, 8GB VRAM
- Recommended: 8+ cores, 32GB RAM, 16GB+ VRAM

---

### [Chapter 5: Resource Monitoring and Containerization](./Chapters/5/Chapter5.md)

**Focus:** Production monitoring, debugging, and Docker deployment

Learn essential production skills for deploying and maintaining AI systems:

**Part 1: Resource Monitoring and Troubleshooting (3-4 hours)**
- GPU, CPU, memory, and disk monitoring
- Common error patterns and diagnostics
- Authentication and port conflict resolution
- GPU/CUDA compatibility troubleshooting
- Performance profiling and optimization
- Effective logging and debugging strategies
- Timeout and retry mechanisms

**Part 2: Dockerization (5-6 hours)**
- Docker fundamentals (images, containers, Dockerfile)
- Building custom images for AI/ML projects
- Multi-service orchestration with Docker Compose
- GPU support and CUDA configuration in containers
- Best practices for containerizing PyTorch applications
- Reproducible deployment workflows

**Key Outcomes:**
- Monitor and optimize resource utilization in AI systems
- Diagnose and resolve production deployment issues
- Create production-ready Docker images for AI applications
- Configure GPU support in containerized environments
- Orchestrate multi-service AI applications
- Implement robust error handling and monitoring

**Prerequisites:** Chapter 3 and 4 completion recommended

**Additional Requirements:**
- Docker Desktop or Docker Engine installed
- nvidia-docker2 for GPU support (if using GPU)
- Basic understanding of networking and ports

---

## 🚀 Getting Started

### Quick Start Path

1. **Complete Chapter 1** - Set up your development environment
2. **Work through Chapter 2** - Master Python and environments
3. **Study Chapter 3** - Learn AI engineering fundamentals
4. **Deploy with Chapter 4** - Build production inference systems
5. **Master Chapter 5** - Production monitoring and containerization

### Alternative Learning Paths

**For Experienced Python Developers:**
- Skip Chapter 2 basics, review environment management only (2-3 hours)
- Focus on Chapters 3, 4, and 5 for AI-specific skills
- Estimated time: 32-40 hours

**For Quick Prototyping:**
- Chapter 1: Tool setup (3 hours)
- Chapter 3 Part 2: Prompt engineering (5-6 hours)
- Chapter 4 Part 1: Hugging Face deployment (4-5 hours)
- Estimated time: 12-14 hours

**For Production Deployment:**
- Complete all chapters sequentially
- Focus on labs, assessment checkpoints, and hands-on projects
- Extra time for experimentation and troubleshooting
- Estimated time: 55-70 hours with comprehensive practice

---

## 📅 Project Timeline

The course culminates in a capstone project that integrates all learned concepts. The project work begins in **Week 4** and concludes with a demo in **Week 8**.

### Project Start (Week 4)
- Complete your project proposal this week
- Begin planning your capstone AI application
- See [Week8](./Schedule.md#week-8-capstone-project-demo) for detailed requirements

### Capstone Project (Week 8)
Build a complete AI application that demonstrates mastery of all course concepts:
- Development Environment Setup with Git and Conda
- Clean Python implementation with proper error handling
- AI System Design with function calling and prompt engineering
- Model deployment (cloud and/or local)
- Production considerations including containerization and monitoring

---

## 💻 Technology Stack

### Core Technologies
- **Python**: 3.10 or higher
- **PyTorch**: 2.6.0 or higher
- **CUDA**: 12.4 or higher (for GPU acceleration)

### Key Libraries
- `transformers` - Hugging Face model library
- `huggingface_hub` - Model and dataset access
- `openai` - OpenAI-compatible client
- `requests` - HTTP client for APIs

### Development Tools
- **VS Code** - Primary IDE with remote development
- **Jupyter** - Interactive notebooks for experimentation
- **Git** - Version control
- **Conda** - Environment management
- **Docker** - Containerization (optional)

### Platforms
- **Hugging Face** - Model hosting and inference
- **Ollama** - Local model serving
- **vLLM** - High-performance inference engine

---

## 📋 Prerequisites

### Required
- Basic computer literacy
- Ability to follow technical instructions
- Willingness to learn command-line tools

### Helpful (Not Required)
- Programming experience in any language
- Basic understanding of machine learning concepts
- Familiarity with cloud services

### Hardware
- **Minimum**: Modern laptop/desktop, 16GB RAM, stable internet
- **Recommended**: GPU with 8GB+ VRAM for local inference
- **Optimal**: GPU with 16GB+ VRAM, 32GB+ RAM, SSD storage

---

## 🎯 Learning Outcomes

By completing this tutorial series, you will be able to:

1. **Set up professional development environments** for AI engineering
2. **Write production-quality Python code** with proper error handling
3. **Design reliable AI systems** using function calling and structured outputs
4. **Engineer effective prompts** that deliver consistent, high-quality results
5. **Evaluate and optimize** AI model performance systematically
6. **Deploy AI models** using cloud and local infrastructure
7. **Build scalable applications** with proper authentication and monitoring
8. **Monitor and optimize** resource utilization in production systems
9. **Containerize AI applications** for reproducible deployments
10. **Troubleshoot and debug** common issues in AI development workflows

---

## 📚 Additional Resources

### Documentation
- [Hugging Face Documentation](https://huggingface.co/docs)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)

### Community
- [Hugging Face Forums](https://discuss.huggingface.co/)
- [PyTorch Forums](https://discuss.pytorch.org/)
- [Stack Overflow - AI/ML Tags](https://stackoverflow.com/questions/tagged/machine-learning)

### Best Practices
- Each chapter includes troubleshooting guides
- Common pitfalls are highlighted throughout
- Assessment checkpoints verify understanding
- Real-world examples demonstrate practical applications

---

## 🤝 Contributing

This is an educational resource focused on practical AI engineering skills. Feedback and suggestions are welcome through:
- Issue reports for errors or unclear content
- Pull requests for improvements
- Suggestions for additional topics or examples

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Philosophy

This tutorial emphasizes:
- **Open-source first**: Using accessible, community-driven tools
- **Production-ready**: Real-world patterns, not toy examples
- **Hands-on learning**: Code along, experiment, and build
- **Best practices**: Security, reproducibility, and maintainability
- **Practical focus**: Skills you'll use in actual AI engineering work

**Ready to start?** Begin with [Chapter 1: Tool Preparation](./Chapters/1/Chapter1.md) and build your AI engineering foundation!
