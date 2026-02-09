# Dockerization of AI Projects

**Duration**: 4 hours  
**Prerequisites**: Python 3.10+, PyTorch 2.6.0+, CUDA 12.4+, Docker installed

---

## Table of Contents

1. [Introduction to Docker](#introduction-to-docker)
2. [Docker Fundamentals](#docker-fundamentals)
3. [Building Custom Images for AI Projects](#building-custom-images-for-ai-projects)
4. [GPU Support in Docker](#gpu-support-in-docker)
5. [Docker Compose for Multi-Service Applications](#docker-compose-for-multi-service-applications)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)

---

## Introduction to Docker

Docker is a platform for developing, shipping, and running applications in containers. Containers package your code and all its dependencies so the application runs quickly and reliably across different computing environments.

### Why Docker for AI/ML Projects?

**Benefits**:
- **Reproducibility**: Ensure consistent environments across development, testing, and production
- **Isolation**: Avoid dependency conflicts between projects
- **Portability**: Run anywhere - local machine, cloud, on-premises
- **Version Control**: Track environment changes alongside code
- **Scalability**: Easy to scale horizontally
- **Collaboration**: Share exact environments with team members

**Use Cases**:
- Model training and experimentation
- Model serving and inference
- CI/CD pipelines
- Distributed training
- Multi-service AI applications

---

## Docker Fundamentals

### Core Concepts

#### 1. Images

**Definition**: Read-only templates containing the application and its dependencies.

**Key Points**:
- Built from Dockerfile instructions
- Layered architecture (each instruction creates a layer)
- Cached for faster builds
- Stored in registries (Docker Hub, private registries)

**Common Commands**:
```bash
# List images
docker images

# Pull an image from registry
docker pull python:3.10

# Build an image
docker build -t myapp:latest .

# Remove an image
docker rmi myapp:latest

# Tag an image
docker tag myapp:latest myregistry/myapp:v1.0

# Push to registry
docker push myregistry/myapp:v1.0
```

#### 2. Containers

**Definition**: Runnable instances of images.

**Lifecycle**:
```bash
# Create and start a container
docker run -d --name mycontainer myapp:latest

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop mycontainer

# Start a stopped container
docker start mycontainer

# Remove a container
docker rm mycontainer

# View container logs
docker logs mycontainer

# Execute command in running container
docker exec -it mycontainer bash

# Copy files to/from container
docker cp mycontainer:/app/output.txt ./output.txt
```

#### 3. Dockerfile

**Definition**: Text file with instructions to build a Docker image.

**Basic Structure**:
```dockerfile
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Set environment variables
ENV MODEL_NAME="gpt2"

# Define entry point
CMD ["python", "app.py"]
```

**Common Instructions**:
- `FROM`: Base image
- `WORKDIR`: Set working directory
- `COPY`: Copy files from host to image
- `ADD`: Copy files (also extracts archives)
- `RUN`: Execute commands during build
- `CMD`: Default command when container starts
- `ENTRYPOINT`: Configure container as executable
- `ENV`: Set environment variables
- `EXPOSE`: Document which ports are used
- `VOLUME`: Create mount points

#### 4. Volumes

**Definition**: Persistent data storage outside container filesystem.

**Types**:
```bash
# Named volume
docker volume create mydata
docker run -v mydata:/app/data myapp

# Bind mount (host directory)
docker run -v /host/path:/container/path myapp

# Anonymous volume
docker run -v /container/path myapp

# List volumes
docker volume ls

# Inspect volume
docker volume inspect mydata

# Remove volume
docker volume rm mydata
```

#### 5. Networks

**Definition**: Enable container communication.

**Types**:
- **bridge**: Default, isolated network
- **host**: Use host network directly
- **none**: No network access
- **Custom**: User-defined networks

```bash
# Create network
docker network create mynetwork

# Run container on network
docker run --network mynetwork myapp

# List networks
docker network ls

# Inspect network
docker network inspect mynetwork
```

---

## Building Custom Images for AI Projects

### Basic PyTorch Image

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "train.py"]
```

**requirements.txt**:
```
torch>=2.6.0
torchvision>=0.19.0
transformers>=4.40.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
jupyter>=1.0.0
```

**Build and Run**:
```bash
# Build image
docker build -t pytorch-app:latest .

# Run container
docker run --rm pytorch-app:latest

# Run with GPU (requires nvidia-docker)
docker run --gpus all --rm pytorch-app:latest

# Run interactively
docker run -it --rm pytorch-app:latest bash
```

### Multi-Stage Build for Smaller Images

**Concept**: Use multiple FROM statements to reduce final image size.

```dockerfile
# Stage 1: Build dependencies
FROM python:3.10 as builder

WORKDIR /app

# Install build dependencies
RUN pip install --user --no-cache-dir \
    torch>=2.6.0 \
    transformers>=4.40.0

# Stage 2: Runtime image
FROM python:3.10-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local

# Update PATH
ENV PATH=/root/.local/bin:$PATH

# Copy application
COPY . .

CMD ["python", "inference.py"]
```

### Hugging Face Model Serving

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    torch>=2.6.0 \
    transformers>=4.40.0 \
    fastapi>=0.110.0 \
    uvicorn[standard]>=0.29.0 \
    huggingface-hub>=0.22.0

# Copy application
COPY app.py .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**app.py**:
```python
from fastapi import FastAPI
from transformers import pipeline
import torch

app = FastAPI()

# Load model
device = 0 if torch.cuda.is_available() else -1
classifier = pipeline("sentiment-analysis", device=device)

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API"}

@app.post("/predict")
def predict(text: str):
    result = classifier(text)[0]
    return {
        "text": text,
        "label": result["label"],
        "score": result["score"]
    }
```

**Usage**:
```bash
# Build
docker build -t hf-serving:latest .

# Run
docker run -p 8000:8000 --gpus all hf-serving:latest

# Test
curl -X POST "http://localhost:8000/predict?text=I%20love%20this!"
```

---

## GPU Support in Docker

### Prerequisites

1. **NVIDIA Driver**: Version 535+ for CUDA 12.4
2. **NVIDIA Container Toolkit**: Install nvidia-docker2

**Installation (Ubuntu)**:
```bash
# Add NVIDIA package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Install nvidia-docker2
sudo apt-get update
sudo apt-get install -y nvidia-docker2

# Restart Docker daemon
sudo systemctl restart docker

# Test GPU access
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

### CUDA Base Images

**Official NVIDIA Images**:
- `nvidia/cuda:12.4.0-base-ubuntu22.04`: CUDA runtime only
- `nvidia/cuda:12.4.0-runtime-ubuntu22.04`: CUDA runtime + libraries
- `nvidia/cuda:12.4.0-devel-ubuntu22.04`: Full CUDA development kit

**PyTorch GPU Dockerfile**:
```dockerfile
FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

# Install Python 3.10
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

WORKDIR /app

# Install PyTorch with CUDA 12.4 support
RUN pip install --no-cache-dir \
    torch>=2.6.0 \
    torchvision>=0.19.0 \
    torchaudio>=2.6.0 \
    --index-url https://download.pytorch.org/whl/cu124

# Install additional dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "train.py"]
```

### Running with GPU Access

**Basic GPU Access**:
```bash
# All GPUs
docker run --gpus all myapp

# Specific GPU
docker run --gpus '"device=0"' myapp

# Multiple specific GPUs
docker run --gpus '"device=0,1"' myapp

# Limit GPU count
docker run --gpus 2 myapp
```

**Advanced GPU Configuration**:
```bash
# Set GPU memory limit
docker run --gpus all --memory=16g --memory-swap=16g myapp

# Set shared memory size (important for PyTorch DataLoader)
docker run --gpus all --shm-size=8g myapp

# Environment variables
docker run --gpus all \
    -e CUDA_VISIBLE_DEVICES=0,1 \
    -e NVIDIA_VISIBLE_DEVICES=all \
    myapp
```

### Verifying GPU Access

**Test Script (test_gpu.py)**:
```python
import torch
import sys

print(f"Python: {sys.version}")
print(f"PyTorch: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA Version: {torch.version.cuda}")
    print(f"GPU Count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        
    # Test computation
    x = torch.randn(1000, 1000).cuda()
    y = torch.randn(1000, 1000).cuda()
    z = torch.matmul(x, y)
    print("✅ GPU computation successful")
else:
    print("❌ CUDA not available")
```

```bash
# Run test
docker run --gpus all --rm pytorch-gpu:latest python test_gpu.py
```

---

## Docker Compose for Multi-Service Applications

### Introduction

Docker Compose allows you to define and run multi-container applications using a YAML file.

### Basic Example: Model Training + Monitoring

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  # Training service
  trainer:
    build:
      context: .
      dockerfile: Dockerfile.train
    container_name: model_trainer
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    volumes:
      - ./data:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    shm_size: '8gb'
    command: python train.py
    depends_on:
      - mlflow

  # MLflow tracking server
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.11.0
    container_name: mlflow_server
    ports:
      - "5000:5000"
    volumes:
      - ./mlruns:/mlflow/mlruns
    command: >
      mlflow server
      --backend-store-uri sqlite:///mlflow/mlruns/mlflow.db
      --default-artifact-root /mlflow/mlruns
      --host 0.0.0.0

  # Jupyter notebook
  jupyter:
    build:
      context: .
      dockerfile: Dockerfile.jupyter
    container_name: jupyter_lab
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/app/notebooks
      - ./data:/app/data
    command: >
      jupyter lab
      --ip=0.0.0.0
      --port=8888
      --no-browser
      --allow-root
      --NotebookApp.token=''
```

**Usage**:
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f trainer

# Stop all services
docker-compose down

# Rebuild and start
docker-compose up -d --build

# Scale a service
docker-compose up -d --scale trainer=3
```

### Advanced Example: Complete ML Pipeline

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  # PostgreSQL database
  postgres:
    image: postgres:15
    container_name: postgres_db
    environment:
      POSTGRES_USER: mluser
      POSTGRES_PASSWORD: mlpassword
      POSTGRES_DB: mldb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  # Redis cache
  redis:
    image: redis:7-alpine
    container_name: redis_cache
    ports:
      - "6379:6379"

  # Model training
  trainer:
    build:
      context: ./training
      dockerfile: Dockerfile
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=0
      - DATABASE_URL=postgresql://mluser:mlpassword@postgres:5432/mldb
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./data:/data
      - ./models:/models
    depends_on:
      - postgres
      - redis
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # Model serving
  serving:
    build:
      context: ./serving
      dockerfile: Dockerfile
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=1
      - MODEL_PATH=/models/best_model.pt
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./models:/models:ro
    ports:
      - "8000:8000"
    depends_on:
      - redis
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # API Gateway
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      - SERVING_URL=http://serving:8000
    depends_on:
      - serving

volumes:
  postgres_data:
```

### Environment Variables

**.env file**:
```env
# Database
POSTGRES_USER=mluser
POSTGRES_PASSWORD=mlpassword
POSTGRES_DB=mldb

# Model settings
MODEL_NAME=bert-base-uncased
BATCH_SIZE=32
LEARNING_RATE=2e-5

# Paths
DATA_PATH=/data
MODEL_PATH=/models
```

**Reference in docker-compose.yml**:
```yaml
services:
  trainer:
    env_file:
      - .env
    # or
    environment:
      - MODEL_NAME=${MODEL_NAME}
      - BATCH_SIZE=${BATCH_SIZE}
```

---

## Best Practices

### 1. Image Optimization

**Minimize Layer Count**:
```dockerfile
# ❌ Bad: Multiple layers
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y git

# ✅ Good: Single layer
RUN apt-get update && apt-get install -y \
    python3 \
    git \
    && rm -rf /var/lib/apt/lists/*
```

**Order Instructions by Change Frequency**:
```dockerfile
# ✅ Good: Least frequently changed first
FROM python:3.10-slim

# System dependencies (rarely change)
RUN apt-get update && apt-get install -y git

# Python dependencies (occasionally change)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Application code (frequently changes)
COPY . .
```

**Use .dockerignore**:
```
# .dockerignore
__pycache__
*.pyc
*.pyo
*.pyd
.git
.gitignore
.env
.venv
*.ipynb_checkpoints
.pytest_cache
.coverage
htmlcov/
dist/
build/
*.egg-info/
.DS_Store
```

### 2. Security

**Don't Run as Root**:
```dockerfile
FROM python:3.10-slim

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Install dependencies as root
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app and change ownership
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

CMD ["python", "app.py"]
```

**Don't Include Secrets**:
```dockerfile
# ❌ Bad
ENV API_KEY="secret_key_12345"

# ✅ Good: Use runtime environment variables
# docker run -e API_KEY=$API_KEY myapp
```

### 3. Resource Management

**Set Memory Limits**:
```bash
docker run -m 4g --memory-swap 4g myapp
```

**Set CPU Limits**:
```bash
docker run --cpus="2.0" myapp
```

**In docker-compose.yml**:
```yaml
services:
  trainer:
    deploy:
      resources:
        limits:
          cpus: '4.0'
          memory: 16G
        reservations:
          cpus: '2.0'
          memory: 8G
```

### 4. Logging

**Configure JSON logging**:
```bash
docker run --log-driver json-file --log-opt max-size=10m --log-opt max-file=3 myapp
```

**Application logging**:
```python
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
```

### 5. Health Checks

**Dockerfile**:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"
```

**docker-compose.yml**:
```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s
```

---

## Troubleshooting

### Common Issues

#### 1. Container Exits Immediately

**Debug**:
```bash
# View logs
docker logs container_name

# Run interactively
docker run -it --entrypoint /bin/bash myapp
```

#### 2. Permission Denied

**Solution**:
```dockerfile
# Fix file permissions
RUN chmod +x /app/entrypoint.sh
```

#### 3. GPU Not Accessible

**Check**:
```bash
# Verify nvidia-docker installation
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi

# Check runtime
docker info | grep -i runtime
```

#### 4. Port Already in Use

**Solution**:
```bash
# Use different host port
docker run -p 8001:8000 myapp

# Or find and kill process
lsof -ti:8000 | xargs kill -9
```

#### 5. Out of Disk Space

**Cleanup**:
```bash
# Remove unused containers
docker container prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Complete cleanup
docker system prune -a --volumes
```

### Debugging Tips

**Inspect Container**:
```bash
# Container details
docker inspect container_name

# Resource usage
docker stats container_name

# Processes
docker top container_name

# File system changes
docker diff container_name
```

**Interactive Debugging**:
```bash
# Enter running container
docker exec -it container_name bash

# Run specific command
docker exec container_name ls -la /app

# Copy files out
docker cp container_name:/app/debug.log ./
```

---

## Summary

This chapter covered Docker fundamentals and containerization for AI projects:

1. **Docker Basics**: Images, containers, Dockerfile, volumes, networks
2. **Custom Images**: Building PyTorch images, multi-stage builds, model serving
3. **GPU Support**: NVIDIA Container Toolkit, CUDA images, GPU configuration
4. **Docker Compose**: Multi-service orchestration, environment management
5. **Best Practices**: Optimization, security, resource management, health checks
6. **Troubleshooting**: Common issues and debugging techniques

Practice these concepts in the accompanying Jupyter notebook: [dockerization_practice.ipynb](./02_dockerization_practice.ipynb)

---

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [PyTorch Docker Images](https://hub.docker.com/r/pytorch/pytorch)
