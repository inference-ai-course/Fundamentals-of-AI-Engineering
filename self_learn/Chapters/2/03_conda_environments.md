# Part 3: Conda Environment Management

## Overview

Imagine training a model that works perfectly on your laptop, but crashes on your colleague's machine. Or a paper's results you can't reproduce six months later because package versions changed. **This is the environment management problem**, and Conda solves it elegantly.

This section teaches you professional environment management—the skill that separates hobbyists from engineers.

---

## Why Environment Management is Critical

### The "Works On My Machine" Problem

**The nightmare scenario:**
```
Researcher A (6 months ago):
- Python 3.9
- NumPy 1.21
- TensorFlow 2.8
- Training accuracy: 94.5%
→ Writes paper, graduates

Researcher B (today):
- Python 3.11
- NumPy 1.26  
- TensorFlow 2.15
- Training accuracy: 82.3%
→ Can't reproduce results!
```

**What went wrong?**
- API changes between versions
- Different default random seeds
- Numerical precision differences
- Dependency conflicts

### How Conda Solves This

**Conda provides:**

1. **Isolation**: Each project has its own environment
   ```
   Project A → Python 3.9 + TensorFlow 2.8
   Project B → Python 3.11 + PyTorch 2.0
   → No conflicts!
   ```

2. **Reproducibility**: Exact environment recreation
   ```
   environment.yml → Create identical env anywhere
   → Same code, same packages, same results
   ```

3. **Binary Packages**: Pre-compiled packages install fast
   ```
   pip install numpy → Compiles from source (minutes)
   conda install numpy → Pre-built binary (seconds)
   ```

4. **Dependency Resolution**: Smart package management
   ```
   Conda checks all dependencies before installing
   → Prevents "dependency hell"
   ```

**In AI/ML context:**
- Experiment tracking with consistent environments
- Team collaboration without setup headaches
- Deployment with frozen dependencies
- Research reproducibility for papers

---

