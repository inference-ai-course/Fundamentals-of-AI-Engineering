# Chapter 1: Development Tools and Environment Setup

## Overview

This chapter introduces the essential development tools and workflows for modern AI engineering and data science. You'll learn to use the command line, manage remote development environments, control code versions, and set up reproducible Python environments—all critical skills for professional AI development.

**Total Duration:** 6-8 hours  
**Prerequisites:** Basic computer literacy  

---

## Learning Objectives

By completing this chapter, you will be able to:

- ✅ Use command-line interfaces efficiently for development tasks
- ✅ Set up secure remote development workflows with SSH and VS Code
- ✅ Manage code versions and collaborate using Git
- ✅ Create isolated, reproducible Python environments with Conda
- ✅ Run interactive notebooks with Jupyter for experimentation
- ✅ Integrate all tools into a professional development workflow

---

## Chapter Structure

### Part 1: Shell and Command Line Fundamentals

**[📄 Read Documentation](./01_shell_command_line.md)**

Master the command-line interface for efficient development and automation.

**Key Topics:**
- Understanding shell, terminal, and CLI concepts
- Essential navigation and file operations
- Command structure, options, and arguments
- Wildcards, pipes, and redirection
- Environment variables and configuration
- Shell scripting basics for automation

**Hands-on Practice:**
- Navigate the file system efficiently
- Manage files and directories
- Use pipes and redirection
- Write simple automation scripts
- Customize your shell environment

**Platform Notes:**
- Linux/macOS: Native Bash/Zsh support
- Windows: Use WSL2, PowerShell, or Git Bash for Unix-like parity

---

### Part 2: Git - Version Control and Collaboration

**[📄 Read Documentation](./02_git_version_control.md)** | **[💻 Open Lab Notebook](./02_git_practice.ipynb)**

Learn to track code changes, collaborate with teams, and maintain project history.

**Key Topics:**
- Repository initialization and basic workflow
- Staging, committing, and pushing changes
- Branching and merging strategies
- VS Code Git integration
- GitHub/GitLab workflows

**Hands-on Practice:**
- Initialize your first repository
- Practice branching and merging
- Resolve merge conflicts
- Set up `.gitignore` files

---

### Part 3: SSH - Secure Remote Development

**[📄 Read Documentation](./03_ssh_remote_development.md)** | **[💻 Open Lab Notebook](./03_ssh_setup_lab.ipynb)**

Master secure remote access for development on cloud servers and HPC clusters.

**Key Topics:**
- SSH key generation (ed25519)
- SSH agent and key management
- Remote command execution
- VS Code Remote-SSH setup
- Port forwarding for Jupyter

**Hands-on Practice:**
- Generate SSH keys
- Configure SSH config file
- Connect to remote servers
- Set up VS Code Remote-SSH

---

### Part 4: Conda - Environment and Package Management

**[📄 Read Documentation](./04_conda_environment_management.md)** | **[💻 Open Lab Notebook](./04_conda_practice.ipynb)**

Create isolated, reproducible Python environments for different projects.

**Key Topics:**
- Environment creation and activation
- Package installation and management
- Environment export and sharing
- Channel configuration
- Best practices for reproducibility

**Hands-on Practice:**
- Create development environments
- Install packages with conda and pip
- Export and recreate environments
- Manage multiple Python versions

---

### Part 5: Jupyter - Interactive Computing

**[📄 Read Documentation](./05_jupyter_interactive_computing.md)** | **[💻 Open Lab Notebook](./05_jupyter_basics_lab.ipynb)**

Use Jupyter notebooks for interactive development, visualization, and documentation.

**Key Topics:**
- JupyterLab vs. Jupyter Notebook
- Kernel management and registration
- Remote Jupyter access
- Cell execution and markdown
- Magic commands and extensions

**Hands-on Practice:**
- Launch Jupyter locally and remotely
- Register conda environments as kernels
- Create interactive notebooks
- Access remote Jupyter via SSH tunneling

---

## Prerequisites

- **Operating System**: Linux, macOS, or Windows 10/11 (with WSL2)
- **Hardware**: Any modern computer with internet access
- **Skills**: Basic computer literacy (no programming required)
- **Accounts**: GitHub account (free) recommended

---

## Technology Requirements

This chapter prepares you for AI development with the following requirements:

- **Python**: 3.10 or higher
- **PyTorch**: 2.6.0 or higher (for later chapters)
- **CUDA**: 12.4 or higher (for GPU acceleration in later chapters)
- **Tools**: Git, SSH, Conda, VS Code, Jupyter

---

## Quick Start Guide

### For Complete Beginners
1. Start with the Shell and Command Line section
2. Progress through each part sequentially
3. Complete all hands-on practice sections
4. Finish with the comprehensive lab

### For Experienced Developers
1. Skim the Shell and Git sections if familiar
2. Focus on SSH and VS Code Remote-SSH setup
3. Deep dive into Conda best practices
4. Complete the comprehensive lab to verify setup

### For Reference
Use this chapter as a reference guide for:
- Common command-line operations
- Git workflows and commands
- Environment troubleshooting
- Tool configuration

---

## Getting Started

Choose your learning path:

- **New to command line?** Start with Shell fundamentals and work through each section
- **Know Git but new to remote development?** Jump to [SSH](03_ssh_remote_development.md) and [VS Code Remote setup](03_ssh_remote_development.md#vs-code-remote-ssh)
- **Python developer new to Conda?** Focus on [Conda Environment Management](04_conda_environment_management.md)
- **Ready for practice?** Go straight to the **Open Lab Notebook** links in each section above

---

## Assessment Checkpoints

By the end of this chapter, you should be able to:

- ✅ Navigate file systems using command-line tools
- ✅ Create and manage Git repositories
- ✅ Connect securely to remote servers via SSH
- ✅ Create isolated conda environments for projects
- ✅ Run Jupyter notebooks locally and remotely
- ✅ Integrate all tools in VS Code for seamless development

---

## Common Pitfalls & Tips

### Shell and Command Line
- ⚠️ **`rm -rf` is destructive**: Always double-check before removing files
- 💡 Use tab completion to avoid typos
- 💡 Check command syntax with `man <command>` or `<command> --help`

### Git
- ⚠️ **Never commit secrets**: Use `.gitignore` for credentials and API keys
- 💡 Write descriptive commit messages
- 💡 Pull before pushing to avoid conflicts

### SSH
- ⚠️ **Protect private keys**: Use passphrases and appropriate permissions (600)
- 💡 Use SSH config file for convenience
- 💡 Test connections with `ssh -vvv` for debugging

### Conda
- ⚠️ **Avoid installing in base**: Create separate environments for projects
- 💡 Export environments for reproducibility
- 💡 Use conda for large packages, pip for pure Python packages

### Jupyter
- ⚠️ **Port conflicts**: Check for existing Jupyter instances
- 💡 Register kernels for different environments
- 💡 Use meaningful notebook names

---

## Support and Resources

- Each section contains detailed examples and explanations
- Troubleshooting guides for common issues
- Links to official documentation
- Best practices from the AI/ML community

---

## Next Steps

After completing Chapter 1:
- **Chapter 2**: Python Programming and Advanced Environment Management
- **Chapter 3**: AI Engineering Fundamentals
- **Chapter 4**: Hugging Face Platform and Local Inference

**Ready to begin? Choose your starting point above and start your journey!**
