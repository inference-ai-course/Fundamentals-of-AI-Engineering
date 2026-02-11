# Part 2: Modules and Exception Handling

## Overview

As your Python projects grow from single scripts to complex systems, two skills become critical: **organizing code into modules** and **handling errors gracefully**. This section teaches you to build production-ready applications that don't just work—they work reliably.

---

## Why Modules and Error Handling Matter

### The Scaling Problem

```
Small Project (1 file):
────────────────────────
script.py (500 lines)
→ Easy to understand
→ But hard to test, reuse, or maintain

Large Project (unorganized):
────────────────────────────
script.py (5,000 lines)
→ Impossible to navigate
→ No code reuse
→ Testing nightmare
→ Merge conflicts in teams

Large Project (organized):
──────────────────────────
├── data/
│   ├── loader.py
│   └── validator.py
├── models/
│   ├── training.py
│   └── evaluation.py
├── utils/
│   └── helpers.py
└── main.py
→ Clear organization
→ Easy to test
→ Team collaboration
→ Code reuse
```

### Error Handling: The Difference Between Toys and Tools

**Without error handling (toy code):**
```python
data = json.loads(file_content)
model.fit(data)
# Crashes on bad data, no recovery, users frustrated
```

**With error handling (production code):**
```python
try:
    data = json.loads(file_content)
    validate_data(data)
    model.fit(data)
except json.JSONDecodeError:
    logger.error("Invalid JSON format")
    return default_config
except ValidationError as e:
    logger.warning(f"Data validation failed: {e}")
    data = fallback_data()
# Continues running, logs issues, recovers gracefully
```

**In AI/ML context:**
- Model training can fail after hours
- Data pipelines process millions of files
- API calls can timeout or fail
- **Robust error handling saves time, money, and sanity**

---

