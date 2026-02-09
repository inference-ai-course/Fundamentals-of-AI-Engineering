# Part 4: Advanced Environment Topics

## Overview

You've mastered basic environment management. Now it's time for the advanced techniques that professionals use in production: mixing package managers safely, integrating with Jupyter, securing API keys, and containerizing with Docker.

These aren't just "nice to have" skills—they're essential for:
- Production ML deployments
- Team collaboration at scale  
- Secure handling of credentials
- Reproducible research infrastructure

---

## Why Advanced Environment Management?

### The Production Gap

**Research environment (your laptop):**
```
conda activate my-env
jupyter notebook
→ Quick experiments, rapid iteration
```

**Production environment (cloud/server):**
```
- No conda installed
- No root access
- Security restrictions
- Must run in containers
- API keys must be secure
- Multiple services coordinating
→ Need Docker, proper secrets management
```

**This section bridges that gap.**

### Real-World Scenarios

1. **Mixed Package Management**
   - Some packages only on PyPI (pip)
   - Some only on conda-forge
   - Need both without breaking things

2. **Jupyter at Scale**
   - Multiple kernels for different projects
   - Remote Jupyter servers
   - Team shared environments

3. **Secrets Management**
   - API keys (OpenAI, HuggingFace)
   - Database credentials
   - OAuth tokens
   - Need secure, versioned storage

4. **Containerization**
   - Reproducible across platforms
   - Isolated from host system
   - Deploy to cloud/Kubernetes
   - Version control entire stack

---