## Table of Contents
1. [Environment Basics](#environment-basics)
2. [Creating and Managing Environments](#creating-and-managing-environments)
3. [Package Management](#package-management)
4. [Environment Configuration](#environment-configuration)
5. [Best Practices](#best-practices)
6. [Practical Exercises](#practical-exercises)

---

## Environment Basics

### What are Conda Environments?

A Conda environment is an **isolated directory** containing a specific Python version and a set of packages. Think of it as a self-contained universe for your project.

**Conceptual Model:**

```
Your Computer
│
├── Base Environment (system Python)
│   ├── Python 3.11
│   └── Minimal packages
│
├── Environment: ml-project
│   ├── Python 3.10
│   ├── NumPy 1.24
│   ├── Pandas 2.0
│   └── Scikit-learn 1.3
│
├── Environment: nlp-research
│   ├── Python 3.9
│   ├── Transformers 4.40
│   └── PyTorch 2.0
│
└── Environment: legacy-code
    ├── Python 3.7
    └── Old packages
```

Each environment is **completely independent**—changes in one don't affect others.

### How Environments Work Internally

**Directory structure:**
```
~/miniconda3/envs/my-env/
├── bin/                    # Executables (python, pip, etc.)
├── lib/                    # Python libraries
│   └── python3.10/
│       └── site-packages/  # Installed packages
├── include/                # C headers
└── share/                  # Shared data
```

**When you activate an environment:**
```bash
$ conda activate my-env

# Python changes your PATH:
# Before: /usr/bin/python  → system Python
# After:  ~/miniconda3/envs/my-env/bin/python  → env Python
```

**This means:**
- `python` command now points to environment's Python
- `pip` installs to environment's site-packages
- Imports search environment's libraries first
- Complete isolation from system and other environments

### Problems Conda Solves

1. **Dependency Hell**
   ```
   Package A requires NumPy >= 1.20
   Package B requires NumPy < 1.22
   Package C requires NumPy == 1.19
   → Impossible to satisfy all constraints!
   
   Solution: Different environments for different projects
   ```

2. **Version Conflicts**
   ```
   Old project needs Python 3.7
   New project needs Python 3.11
   → Can't have both in same environment
   
   Solution: One environment per project
   ```

3. **Reproducibility**
   ```
   "Works on my machine" syndrome
   → Different package versions = different results
   
   Solution: environment.yml specifies exact versions
   ```

4. **Team Collaboration**
   ```
   Teammate can't run your code
   → Missing packages or wrong versions
   
   Solution: Share environment.yml, identical setup
   ```

---

### Why Use Conda for AI Engineering?

- **Package Availability**: Access to scientific computing packages (NumPy, Pandas, SciPy)
- **Binary Packages**: Pre-compiled packages that install quickly
- **Cross-Platform**: Works consistently on Windows, macOS, and Linux
- **Environment Management**: Superior dependency resolution compared to pip alone

---

## Creating and Managing Environments

### Basic Environment Operations

```bash
# Create a new environment with Python 3.10
conda create -n llm-env python=3.10

# Create environment with multiple packages
conda create -n data-science python=3.10 numpy pandas matplotlib

# Create environment from file (we'll cover this later)
conda env create -f environment.yml

# Activate the environment
conda activate llm-env

# Deactivate current environment
conda deactivate

# List all environments
conda env list
# or
conda info --envs

# Remove an environment
conda remove --name llm-env --all

# Export current environment
conda env export --name llm-env > environment.yml
```

### Environment Naming Conventions

```bash
# Good naming examples
conda create -n ai-project-2024 python=3.10
conda create -n tensorflow-gpu python=3.9
conda create -n data-analysis python=3.10

# Avoid these naming patterns
conda create -n test python=3.10          # Too generic
conda create -n myenv python=3.10         # Not descriptive
conda create -n 2024-project python=3.10  # Starts with number
```

### Environment Locations

```bash
# Check where environments are stored
conda info

# Typical locations:
# Linux/macOS: ~/miniconda3/envs/ or ~/anaconda3/envs/
# Windows: C:\Users\username\Miniconda3\envs\

# Find specific environment path
conda env list --json | python -c "import json, sys; data = json.load(sys.stdin); print([env for env in data['envs'] if 'llm-env' in env])"
```

---

## Package Management

### Installing Packages

```bash
# Install packages from conda-forge (recommended)
conda install -c conda-forge numpy pandas matplotlib

# Install specific versions
conda install -c conda-forge numpy=1.24 pandas=2.0 matplotlib=3.7

# Install multiple packages at once
conda install -c conda-forge numpy pandas matplotlib scikit-learn jupyter

# Update packages
conda update numpy

# Update all packages in environment
conda update --all

# Search for packages
conda search pandas

# Check package information
conda info pandas
```

### Channel Management

```bash
# Configure channel priority
conda config --add channels conda-forge
conda config --set channel_priority strict

# Check current channel configuration
conda config --show channels

# Install from specific channel
conda install -c bioconda biopython

# Temporarily use different channel
conda install -c defaults numpy
```

### Common AI/ML Packages

```bash
# Core scientific computing
conda install -c conda-forge numpy pandas matplotlib seaborn

# Machine learning
conda install -c conda-forge scikit-learn xgboost lightgbm

# Deep learning frameworks
conda install -c conda-forge tensorflow pytorch torchvision

# Jupyter ecosystem
conda install -c conda-forge jupyter jupyterlab notebook

# Data processing
conda install -c conda-forge scipy statsmodels

# Computer vision
conda install -c conda-forge opencv pillow

# Natural language processing
conda install -c conda-forge nltk spacy
```

---

## Environment Configuration

### Creating environment.yml Files

Create a file named `environment.yml`:
```yaml
name: llm-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.24
  - pandas=2.0
  - matplotlib=3.7
  - scikit-learn=1.3
  - jupyter=1.0
  - ipykernel=6.0
  - pip
  - pip:
    - transformers>=4.40
    - huggingface_hub>=0.22
    - openai>=1.0
```

### Advanced environment.yml Configuration

```yaml
name: ai-research-env
channels:
  - conda-forge
  - pytorch
  - nvidia
  - defaults

dependencies:
  # Python version
  - python=3.10
  
  # Core scientific computing
  - numpy=1.24
  - pandas=2.0
  - matplotlib=3.7
  - seaborn=0.12
  - scipy=1.10
  
  # Machine learning
  - scikit-learn=1.3
  - xgboost=1.7
  - lightgbm=3.3
  
  # Deep learning
  - pytorch=2.0
  - torchvision=0.15
  - cpuonly  # Remove this line for GPU support
  
  # Jupyter ecosystem
  - jupyter=1.0
  - jupyterlab=4.0
  - notebook=6.5
  - ipywidgets=8.0
  
  # Development tools
  - black=23.0
  - flake8=6.0
  - pytest=7.4
  
  # System utilities
  - tqdm=4.65
  - pyyaml=6.0
  - requests=2.31
  
  # Pip dependencies
  - pip
  - pip:
    - transformers>=4.40
    - huggingface_hub>=0.22
    - datasets>=2.14
    - evaluate>=0.4
    - accelerate>=0.20
    - wandb>=0.15
    - tensorboard>=2.13
```

### Environment Variables and Activation Scripts

Create activation scripts that set environment variables:

```bash
# Create activation script
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
mkdir -p $CONDA_PREFIX/etc/conda/deactivate.d

# Create activate script
cat > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh << 'EOF'
#!/bin/bash
export HF_TOKEN="your_huggingface_token_here"
export OPENAI_API_KEY="your_openai_key_here"
export PYTHONPATH="${CONDA_PREFIX}/lib/python3.10/site-packages:${PYTHONPATH}"
echo "Environment variables set for AI development"
EOF

# Create deactivate script
cat > $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh << 'EOF'
#!/bin/bash
unset HF_TOKEN
unset OPENAI_API_KEY
unset PYTHONPATH
echo "Environment variables cleaned up"
EOF

# Make scripts executable
chmod +x $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
chmod +x $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
```

---

## Best Practices

### Environment Management Best Practices

1. **Use descriptive names**: `ai-project-2024` instead of `env1`
2. **Pin Python version**: Always specify `python=3.x` in environment files
3. **Prefer conda-forge**: Use `-c conda-forge` for better package availability
4. **Document dependencies**: Include comments in environment.yml files
5. **Version control**: Commit environment.yml files to your repository
6. **Regular updates**: Update packages periodically but test thoroughly

### Channel Priority Configuration

```bash
# Set up optimal channel configuration
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels defaults
conda config --set channel_priority strict

# Verify configuration
conda config --show channels
```

### Mixed Conda/Pip Usage

When you need packages not available in conda:

```bash
# Install conda packages first
conda install -c conda-forge numpy pandas scikit-learn

# Then install pip packages
pip install transformers huggingface_hub

# Never upgrade pip packages that conda manages
# ❌ Don't do this: pip install --upgrade numpy
# ✅ Do this instead: conda update numpy
```

### Environment Backup and Sharing

```bash
# Export exact environment (including builds)
conda env export --name myenv > environment.yml

# Export without builds (more portable)
conda env export --name myenv --no-builds > environment.yml

# Export only explicitly installed packages
conda env export --name myenv --from-history > environment.yml

# Create from exported file
conda env create -f environment.yml

# Update existing environment from file
conda env update -f environment.yml --prune
```

---

## Practical Exercises

### Exercise 1: Create Your First AI Environment

```bash
# Create a basic AI development environment
conda create -n ai-basics python=3.10 numpy pandas matplotlib jupyter

# Activate the environment
conda activate ai-basics

# Install additional packages
conda install -c conda-forge scikit-learn seaborn

# Test the installation
python -c "import numpy, pandas, matplotlib, sklearn; print('All packages imported successfully!')"

# Create a simple test script
cat > test_environment.py << 'EOF'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create DataFrame
df = pd.DataFrame({'x': x, 'y': y})

# Simple plot
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'])
plt.title('Sine Wave Test')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('test_plot.png')
print("Plot saved as test_plot.png")
EOF

# Run the test script
python test_environment.py
```

### Exercise 2: Create and Share an Environment

Create a file named `ai-research-env.yml`:
```yaml
name: ai-research-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.24
  - pandas=2.0
  - matplotlib=3.7
  - scikit-learn=1.3
  - jupyter=1.0
  - pip
  - pip:
    - transformers>=4.40
    - huggingface_hub>=0.22
```

Create the environment from file:
```bash
# Create environment from YAML file
conda env create -f ai-research-env.yml

# Activate the environment
conda activate ai-research-env

# Test with a simple NLP example
python -c "
from transformers import pipeline
import huggingface_hub

# Test sentiment analysis
classifier = pipeline('sentiment-analysis')
result = classifier('I love using Conda environments!')[0]
print(f'Sentiment: {result[\"label\"]}, Confidence: {result[\"score\"]:.3f}')
"
```

### Exercise 3: Environment with Custom Activation Scripts

```bash
# Create a new environment
conda create -n secure-ai python=3.10 numpy pandas

# Activate the environment
conda activate secure-ai

# Create activation script for API keys
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
mkdir -p $CONDA_PREFIX/etc/conda/deactivate.d

# Create secure activation script
cat > $CONDA_PREFIX/etc/conda/activate.d/secure_vars.sh << 'EOF'
#!/bin/bash
# This script sets up secure environment variables

# Check if .env file exists in current directory
if [ -f ".env" ]; then
    echo "Loading environment variables from .env file"
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "No .env file found. Please create one with your API keys."
    echo "Example .env file contents:"
    echo "HF_TOKEN=your_huggingface_token"
    echo "OPENAI_API_KEY=your_openai_key"
fi

# Set secure permissions for Python
export PYTHONHASHSEED=random
export PYTHONDONTWRITEBYTECODE=1
EOF

# Create deactivation script
cat > $CONDA_PREFIX/etc/conda/deactivate.d/secure_vars.sh << 'EOF'
#!/bin/bash
# Clean up environment variables

# Unset API keys
unset HF_TOKEN
unset OPENAI_API_KEY
unset OPENAI_API_BASE
unset PYTHONHASHSEED
unset PYTHONDONTWRITEBYTECODE

echo "Environment variables cleaned up"
EOF

# Make scripts executable
chmod +x $CONDA_PREFIX/etc/conda/activate.d/secure_vars.sh
chmod +x $CONDA_PREFIX/etc/conda/deactivate.d/secure_vars.sh

# Test the setup
conda deactivate
conda activate secure-ai
```

### Exercise 4: Troubleshooting Environment Issues

```bash
# Common troubleshooting scenarios

# 1. Environment won't activate
conda activate nonexistent-env
# Error: Could not find conda environment: nonexistent-env

# 2. Package conflicts
conda create -n conflict-test python=3.10
conda activate conflict-test
# This might cause conflicts:
# conda install -c conda-forge numpy=1.20
# conda install -c defaults numpy=1.24

# 3. Check for conflicts
conda install -c conda-forge numpy=1.24 --dry-run

# 4. Clean conda cache
conda clean --all

# 5. Reset conda configuration
conda config --remove-key channels
conda config --add channels defaults
conda config --add channels conda-forge

# 6. Debug package resolution
conda install -c conda-forge some-package --debug
```

---

## Summary

In this section, you learned:

- **Environment Management**: Create, activate, and remove conda environments
- **Package Installation**: Install and manage packages from different channels
- **Configuration**: Create environment.yml files for reproducible setups
- **Best Practices**: Follow conventions for naming, channel priority, and mixed usage
- **Troubleshooting**: Handle common environment issues and conflicts

## Next Steps

Now you're ready to move on to [Part 5: Advanced Environment Topics](./05_advanced_environments.md), where you'll learn:

- Advanced pip and conda integration
- Jupyter kernel management
- Environment variable security
- Docker containerization

## Additional Resources

- [Conda Documentation](https://docs.conda.io/)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Conda-forge Package Search](https://anaconda.org/conda-forge)
- [Python Packaging Authority](https://packaging.python.org/)

**Practice these concepts by creating environments for your own projects!**
