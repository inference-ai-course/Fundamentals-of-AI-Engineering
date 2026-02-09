# Authentication and Security

## Introduction

Proper authentication and security practices are critical when working with AI inference APIs. This guide covers best practices for managing credentials, securing API access, and protecting sensitive data.

## Hugging Face Token Management

### Obtaining Your Token

1. **Sign up/Login** to [Hugging Face](https://huggingface.co)
2. Navigate to **Settings** → **Access Tokens**
3. Click **New Token**
4. Choose token type:
   - **Read**: Access public models and datasets
   - **Write**: Upload and modify resources
   - **Fine-grained**: Custom permissions

### Token Types and Permissions

| Token Type | Use Case | Permissions |
|------------|----------|-------------|
| Read | Public model inference | Read public repos, use inference API |
| Write | Model development | Read + write repos, manage spaces |
| Fine-grained | Production apps | Custom scoped permissions |

### Secure Token Storage

#### Method 1: Environment Variables (Recommended)

**Linux/macOS:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export HF_TOKEN="hf_your_token_here"

# Reload shell configuration
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
# Set for current session
$env:HF_TOKEN = "hf_your_token_here"

# Set permanently (User level)
[System.Environment]::SetEnvironmentVariable('HF_TOKEN', 'hf_your_token_here', 'User')
```

**Verify in Python:**
```python
import os

token = os.getenv("HF_TOKEN")
if token:
    print("Token loaded successfully")
else:
    print("Warning: HF_TOKEN not found")
```

#### Method 2: Configuration File

The `huggingface_hub` library automatically reads from `~/.huggingface/token`:

```bash
# Login via CLI (recommended)
huggingface-cli login

# Or manually create the file
mkdir -p ~/.huggingface
echo "hf_your_token_here" > ~/.huggingface/token
chmod 600 ~/.huggingface/token  # Restrict permissions
```

**Python usage:**
```python
from huggingface_hub import InferenceClient

# Token automatically loaded from ~/.huggingface/token
client = InferenceClient()
```

#### Method 3: Secret Management Systems (Production)

**AWS Secrets Manager:**
```python
import boto3
import json

def get_hf_token():
    client = boto3.client('secretsmanager', region_name='us-east-1')
    response = client.get_secret_value(SecretId='huggingface/token')
    secret = json.loads(response['SecretString'])
    return secret['HF_TOKEN']

token = get_hf_token()
```

**Azure Key Vault:**
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_hf_token():
    credential = DefaultAzureCredential()
    vault_url = "https://your-vault.vault.azure.net/"
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret("HF-TOKEN")
    return secret.value

token = get_hf_token()
```

**HashiCorp Vault:**
```python
import hvac

def get_hf_token():
    client = hvac.Client(url='http://localhost:8200')
    client.token = os.getenv('VAULT_TOKEN')
    secret = client.secrets.kv.v2.read_secret_version(
        path='huggingface/token'
    )
    return secret['data']['data']['token']

token = get_hf_token()
```

## Security Best Practices

### ❌ What NOT to Do

**1. Hardcoding Tokens**
```python
# NEVER DO THIS!
client = InferenceClient(token="hf_abc123xyz456")
```

**2. Committing Tokens to Git**
```python
# config.py - INSECURE!
HF_TOKEN = "hf_abc123xyz456"
```

**3. Logging Tokens**
```python
# NEVER DO THIS!
print(f"Using token: {token}")
logger.info(f"Token: {token}")
```

**4. Exposing in URLs**
```python
# INSECURE!
url = f"https://api.huggingface.co/models?token={token}"
```

### ✅ What TO Do

**1. Use Environment Variables**
```python
import os
from huggingface_hub import InferenceClient

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError("HF_TOKEN environment variable not set")

client = InferenceClient(token=token)
```

**2. Use .gitignore**
```gitignore
# .gitignore
.env
.env.local
*.token
config/secrets.json
.huggingface/token
```

**3. Use .env Files (with python-dotenv)**
```python
# .env file (add to .gitignore!)
HF_TOKEN=hf_your_token_here

# Python code
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file
token = os.getenv("HF_TOKEN")
```

**4. Validate Token Format**
```python
import re

def validate_hf_token(token: str) -> bool:
    """Validate Hugging Face token format"""
    if not token:
        return False
    # HF tokens start with 'hf_' and are alphanumeric
    pattern = r'^hf_[a-zA-Z0-9]{30,}$'
    return bool(re.match(pattern, token))

token = os.getenv("HF_TOKEN")
if not validate_hf_token(token):
    raise ValueError("Invalid HF_TOKEN format")
```

## Jupyter Notebook Security

### Secure Token Loading in Notebooks

```python
# Cell 1: Import and load token
import os
from getpass import getpass
from huggingface_hub import InferenceClient

# Try environment variable first
token = os.getenv("HF_TOKEN")

# If not found, prompt securely (won't show in output)
if not token:
    token = getpass("Enter your Hugging Face token: ")

# Verify token is loaded
assert token, "Token must be provided"
print("✓ Token loaded successfully")
```

### Clear Outputs Before Sharing

```python
# Add this to your notebook
from IPython.display import clear_output

# After sensitive operations
clear_output(wait=True)
print("Operation completed")
```

### Notebook Best Practices

1. **Clear all outputs** before committing notebooks to Git
2. **Never print** token values
3. **Use getpass()** for interactive token input
4. **Document** that users need to set `HF_TOKEN` environment variable
5. **Add warnings** at the top of notebooks about security

## Authentication with Different Clients

### huggingface_hub.InferenceClient

```python
from huggingface_hub import InferenceClient
import os

# Method 1: Explicit token
client = InferenceClient(token=os.getenv("HF_TOKEN"))

# Method 2: Auto-load from ~/.huggingface/token
client = InferenceClient()  # Automatically uses saved token
```

### OpenAI-Compatible Client

```python
from openai import OpenAI
import os

# For Hugging Face with OpenAI compatibility
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)
```

### Requests Library

```python
import requests
import os

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload)
```

## Token Rotation and Revocation

### When to Rotate Tokens

- **Regular schedule**: Every 90 days for production
- **After exposure**: Immediately if token is compromised
- **Team changes**: When team members leave
- **Security incidents**: As part of incident response

### How to Rotate

1. **Generate new token** on Hugging Face
2. **Update secret storage** (environment variables, vault, etc.)
3. **Test with new token** in non-production environment
4. **Deploy to production**
5. **Revoke old token** after verification

### Revoking Compromised Tokens

1. Go to [Hugging Face Settings → Access Tokens](https://huggingface.co/settings/tokens)
2. Click **Revoke** next to the compromised token
3. Generate a new token immediately
4. Update all systems using the old token

## Monitoring and Auditing

### Track Token Usage

```python
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def log_api_call(endpoint: str, status: str):
    """Log API calls without exposing tokens"""
    logger.info(
        f"API Call - Endpoint: {endpoint}, "
        f"Status: {status}, "
        f"Timestamp: {datetime.now().isoformat()}"
    )

# Usage
try:
    response = client.text_to_image(prompt)
    log_api_call("text_to_image", "success")
except Exception as e:
    log_api_call("text_to_image", f"failed: {type(e).__name__}")
```

### Rate Limiting and Quotas

```python
from time import sleep, time
from collections import deque

class RateLimiter:
    """Simple rate limiter for API calls"""
    
    def __init__(self, max_calls: int, time_window: int):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
    
    def wait_if_needed(self):
        now = time()
        
        # Remove old calls outside time window
        while self.calls and self.calls[0] < now - self.time_window:
            self.calls.popleft()
        
        # Wait if at limit
        if len(self.calls) >= self.max_calls:
            sleep_time = self.time_window - (now - self.calls[0])
            if sleep_time > 0:
                print(f"Rate limit reached, waiting {sleep_time:.1f}s")
                sleep(sleep_time)
        
        self.calls.append(now)

# Usage: 10 calls per minute
limiter = RateLimiter(max_calls=10, time_window=60)

for prompt in prompts:
    limiter.wait_if_needed()
    response = client.text_to_image(prompt)
```

## Compliance and Data Privacy

### GDPR Considerations

- **Data Minimization**: Only send necessary data to APIs
- **User Consent**: Obtain consent before processing personal data
- **Data Retention**: Understand provider data retention policies
- **Right to Deletion**: Know how to request data deletion

### Example: Anonymizing User Data

```python
import hashlib

def anonymize_user_id(user_id: str) -> str:
    """Hash user IDs before sending to API"""
    return hashlib.sha256(user_id.encode()).hexdigest()[:16]

# Use anonymized ID in prompts
anon_id = anonymize_user_id("user@example.com")
prompt = f"Generate image for user {anon_id}"
```

## Summary Checklist

- ✅ Store tokens in environment variables or secret management systems
- ✅ Never hardcode tokens in source code
- ✅ Add token files to `.gitignore`
- ✅ Use `getpass()` for interactive token input in notebooks
- ✅ Validate token format before use
- ✅ Implement rate limiting to avoid quota exhaustion
- ✅ Log API usage without exposing credentials
- ✅ Rotate tokens regularly
- ✅ Revoke compromised tokens immediately
- ✅ Consider data privacy and compliance requirements

## Next Steps

- Review **[Provider Selection and Failover](04_provider_selection.md)**
- Practice secure authentication in **[Image Generation Practice](01_image_generation_practice.ipynb)**