## Table of Contents
1. [Mixed Conda/Pip Usage](#mixed-conda-pip-usage)
2. [Jupyter Integration](#jupyter-integration)
3. [Environment Variables and Security](#environment-variables-and-security)
4. [Docker Containerization](#docker-containerization)
5. [Performance Optimization](#performance-optimization)
6. [Practical Exercises](#practical-exercises)

---

## Mixed Conda/Pip Usage

### When to Use Mixed Package Managers

```bash
# Use Conda when:
# - Package is available in conda-forge
# - You need binary packages (faster installation)
# - Working with scientific computing libraries

# Use pip when:
# - Package is not available in conda
# - You need the latest version
# - Working with pure Python packages
```

### Best Practices for Mixed Usage

```bash
# 1. Create base environment with conda
conda create -n mixed-env python=3.10
conda activate mixed-env

# 2. Install conda packages first
conda install -c conda-forge numpy pandas matplotlib scikit-learn

# 3. Install pip packages that aren't in conda
pip install transformers huggingface_hub openai

# 4. Document what came from where
echo "# Environment Sources" > package_sources.txt
echo "## Conda Packages:" >> package_sources.txt
conda list >> package_sources.txt
echo "## Pip Packages:" >> package_sources.txt
pip list >> package_sources.txt
```

### Avoiding Conflicts

```bash
# Create a constraint file to prevent conflicts
cat > constraints.txt << 'EOF'
# Prevent pip from upgrading conda-managed packages
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
EOF

# Install pip packages with constraints
pip install -c constraints.txt some-package

# Or use --no-deps to avoid dependency resolution
pip install --no-deps package-name
```

### Creating Hybrid environment.yml Files

```yaml
name: hybrid-ai-env
channels:
  - conda-forge
  - nvidia
  - defaults

dependencies:
  # Core packages from conda
  - python=3.10
  - numpy=1.24
  - pandas=2.0
  - matplotlib=3.7
  - scikit-learn=1.3
  - pytorch=2.6.0
  - torchvision=0.21.0
  - pytorch-cuda=12.4
  
  # Jupyter ecosystem
  - jupyter=1.0
  - jupyterlab=4.0
  - ipykernel=6.0
  
  # Development tools
  - black=23.0
  - pytest=7.4
  
  # Pip for packages not in conda
  - pip
  
  # Pip packages
  - pip:
    - transformers>=4.40
    - huggingface_hub>=0.22
    - datasets>=2.14
    - evaluate>=0.4
    - accelerate>=0.20
    - wandb>=0.15
    - openai>=1.0
    - tiktoken>=0.5
```

---

## Jupyter Integration

### Registering Kernels

```bash
# Install ipykernel in your environment
conda install -c conda-forge ipykernel

# Register kernel for Jupyter
python -m ipykernel install --user --name hybrid-ai-env --display-name "Python (AI Environment)"

# List available kernels
jupyter kernelspec list

# Remove a kernel
jupyter kernelspec uninstall hybrid-ai-env
```

### Multiple Kernel Management

```python
# Create a script to manage multiple kernels
# save as manage_kernels.py
import subprocess
import json

def list_kernels():
    """List all Jupyter kernels."""
    result = subprocess.run(['jupyter', 'kernelspec', 'list', '--json'], 
                          capture_output=True, text=True)
    return json.loads(result.stdout)

def install_kernel(env_name, display_name=None):
    """Install a kernel for a conda environment."""
    if display_name is None:
        display_name = f"Python ({env_name})"
    
    subprocess.run([
        'conda', 'run', '-n', env_name,
        'python', '-m', 'ipykernel', 'install',
        '--user', '--name', env_name,
        '--display-name', display_name
    ])

def remove_kernel(kernel_name):
    """Remove a Jupyter kernel."""
    subprocess.run(['jupyter', 'kernelspec', 'remove', '-f', kernel_name])

# Example usage
if __name__ == "__main__":
    kernels = list_kernels()
    print("Available kernels:")
    for kernel, path in kernels['kernelspecs'].items():
        print(f"  {kernel}: {path}")
```

### JupyterLab Extensions

```bash
# Install JupyterLab with extensions
conda install -c conda-forge jupyterlab

# Useful extensions for AI development
conda install -c conda-forge jupyterlab-git
pip install jupyterlab-system-monitor
pip install jupyterlab-lsp
conda install -c conda-forge python-lsp-server

# Enable extensions
jupyter server extension enable jupyterlab_git
jupyter server extension enable jupyterlab_system_monitor
```

### Custom Jupyter Configuration

Create `~/.jupyter/jupyter_lab_config.py`:
```python
c = get_config()

# Server configuration
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.allow_root = True

# Security
c.ServerApp.token = ''
c.ServerApp.password = ''

# Kernel configuration
c.KernelManager.autorestart = True
c.KernelManager.cull_idle_timeout = 3600  # 1 hour
c.KernelManager.cull_interval = 300      # 5 minutes

# Resource limits
c.ResourceUseDisplay.track_cpu_percent = True
c.ResourceUseDisplay.cpu_limit = 2.0
c.ResourceUseDisplay.mem_limit = 8589934592  # 8GB in bytes

# Extension settings
c.GitCommitPush.git_dir = '.'
```

---

## Environment Variables and Security

### Secure Environment Variable Management

Create a `.env` file in your project directory:
```
# .env
HF_TOKEN=your_huggingface_token_here
OPENAI_API_KEY=your_openai_key_here
DATABASE_URL=your_database_url_here
API_BASE_URL=https://api.example.com
```

Load environment variables securely:
```python
# load_env.py
import os
import warnings
from pathlib import Path
from typing import Optional

class EnvironmentManager:
    def __init__(self, env_file: str = ".env"):
        self.env_file = Path(env_file)
        self.load_env_file()
    
    def load_env_file(self):
        """Load environment variables from .env file."""
        if not self.env_file.exists():
            warnings.warn(f"No {self.env_file} file found. Some features may not work.")
            return
        
        with open(self.env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value
    
    def get_env_var(self, key: str, default: Optional[str] = None) -> str:
        """Get environment variable with optional default."""
        value = os.environ.get(key, default)
        if value is None:
            raise ValueError(f"Environment variable {key} not found and no default provided")
        return value
    
    def validate_required_vars(self, required_vars: list) -> bool:
        """Validate that all required environment variables are set."""
        missing_vars = []
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {missing_vars}")
        return True

# Usage
env_manager = EnvironmentManager()
try:
    env_manager.validate_required_vars(['HF_TOKEN', 'OPENAI_API_KEY'])
    hf_token = env_manager.get_env_var('HF_TOKEN')
    openai_key = env_manager.get_env_var('OPENAI_API_KEY')
    print("Environment variables loaded successfully!")
except ValueError as e:
    print(f"Environment error: {e}")
```

### Secure API Key Storage

```python
# secure_storage.py
import os
import json
import getpass
from pathlib import Path
from cryptography.fernet import Fernet
import base64

class SecureStorage:
    def __init__(self, storage_file: str = ".secure_keys"):
        self.storage_file = Path(storage_file)
        self.key_file = Path(".encryption_key")
        self.cipher = self._get_cipher()
    
    def _get_cipher(self):
        """Get or create encryption cipher."""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            # Set restrictive permissions
            os.chmod(self.key_file, 0o600)
        
        return Fernet(key)
    
    def store_key(self, name: str, value: str):
        """Securely store an API key."""
        encrypted_value = self.cipher.encrypt(value.encode())
        
        # Load existing keys
        keys = {}
        if self.storage_file.exists():
            with open(self.storage_file, 'rb') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self.cipher.decrypt(encrypted_data)
                    keys = json.loads(decrypted_data.decode())
        
        # Add new key
        keys[name] = base64.b64encode(encrypted_value).decode()
        
        # Save encrypted data
        data = json.dumps(keys).encode()
        encrypted_data = self.cipher.encrypt(data)
        
        with open(self.storage_file, 'wb') as f:
            f.write(encrypted_data)
        
        # Set restrictive permissions
        os.chmod(self.storage_file, 0o600)
    
    def get_key(self, name: str) -> str:
        """Retrieve a stored API key."""
        if not self.storage_file.exists():
            raise KeyError(f"No stored keys found")
        
        with open(self.storage_file, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
            keys = json.loads(decrypted_data.decode())
        
        if name not in keys:
            raise KeyError(f"Key '{name}' not found")
        
        encrypted_value = base64.b64decode(keys[name])
        return self.cipher.decrypt(encrypted_value).decode()

# Usage
storage = SecureStorage()

# Store keys securely
storage.store_key('hf_token', 'your_huggingface_token')
storage.store_key('openai_key', 'your_openai_key')

# Retrieve keys
hf_token = storage.get_key('hf_token')
openai_key = storage.get_key('openai_key')
```

---

## Docker Containerization

### Basic Dockerfile for AI Environment

Create a `Dockerfile`:
```dockerfile
# Use official Python runtime with CUDA support
FROM nvidia/cuda:12.4-devel-ubuntu22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh
ENV PATH="/opt/conda/bin:${PATH}"

# Create working directory
WORKDIR /app

# Copy environment file
COPY environment.yml .

# Create conda environment
RUN conda env create -f environment.yml && \
    conda clean -afy

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "ai-env", "/bin/bash", "-c"]

# Copy application code
COPY . .

# Expose port for Jupyter
EXPOSE 8888

# Set default command
CMD ["conda", "run", "-n", "ai-env", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

### Docker Compose Configuration

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  ai-environment:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/app/notebooks
      - ./data:/app/data
    environment:
      - JUPYTER_ENABLE_LAB=yes
      - CUDA_VISIBLE_DEVICES=0
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    networks:
      - ai-network

  mlflow:
    image: python:3.10
    ports:
      - "5000:5000"
    command: pip install mlflow && mlflow server --host 0.0.0.0 --port 5000
    networks:
      - ai-network

networks:
  ai-network:
    driver: bridge
```

### Multi-stage Docker Build

```dockerfile
# Build stage
FROM nvidia/cuda:12.4-devel-ubuntu22.04 as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements-build.txt .
RUN pip install --user --no-cache-dir -r requirements-build.txt

# Runtime stage
FROM nvidia/cuda:12.4-runtime-ubuntu22.04

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Set environment variables
ENV PATH=/root/.local/bin:$PATH

# Copy application
COPY . /app
WORKDIR /app

# Set default command
CMD ["python3", "app.py"]
```

---

## Performance Optimization

### Environment Size Optimization

```bash
# Remove unnecessary packages
conda remove --name myenv --all
conda create -n optimized python=3.10 numpy pandas scikit-learn

# Use mamba for faster dependency resolution
conda install -n base -c conda-forge mamba
mamba create -n fast-env python=3.10 numpy pandas scikit-learn

# Clean conda cache
conda clean --all

# Remove pip cache
pip cache purge
```

### GPU-Optimized Environment

```yaml
name: gpu-optimized-env
channels:
  - nvidia
  - conda-forge
  - defaults

dependencies:
  - python=3.10
  - cudatoolkit=12.4
  - pytorch=2.6.0
  - torchvision=0.21.0
  - torchaudio=2.6.0
  - pytorch-cuda=12.4
  
  # GPU-accelerated libraries
  - cupy=12.0
  
  # Core packages
  - numpy=1.24
  - pandas=2.0
  - scikit-learn=1.3
  
  # Performance libraries
  - numba=0.57
  - numexpr=2.8
  
  # Jupyter
  - jupyter=1.0
  - ipykernel=6.0
```

### Memory Optimization

```python
# memory_optimization.py
import gc
import torch
import psutil

class MemoryOptimizer:
    def __init__(self):
        self.process = psutil.Process()
    
    def get_memory_usage(self):
        """Get current memory usage in MB."""
        return self.process.memory_info().rss / 1024 / 1024
    
    def clear_gpu_cache(self):
        """Clear GPU memory cache."""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.synchronize()
            gc.collect()
    
    def optimize_dataframe(self, df):
        """Optimize pandas DataFrame memory usage."""
        # Convert object columns to category if appropriate
        for col in df.select_dtypes(include=['object']).columns:
            if df[col].nunique() / len(df) < 0.5:
                df[col] = df[col].astype('category')
        
        # Downcast numeric columns
        for col in df.select_dtypes(include=['int']).columns:
            df[col] = pd.to_numeric(df[col], downcast='integer')
        
        for col in df.select_dtypes(include=['float']).columns:
            df[col] = pd.to_numeric(df[col], downcast='float')
        
        return df

# Usage
optimizer = MemoryOptimizer()
print(f"Memory usage: {optimizer.get_memory_usage():.2f} MB")
optimizer.clear_gpu_cache()
```

---

## Practical Exercises

### Exercise 1: Create GPU-Optimized Environment

```bash
# Create GPU-optimized environment
conda create -n gpu-ai-env python=3.10

# Activate environment
conda activate gpu-ai-env

# Install CUDA and PyTorch with GPU support
conda install -c nvidia -c conda-forge \
    cudatoolkit=12.4 \
    pytorch=2.6.0 \
    torchvision=0.21.0 \
    torchaudio=2.6.0 \
    pytorch-cuda=12.4

# Install additional packages
conda install -c conda-forge numpy pandas matplotlib scikit-learn
pip install transformers huggingface_hub

# Test GPU availability
python -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'CUDA version: {torch.version.cuda}')
print(f'GPU count: {torch.cuda.device_count()}')
if torch.cuda.is_available():
    print(f'Current GPU: {torch.cuda.current_device()}')
    print(f'GPU name: {torch.cuda.get_device_name(0)}')
"
```

### Exercise 2: Docker Container with AI Environment

Create `Dockerfile`:
```dockerfile
FROM nvidia/cuda:12.4-devel-ubuntu22.04

# Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

#