## Table of Contents
1. [Working with Modules](#working-with-modules)
2. [Creating Your Own Modules](#creating-your-own-modules)
3. [Exception Handling](#exception-handling)
4. [File I/O Operations](#file-io-operations)
5. [JSON Processing](#json-processing)
6. [Practical Exercises](#practical-exercises)

---

## Working with Modules

Python's module system allows you to organize code into separate files and reuse functionality from the standard library and third-party packages.

### Importing Standard Library Modules

```python
# Different ways to import modules
# Python Standard Library: https://docs.python.org/3/library/
import math
import json
import csv
import os
from datetime import datetime, timedelta
import random

# Using imported modules
# Math module
radius = 5
area = math.pi * radius ** 2
print(f"Circle area: {area:.2f}")

# Square root and power
number = 16
sqrt_result = math.sqrt(number)
power_result = math.pow(2, 3)
print(f"Square root of {number}: {sqrt_result}")
print(f"2 to the power of 3: {power_result}")

# DateTime module
now = datetime.now()
print(f"Current time: {now}")

# Calculate future date
one_week_later = now + timedelta(days=7)
print(f"One week from now: {one_week_later}")

# Random module
random_number = random.randint(1, 100)
random_float = random.random()
print(f"Random integer (1-100): {random_number}")
print(f"Random float (0-1): {random_float:.3f}")
```

### Selective Imports

```python
# Import specific functions
from math import sqrt, pow, factorial
from datetime import datetime as dt
from random import choice, shuffle

# Use imported functions directly
print(f"Square root of 25: {sqrt(25)}")
print(f"2^10: {pow(2, 10)}")
print(f"5!: {factorial(5)}")

# Use alias
current_time = dt.now()
print(f"Current time (using alias): {current_time}")

# Use choice and shuffle
colors = ["red", "green", "blue", "yellow"]
random_color = choice(colors)
print(f"Random color: {random_color}")

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(f"Shuffled numbers: {numbers}")
```

### Working with CSV Data

```python
import csv
import os

def create_sample_csv(filename='sample_data.csv'):
    """Create a sample CSV file with data."""
    data = [
        ['Name', 'Age', 'City', 'Score'],
        ['Alice', '25', 'New York', '85'],
        ['Bob', '30', 'San Francisco', '92'],
        ['Charlie', '22', 'Chicago', '78'],
        ['Diana', '28', 'Boston', '88']
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"Sample CSV created: {filename}")

def read_csv_file(filename):
    """Read and process CSV file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            print(f"Reading {filename}:")
            for row in reader:
                name = row['Name']
                age = row['Age']
                city = row['City']
                score = row['Score']
                print(f"  {name}, {age}, {city}, {score}")
            
            # Reset file pointer and calculate average score
            file.seek(0)
            next(reader)  # Skip header
            scores = [int(row['Score']) for row in reader]
            average = sum(scores) / len(scores)
            print(f"Average score: {average:.1f}")
            
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error reading CSV: {e}")

# Create and read sample data
create_sample_csv()
read_csv_file('sample_data.csv')
```

---

## Creating Your Own Modules

Organize your code by creating reusable modules that can be imported into other programs.

### Basic Module Creation

Create a file named `math_utils.py`:
```python
# math_utils.py
"""Mathematical utility functions."""

import math
from typing import List, Union

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
    """
    return math.pi * radius ** 2

def calculate_statistics(numbers: List[float]) -> dict:
    """Calculate basic statistics for a list of numbers.
    
    Args:
        numbers: List of numerical values
        
    Returns:
        Dictionary with count, sum, mean, min, and max
    """
    if not numbers:
        return {"error": "Empty list provided"}
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    Args:
        n: The number to check
        
    Returns:
        True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Constants
PI = math.pi
E = math.e
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2
```

### Using Your Module

Create a file named `main.py`:
```python
# main.py
"""Main program demonstrating module usage."""

import math_utils
from math_utils import calculate_statistics, is_prime, PI

def main():
    """Main function to demonstrate module usage."""
    print("=== Math Utils Module Demo ===\n")
    
    # Using functions from the module
    radius = 5
    area = math_utils.calculate_circle_area(radius)
    print(f"Circle with radius {radius} has area: {area:.2f}")
    
    # Using imported functions directly
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = calculate_statistics(numbers)
    print(f"\nStatistics for {numbers}:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Using constants
    print(f"\nConstants from module:")
    print(f"  PI: {PI}")
    print(f"  E: {math_utils.E}")
    print(f"  Golden Ratio: {math_utils.GOLDEN_RATIO:.6f}")
    
    # Testing prime function
    test_numbers = [2, 3, 4, 5, 16, 17, 18, 19]
    print(f"\nPrime numbers in {test_numbers}:")
    primes = [n for n in test_numbers if is_prime(n)]
    print(f"  Primes: {primes}")

if __name__ == "__main__":
    main()
```

### Package Structure

Create a simple package structure:
```
my_package/
├── __init__.py
├── calculations.py
├── data_processing.py
└── utils.py
```

Create `my_package/__init__.py`:
```python
# my_package/__init__.py
"""My package for calculations and data processing."""

from .calculations import add, multiply, power
from .data_processing import clean_data, validate_data
from .utils import timer, logger

__version__ = "1.0.0"
__author__ = "Your Name"
```

Create `my_package/calculations.py`:
```python
# my_package/calculations.py
"""Calculation functions."""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Calculate base raised to power."""
    return base ** exponent
```

Create `my_package/data_processing.py`:
```python
# my_package/data_processing.py
"""Data processing functions."""

def clean_data(data):
    """Clean and normalize data."""
    if isinstance(data, list):
        return [item.strip() if isinstance(item, str) else item for item in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def validate_data(data, data_type):
    """Validate data type and format."""
    if data_type == "email":
        return "@" in data and "." in data
    elif data_type == "phone":
        return data.replace("-", "").replace(" ", "").isdigit()
    return True
```

Create `my_package/utils.py`:
```python
# my_package/utils.py
"""Utility functions."""

import time
from functools import wraps

def timer(func):
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logger(func):
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
```

---

## Exception Handling

### Understanding Python's Exception System

Exception handling allows you to manage errors gracefully. Instead of crashing, your program can recover, log the issue, and continue or fail elegantly.

**Python's Exception Philosophy:**
```
"It's easier to ask for forgiveness than permission" (EAFP)

vs.

"Look before you leap" (LBYL)
```

**Python way (EAFP):**
```python
try:
    value = my_dict['key']
except KeyError:
    value = default_value
```

**Not Python way (LBYL):**
```python
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = default_value
```

**Why EAFP?**
- Handles race conditions better
- More readable for happy path
- Faster when exceptions are rare
- More Pythonic

### Exception Hierarchy

Understanding the exception hierarchy helps you catch errors at the right level:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception (← Catch this or more specific)
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── FileNotFoundError
    ├── IOError
    └── ... many more
```

**Best practices:**
- ✅ Catch specific exceptions: `except ValueError`
- ✅ Catch Exception for unknown errors
- ❌ Never catch BaseException (blocks Ctrl+C!)
- ❌ Avoid bare except (hides all errors)

---

### Basic try/except Structure

```python
def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None

# Test the function
print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Error message
print(safe_divide("10", 2))    # Error message
```

### Handling Multiple Exception Types

```python
def process_user_input(user_input):
    """Process user input with comprehensive error handling."""
    try:
        # Try to convert to integer
        number = int(user_input)
        
        # Check if positive
        if number < 0:
            raise ValueError("Number must be positive")
        
        # Calculate square root
        import math
        result = math.sqrt(number)
        return result
        
    except ValueError as e:
        print(f"Value Error: {e}")
        return None
    except TypeError:
        print("Type Error: Input must be a string or number")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test the function
print(process_user_input("16"))    # 4.0
print(process_user_input("-5"))    # Value Error
print(process_user_input("abc"))   # Value Error
```

### Using else and finally

```python
def read_file_safely(filename):
    """Read a file with comprehensive error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except IOError as e:
        print(f"IO Error reading file: {e}")
        return None
    else:
        # This block executes if no exception occurs
        print(f"Successfully read {len(content)} characters")
        return content
    finally:
        # This block always executes
        print(f"Finished attempting to read file: {filename}")

# Test the function
content = read_file_safely('example.txt')
if content:
    print(f"First 50 characters: {content[:50]}...")
```

### Raising Custom Exceptions

```python
class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

class AgeValidationError(ValidationError):
    """Custom exception for age validation errors."""
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = f"{message}: {age}"
        super().__init__(self.message)

def validate_age(age):
    """Validate age with custom exceptions."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise AgeValidationError(age, "Age cannot be negative")
    
    if age > 150:
        raise AgeValidationError(age, "Age seems unrealistic")
    
    if age < 18:
        raise ValidationError("Must be 18 or older")
    
    return True

# Test the validation
test_ages = [25, -5, "25", 200, 16]

for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age}: Valid")
    except AgeValidationError as e:
        print(f"Age {age}: {e}")
    except ValidationError as e:
        print(f"Age {age}: {e}")
    except Exception as e:
        print(f"Age {age}: Unexpected error - {e}")
```

---

## File I/O Operations

File input/output is essential for working with data persistence and external data sources.

### Reading Files Safely

```python
def read_text_file(filename):
    """Read a text file with proper error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def read_file_line_by_line(filename):
    """Read file line by line for large files."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = []
            for line_num, line in enumerate(file, 1):
                # Process each line
                cleaned_line = line.strip()
                if cleaned_line:  # Skip empty lines
                    lines.append(cleaned_line)
                    print(f"Line {line_num}: {cleaned_line}")
            return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error processing file: {e}")
        return []

# Create a sample file for testing
def create_sample_text_file(filename='sample.txt'):
    """Create a sample text file."""
    content = """Python is a powerful programming language.
It is widely used in data science and AI.
File handling is an important skill.
Practice makes perfect!"""
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Sample file created: {filename}")

# Test file operations
create_sample_text_file()
content = read_text_file('sample.txt')
if content:
    print(f"\nFile content:\n{content}")

print("\nReading line by line:")
lines = read_file_line_by_line('sample.txt')
print(f"\nTotal lines: {len(lines)}")
```

### Writing Files

```python
def write_to_file(filename, content, mode='w'):
    """Write content to a file with specified mode."""
    try:
        with open(filename, mode, encoding='utf-8') as file:
            if isinstance(content, list):
                for line in content:
                    file.write(str(line) + '\n')
            else:
                file.write(str(content))
        print(f"Successfully wrote to {filename}")
        return True
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False

def append_to_file(filename, content):
    """Append content to a file."""
    return write_to_file(filename, content, mode='a')

# Test writing operations
data = [
    "First line of data",
    "Second line of data",
    "Third line of data"
]

write_to_file('output.txt', data)
append_to_file('output.txt', "Appended line")
append_to_file('output.txt', ["More data", "Even more data"])

# Read back to verify
print("\nVerifying written content:")
content = read_text_file('output.txt')
if content:
    print(content)
```

### Working with Different File Formats

```python
import csv
import json

def create_config_file(filename='config.json'):
    """Create a sample configuration file."""
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "api": {
            "timeout": 30,
            "retries": 3
        },
        "features": {
            "logging": True,
            "debug_mode": False
        }
    }
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=2)
        print(f"Config file created: {filename}")
        return True
    except Exception as e:
        print(f"Error creating config: {e}")
        return False

def read_config_file(filename='config.json'):
    """Read and parse configuration file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            config = json.load(file)
        
        print("Configuration loaded:")
        print(f"Database host: {config['database']['host']}")
        print(f"API timeout: {config['api']['timeout']} seconds")
        print(f"Logging enabled: {config['features']['logging']}")
        
        return config
    except FileNotFoundError:
        print(f"Config file '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in config file: {e}")
        return None
    except Exception as e:
        print(f"Error reading config: {e}")
        return None

# Test configuration file operations
create_config_file()
config = read_config_file('config.json')
```

---

## JSON Processing

JSON (JavaScript Object Notation) is a lightweight data format commonly used for data exchange.

### Basic JSON Operations

```python
import json

def create_sample_json():
    """Create sample JSON data."""
    data = {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com",
                "active": True,
                "scores": [85, 92, 78]
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com",
                "active": False,
                "scores": [79, 85, 88]
            }
        ],
        "metadata": {
            "total_users": 2,
            "last_updated": "2024-01-15"
        }
    }
    return data

def save_json_to_file(data, filename):
    """Save JSON data to file with pretty formatting."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"JSON data saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False

def load_json_from_file(filename):
    """Load JSON data from file with validation."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Basic validation
        if not isinstance(data, dict):
            raise ValueError("JSON data must be a dictionary")
        
        if 'users' not in data:
            raise ValueError("Missing required 'users' key")
        
        if not isinstance(data['users'], list):
            raise ValueError("'users' must be a list")
        
        print(f"JSON data loaded from {filename}")
        return data
        
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        return None
    except ValueError as e:
        print(f"Validation error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test JSON operations
sample_data = create_sample_json()
save_json_to_file(sample_data, 'users.json')
loaded_data = load_json_from_file('users.json')

if loaded_data:
    print("\nLoaded data summary:")
    print(f"Total users: {loaded_data['metadata']['total_users']}")
    for user in loaded_data['users']:
        avg_score = sum(user['scores']) / len(user['scores'])
        print(f"  {user['name']}: avg score = {avg_score:.1f}, active = {user['active']}")
```

### Advanced JSON Processing

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def process_json_data(json_string):
    """Process JSON data with custom handling."""
    try:
        data = json.loads(json_string)
        
        # Process the data
        if isinstance(data, list):
            print(f"Processing array with {len(data)} items")
            for item in data:
                process_item(item)
        elif isinstance(data, dict):
            print("Processing object")
            process_object(data)
        else:
            print(f"Processing simple value: {data}")
            
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None
    except Exception as e:
        print(f"Processing error: {e}")
        return None

def process_item(item):
    """Process individual JSON items."""
    if isinstance(item, dict):
        print(f"  Object with keys: {list(item.keys())}")
    elif isinstance(item, list):
        print(f"  Array with {len(item)} elements")
    else:
        print(f"  Value: {item}")

def process_object(obj):
    """Process JSON objects."""
    for key, value in obj.items():
        print(f"  {key}: {type(value).__name__} = {value}")

# Test with different JSON structures
test_json_strings = [
    '{"name": "Alice", "age": 30, "active": true}',
    '[1, 2, 3, 4, 5]',
    '{"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}',
    '"simple string"',
    '42',
    'true'
]

print("Testing different JSON structures:")
for json_str in test_json_strings:
    print(f"\nProcessing: {json_str}")
    process_json_data(json_str)
```

---

## Practical Exercises

### Exercise 1: Data Validation Module

Create a file named `data_validator.py`:
```python
# data_validator.py
"""Data validation utilities."""

import re
from typing import Union, List, Any

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    return cleaned.isdigit() and 10 <= len(cleaned) <= 15

def validate_age(age: Union[int, str], min_age: int = 0, max_age: int = 150) -> int:
    """Validate and return age."""
    try:
        age_int = int(age)
    except (ValueError, TypeError):
        raise ValidationError("Age must be a valid number")
    
    if age_int < min_age or age_int > max_age:
        raise ValidationError(f"Age must be between {min_age} and {max_age}")
    
    return age_int

def validate_json_schema(data: dict, schema: dict) -> bool:
    """Validate JSON data against a schema."""
    for key, expected_type in schema.items():
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        
        if not isinstance(data[key], expected_type):
            raise ValidationError(f"Key '{key}' must be of type {expected_type.__name__}")
    
    return True

# Test the validator
if __name__ == "__main__":
    # Test email validation
    test_emails = ["user@example.com", "invalid.email", "test@domain"]
    for email in test_emails:
        try:
            if validate_email(email):
                print(f"✓ Valid email: {email}")
            else:
                print(f"✗ Invalid email: {email}")
        except Exception as e:
            print(f"Error validating {email}: {e}")
    
    # Test age validation
    test_ages = [25, -5, "30", "abc", 200]
    for age in test_ages:
        try:
            validated_age = validate_age(age)
            print(f"✓ Valid age: {validated_age}")
        except ValidationError as e:
            print(f"✗ Invalid age {age}: {e}")
```

### Exercise 2: File Processing with Error Handling

Create a file named `file_processor.py`:
```python
# file_processor.py
"""File processing with comprehensive error handling."""

import json
import csv
import os
from typing import List, Dict, Any

class FileProcessingError(Exception):
    """Custom exception for file processing errors."""
    pass

def process_text_file(filename: str) -> Dict[str, Any]:
    """Process text file and return statistics."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        words = content.split()
        
        return {
            "filename": filename,
            "total_characters": len(content),
            "total_lines": len(lines),
            "total_words": len(words),
            "average_words_per_line": len(words) / len(lines) if lines else 0,
            "content": content[:100] + "..." if len(content) > 100 else content
        }
        
    except FileNotFoundError:
        raise FileProcessingError(f"File '{filename}' not found")
    except IOError as e:
        raise FileProcessingError(f"IO error reading '{filename}': {e}")
    except Exception as e:
        raise FileProcessingError(f"Unexpected error processing '{filename}': {e}")

def convert_csv_to_json(csv_filename: str, json_filename: str) -> bool:
    """Convert CSV file to JSON format."""
    try:
        # Read CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        # Write JSON file
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)
        
        print(f"Successfully converted {csv_filename} to {json_filename}")
        return True
        
    except FileNotFoundError:
        raise FileProcessingError(f"CSV file '{csv_filename}' not found")
    except csv.Error as e:
        raise FileProcessingError(f"CSV parsing error: {e}")
    except json.JSONDecodeError as e:
        raise FileProcessingError(f"JSON encoding error: {e}")
    except Exception as e:
        raise FileProcessingError(f"Conversion error: {e}")

def batch_process_files(file_list: List[str], output_dir: str) -> Dict[str, Any]:
    """Process multiple files and collect results."""
    results = {
        "successful": [],
        "failed": [],
        "total_files": len(file_list)
    }
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in file_list:
        try:
            if filename.endswith('.txt'):
                stats = process_text_file(filename)
                results["successful"].append({
                    "file": filename,
                    "type": "text",
                    "stats": stats
                })
            else:
                results["failed"].append({
                    "file": filename,
                    "error": "Unsupported file type"
                })
                
        except FileProcessingError as e:
            results["failed"].append({
                "file": filename,
                "error": str(e)
            })
        except Exception as e:
            results["failed"].append({
                "file": filename,
                "error": f"Unexpected error: {e}"
            })
    
    return results

# Test the file processor
if __name__ == "__main__":
    # Create sample files for testing
    sample_files = ['sample1.txt', 'sample2.txt', 'nonexistent.txt']
    
    # Create sample text files
    for i, filename in enumerate(sample_files[:2]):
        with open(filename, 'w') as f:
            f.write(f"This is sample file {i+1}\n" * 5)
    
    # Test batch processing
    results = batch_process_files(sample_files, 'output')
    
    print("\nBatch Processing Results:")
    print(f"Total files: {results['total_files']}")
    print(f"Successful: {len(results['successful'])}")
    print(f"Failed: {len(results['failed'])}")
    
    for success in results['successful']:
        print(f"✓ {success['file']}: {success['stats']['total_lines']} lines")
    
    for failure in results['failed']:
        print(f"✗ {failure['file']}: {failure['error']}")
```

---

## Summary

In this section, you learned:

- **Module System**: How to import, create, and organize Python modules and packages
- **Exception Handling**: Comprehensive error management with try/except/else/finally
- **File I/O**: Safe file reading and writing operations with proper encoding
- **JSON Processing**: Parsing and generating JSON data with validation
- **Custom Exceptions**: Creating and using your own exception types

## Next Steps

Now you're ready to move on to [Part 3: Conda Environments](./03_conda_environments.md), where you'll learn:

- Advanced Python concepts and best practices
- Code organization and structure
- Professional development techniques
- Real-world Python patterns

## Additional Resources

- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [JSON Module Documentation](https://docs.python.org/3/library/json.html)

**Practice these concepts by creating your own modules and handling real-world data processing scenarios!**
