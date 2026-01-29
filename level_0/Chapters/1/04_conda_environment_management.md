# Conda: Environments and Packages

## Overview

Conda is a powerful package manager and environment manager that helps you create isolated Python environments with specific package versions, preventing conflicts between different projects.

---

## Key Features

- **Environment Management**: Create isolated spaces for different projects
- **Package Management**: Install, update, and remove packages easily
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Language Agnostic**: Supports Python, R, and other languages
- **Dependency Resolution**: Automatically handles package dependencies

---

## Installation Guide

### Check Existing Installation
```bash
conda info
```

If conda is not installed, follow the steps below.

### Fresh Miniconda Installation

#### Step 1: Download Installer
Visit [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html) and download the appropriate installer for your system.

#### Step 2: Run Installation
```bash
# For Linux/macOS
bash Miniconda3-latest-MacOSX-x86_64.sh

# For Windows
# Run the downloaded .exe installer
```

#### Step 3: Complete Setup
- Accept the license agreement
- Allow the installer to run
- **Important**: Allow conda init when prompted to configure your shell

#### Step 4: Verify Installation
```bash
conda info
```
This should show environment and channel details.

---

## Suggested Practice Flow

### After Lab Completion

1. **Create Project Environment**
   ```bash
   conda create -n myproject python=3.12
   conda activate myproject
   ```

2. **Install Essential Packages**
   ```bash
   # Install common data science packages
   # JupyterLab: https://jupyterlab.readthedocs.io/
   # NumPy: https://numpy.org/doc/
   # Pandas: https://pandas.pydata.org/docs/
   # Matplotlib: https://matplotlib.org/stable/contents.html
   conda install jupyterlab numpy pandas matplotlib
   # or use pip if packages aren't available in conda
   pip install package_name
   ```

3. **Launch Jupyter**
   - **Locally**: `jupyter lab`
   - **Remote**: Run in terminal and use VS Code port forwarding to access UI

4. **Set Up Version Control**
   ```bash
   # Initialize Git repository
   git init
   
   # Make small changes, stage/commit in VS Code Source Control
   # Push to GitHub (after adding SSH key)
   ```

---

## Best Practices

### Environment Management
- Create separate environments for different projects
- Name environments descriptively (e.g., `data-science`, `web-dev`)
- Keep environment files (`environment.yml`) for reproducibility

### Package Installation
- Use conda first, then pip if package not available
- Pin important package versions in requirements files
- Regularly update conda and base packages

### Common Commands
```bash
# Environment operations
conda create -n env_name python=3.12
conda activate env_name
conda deactivate
conda env list

# Package operations
conda install package_name
conda update package_name
conda remove package_name
conda list

# Environment export/import
conda env export > environment.yml
conda env create -f environment.yml
```

---

## Troubleshooting

### Common Issues
- **Package Not Found**: Try `conda-forge` channel or use pip
- **Environment Conflicts**: Create fresh environment with specific versions
- **Permission Errors**: Avoid installing in base environment
- **Slow Performance**: Use `mamba` (faster conda alternative)

### Performance Tips
- Use `mamba` for faster dependency resolution
- Keep base environment minimal
- Regularly clean unused packages and caches
