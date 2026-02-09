# Part 1: Python Fundamentals

## Overview

Python is the lingua franca of AI and data science. Understanding its fundamentals deeply isn't just about syntax—it's about thinking in Python's paradigm. This section covers the essential building blocks that will serve as your foundation for AI engineering, machine learning, and data science work.

---

## Why Python for AI Engineering?

### The AI Language of Choice

Python dominates AI/ML for compelling reasons:

1. **Readability = Rapid Prototyping**
   - Clear syntax accelerates experimentation
   - Less time debugging, more time innovating
   - Easy to share research code with colleagues

2. **Rich Ecosystem**
   - [NumPy](https://numpy.org/doc/), [Pandas](https://pandas.pydata.org/docs/) for data manipulation
   - [TensorFlow](https://www.tensorflow.org/api_docs), [PyTorch](https://pytorch.org/docs/) for deep learning
   - [Scikit-learn](https://scikit-learn.org/stable/) for classical ML
   - [Hugging Face](https://huggingface.co/docs) for LLMs

3. **Community & Resources**
   - Massive AI/ML community
   - Extensive tutorials and documentation
   - Active research code sharing (GitHub, papers)

4. **Industry Standard**
   - Most AI job postings require Python
   - Research papers include Python implementations
   - Production ML systems built with Python

**Think of Python as:** The glue that connects data, algorithms, and deployment in the AI pipeline.

---

## Table of Contents
1. [Variables and Basic Types](#variables-and-basic-types)
2. [Data Structures](#data-structures)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Practical Exercises](#practical-exercises)

---

## Variables and Basic Types

### Understanding Dynamic Typing

Python uses **dynamic typing**, meaning variables are not bound to specific types. This is fundamentally different from statically-typed languages like Java or C++.

**What this means:**
```
Static typing (Java):  int age = 25;        // age MUST be integer
Dynamic typing (Python): age = 25           # age can be anything
                         age = "twenty-five" # Now it's a string!
```

**Trade-offs:**
- ✅ **Pros**: Faster prototyping, more flexible code, less boilerplate
- ⚠️ **Cons**: Runtime type errors, requires more testing, can be confusing

**How Python manages this:**
```
Variable Name  →  Reference  →  Object (with type)
    age              ↓              25 (int)
                   0x1a2b3c      [value: 25, type: int]
```

Every Python object knows its own type. Variables are just labels pointing to objects.

---

### Basic Variable Assignments

```python
# Integer
age = 25
temperature = -10

# Float
pi = 3.14159
price = 29.99

# String
name = "Alice"
message = 'Hello, World!'

# Boolean
is_student = True
has_permission = False

# None type (represents absence of value)
result = None
```

### Type Checking and Conversion

```python
# Check variable types
print(f"age is {type(age)}: {age}")
print(f"pi is {type(pi)}: {pi}")
print(f"name is {type(name)}: {name}")
print(f"is_student is {type(is_student)}: {is_student}")

# Type conversion
str_number = "42"
int_number = int(str_number)           # Convert string to int
float_number = float(str_number)       # Convert string to float
str_from_int = str(42)                 # Convert int to string

print(f"Converted: {str_number} -> {int_number} -> {float_number}")
```

### String Operations

```python
# String formatting
name = "Alice"
age = 30

# f-strings (recommended)
introduction = f"My name is {name} and I am {age} years old."

# String methods
text = "  Python Programming  "
cleaned = text.strip()                 # Remove whitespace
uppercase = text.upper()               # Convert to uppercase
lowercase = text.lower()               # Convert to lowercase
replaced = text.replace("Python", "Java")

print(f"Original: '{text}'")
print(f"Cleaned: '{cleaned}'")
print(f"Uppercase: '{uppercase}'")
```

---

## Data Structures

### The Right Tool for the Job

Python provides several built-in data structures, each optimized for specific use cases. Choosing the right one dramatically affects performance and code clarity.

**Quick Decision Guide:**

```
Need ordered sequence that changes?     → List
Need fast lookups by key?               → Dictionary  
Need immutable sequence?                → Tuple
Need unique items only?                 → Set
```

**Performance Characteristics:**

| Operation          | List      | Dict      | Tuple     | Set       |
|--------------------|-----------|-----------|-----------|-----------|
| Access by index    | O(1)      | N/A       | O(1)      | N/A       |
| Search             | O(n)      | O(1)      | O(n)      | O(1)      |
| Insert/Delete      | O(n)      | O(1)      | N/A       | O(1)      |
| Memory usage       | Medium    | High      | Low       | Medium    |

**Real-world analogy:**
- **List**: Shopping list (ordered, can modify)
- **Dictionary**: Phone book (quick name → number lookup)
- **Tuple**: GPS coordinates (fixed, never change)
- **Set**: Guest list at event (unique names, no duplicates)

---

### Lists - Ordered, Mutable Collections

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

# List operations
numbers.append(6)                      # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)                   # Insert at position: [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])                 # Add multiple items: [0, 1, 2, 3, 4, 5, 6, 7, 8]
removed = numbers.pop()                # Remove and return last: returns 8
numbers.remove(3)                      # Remove first occurrence of 3

# List slicing
first_three = numbers[:3]              # [0, 1, 2]
last_two = numbers[-2:]                # Last two elements
reversed_list = numbers[::-1]          # Reverse the list
every_second = numbers[::2]            # Every second element

print(f"Numbers: {numbers}")
print(f"First three: {first_three}")
print(f"Reversed: {reversed_list}")
```

**List Comprehensions:**
```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Complex example
words = ["hello", "world", "python", "programming"]
long_words = [word.upper() for word in words if len(word) > 5]
print(f"Long words (uppercase): {long_words}")
```

### Dictionaries - Key-Value Mappings

```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "San Francisco",
    "skills": ["Python", "Data Science"]
}

# Dictionary operations
person["email"] = "alice@example.com"   # Add new key
age = person.get("age", 0)              # Get with default
keys = list(person.keys())              # Get all keys
values = list(person.values())          # Get all values

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(5)}
print(f"Squared numbers: {squared_numbers}")

# Nested dictionary access
contacts = {
    "alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "bob": {"phone": "098-765-4321", "email": "bob@example.com"}
}

alice_phone = contacts["alice"]["phone"]
print(f"Alice's phone: {alice_phone}")
```

### Tuples - Ordered, Immutable Sequences

```python
# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)                     # Note the comma for single-item tuple

# Tuple unpacking
x, y = coordinates
red, green, blue = rgb_color

print(f"Coordinates: x={x}, y={y}")
print(f"RGB: R={red}, G={green}, B={blue}")

# Named tuples for better readability
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: x={p.x}, y={p.y}")

# Returning multiple values from function
def get_min_max(numbers):
    return min(numbers), max(numbers)

values = [3, 7, 2, 9, 1]
min_val, max_val = get_min_max(values)
print(f"Min: {min_val}, Max: {max_val}")
```

### Sets - Unique, Unordered Collections

```python
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
duplicates_removed = set([1, 2, 2, 3, 3, 3])
empty_set = set()                       # Note: {} creates an empty dict

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union = set_a | set_b                   # {1, 2, 3, 4, 5}
intersection = set_a & set_b            # {3}
difference = set_a - set_b              # {1, 2}
symmetric_diff = set_a ^ set_b          # {1, 2, 4, 5}

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

# Set methods
set_a.add(6)                            # Add element
set_a.remove(2)                         # Remove element (raises KeyError if not found)
set_a.discard(10)                       # Remove element (no error if not found)

# Practical use: removing duplicates
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Original: {numbers_with_duplicates}")
print(f"Unique: {sorted(unique_numbers)}")
```

---

## Control Flow

Control flow statements allow you to control the execution order of your code.

### Conditional Statements

```python
# if/elif/else structure
temperature = 25

if temperature > 30:
    print("It's hot outside!")
    activity = "swimming"
    recommendation = "Stay hydrated!"
elif temperature > 20:
    print("Nice weather!")
    activity = "walking"
    recommendation = "Perfect for outdoor activities!"
else:
    print("It's cool!")
    activity = "reading"
    recommendation = "Good time for indoor activities!"

print(f"Suggested activity: {activity}")
print(f"Recommendation: {recommendation}")

# Ternary operator (conditional expression)
status = "warm" if temperature > 20 else "cool"
print(f"The weather is {status}")
```

### Loops

```python
# for loops with different iterables
fruits = ["apple", "banana", "orange"]

# Basic for loop
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop with enumerate starting from 1
for index, fruit in enumerate(fruits, 1):
    print(f"Fruit {index}: {fruit}")

# Loop with range
print("Counting to 5:")
for i in range(5):                      # 0, 1, 2, 3, 4
    print(f"Count: {i}")

print("Counting from 1 to 5:")
for i in range(1, 6):                   # 1, 2, 3, 4, 5
    print(f"Count: {i}")

print("Counting by 2s:")
for i in range(0, 10, 2):               # 0, 2, 4, 6, 8
    print(f"Even number: {i}")
```

**while loops:**
```python
# Basic while loop
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1

# while loop with break and continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

print("Searching for target:")
i = 0
while i < len(numbers):
    if numbers[i] < 5:
        i += 1
        continue                      # Skip to next iteration
    
    print(f"Checking {numbers[i]}")
    
    if numbers[i] == target:
        print(f"Found target: {target}")
        break                         # Exit loop
    
    i += 1
else:
    print("Target not found")         # Executes if loop completes without break
```

**Nested loops:**
```python
# Multiplication table
print("Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i} × {j} = {product}")
    print()  # Empty line after each row
```

---

## Functions

### Why Functions Matter

Functions are the fundamental building blocks of organized, reusable code. They transform programming from writing scripts into building systems.

**The Power of Functions:**

```
Without Functions (Script Thinking):
─────────────────────────────────────
code line 1
code line 2
code line 3
... 
code line 1000
→ Hard to understand, impossible to reuse, difficult to test

With Functions (System Thinking):
──────────────────────────────────
function load_data()
function clean_data()
function analyze_data()
function visualize_results()
→ Clear purpose, reusable, testable, maintainable
```

**Key Benefits:**
1. **DRY Principle**: Don't Repeat Yourself - write once, use everywhere
2. **Abstraction**: Hide complexity behind simple interfaces
3. **Testing**: Test individual components independently
4. **Collaboration**: Team members work on different functions
5. **Debugging**: Isolate problems to specific functions

**In AI/ML Context:**
```python
# Bad: Everything in one place
data = pd.read_csv('data.csv')
data = data.dropna()
data['feature'] = data['feature'] / data['feature'].max()
model = LinearRegression()
model.fit(X, y)
...

# Good: Organized into functions
data = load_and_validate_data('data.csv')
data = preprocess_data(data)
model = train_model(data)
results = evaluate_model(model, test_data)
```

---

### Basic Function Definition

```python
def greet(name):
    """Return a greeting message.
    
    Args:
        name (str): The person's name
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"

# Using the function
message = greet("Alice")
print(message)

# Function without return value (returns None)
def log_message(message):
    """Print a message with timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

log_message("System started")
```

### Function Parameters

```python
# Function with default parameters
def calculate_area(length, width=1):
    """Calculate rectangle area.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle (default: 1)
        
    Returns:
        float: Area of rectangle
    """
    return length * width

# Using default parameter
print(f"Square area: {calculate_area(5)}")           # width defaults to 1
print(f"Rectangle area: {calculate_area(5, 3)}")     # width = 3

# Function with multiple return values
def get_stats(numbers):
    """Return min, max, and average of a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        tuple: (min, max, average) or (None, None, None) if empty
    """
    if not numbers:
        return None, None, None
    
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Unpacking multiple return values
values = [1, 2, 3, 4, 5]
min_val, max_val, avg = get_stats(values)
print(f"Stats - Min: {min_val}, Max: {max_val}, Avg: {avg:.2f}")
```

### Function with Type Hints (Python 3.5+)

```python
from typing import List, Dict, Optional, Union

def process_data(data: List[float]) -> Dict[str, float]:
    """Process a list and return statistics.
    
    Args:
        data: List of float numbers
        
    Returns:
        Dictionary with count, sum, and average
    """
    if not data:
        return {}
    
    return {
        "count": len(data),
        "sum": sum(data),
        "average": sum(data) / len(data)
    }

def find_item(items: List[str], target: str) -> Optional[int]:
    """Find index of target item in list.
    
    Args:
        items: List of strings to search
        target: Target string to find
        
    Returns:
        Index of target or None if not found
    """
    try:
        return items.index(target)
    except ValueError:
        return None

def flexible_function(value: Union[int, float, str]) -> str:
    """Handle multiple input types.
    
    Args:
        value: Can be int, float, or str
        
    Returns:
        String representation
    """
    return str(value)

# Usage examples
numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
stats = process_data(numbers)
print(f"Statistics: {stats}")

fruits = ["apple", "banana", "orange"]
index = find_item(fruits, "banana")
print(f"Banana index: {index}")

result = flexible_function(42)
print(f"Flexible result: {result}")
```

### Variable Scope

```python
# Global variable
global_counter = 0

def increment_global():
    """Increment global counter."""
    global global_counter              # Declare we're using global variable
    global_counter += 1
    return global_counter

def local_scope_example():
    """Demonstrate local scope."""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global counter: {global_counter}")

# Usage
print(f"Initial global: {global_counter}")
increment_global()
increment_global()
print(f"After increments: {global_counter}")

local_scope_example()
# print(local_var)  # This would raise NameError - local_var not accessible here
```

---

## Practical Exercises

### Exercise 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Test the functions
temperatures_c = [0, 20, 25, 30, 100]
temperatures_f = [32, 68, 77, 86, 212]

print("Celsius to Fahrenheit:")
for c in temperatures_c:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.1f}°F")

print("\nFahrenheit to Celsius:")
for f in temperatures_f:
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.1f}°C")
```

### Exercise 2: Shopping Cart Calculator

```python
def calculate_total(items, tax_rate=0.08):
    """Calculate total with tax.
    
    Args:
        items: List of (item_name, price) tuples
        tax_rate: Tax rate as decimal (default 0.08)
        
    Returns:
        Dictionary with subtotal, tax, and total
    """
    subtotal = sum(price for _, price in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    return {
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

# Test the function
shopping_cart = [
    ("Apples", 3.99),
    ("Bread", 2.50),
    ("Milk", 4.25),
    ("Eggs", 3.75)
]

result = calculate_total(shopping_cart)
print("Shopping Cart Summary:")
print(f"Subtotal: ${result['subtotal']:.2f}")
print(f"Tax (8%): ${result['tax']:.2f}")
print(f"Total: ${result['total']:.2f}")
```

### Exercise 3: Grade Analyzer

```python
def analyze_grades(grades):
    """Analyze a list of grades.
    
    Args:
        grades: List of numerical grades (0-100)
        
    Returns:
        Dictionary with analysis results
    """
    if not grades:
        return {"error": "No grades provided"}
    
    # Calculate statistics
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Count grades by letter
    letter_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for grade in grades:
        if grade >= 90:
            letter_counts["A"] += 1
        elif grade >= 80:
            letter_counts["B"] += 1
        elif grade >= 70:
            letter_counts["C"] += 1
        elif grade >= 60:
            letter_counts["D"] += 1
        else:
            letter_counts["F"] += 1
    
    return {
        "count": len(grades),
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "letter_distribution": letter_counts
    }

# Test the function
test_grades = [85, 92, 78, 88, 95, 67, 89, 91, 73, 84]
analysis = analyze_grades(test_grades)

print("Grade Analysis:")
print(f"Total students: {analysis['count']}")
print(f"Average grade: {analysis['average']}")
print(f"Highest grade: {analysis['highest']}")
print(f"Lowest grade: {analysis['lowest']}")
print("\nLetter grade distribution:")
for letter, count in analysis['letter_distribution'].items():
    print(f"  {letter}: {count} students")
```

---

## Summary

### Core Concepts Mastered

✅ **Variables and Dynamic Typing**
- Python's dynamic typing system and how it differs from static languages
- Basic types: integers, floats, strings, booleans, None
- Type conversion and string formatting with f-strings

✅ **Data Structures**
- **Lists**: Ordered, mutable sequences for dynamic collections
- **Dictionaries**: Fast key-value lookups for structured data
- **Tuples**: Immutable sequences for fixed data
- **Sets**: Unique collections with mathematical operations
- Performance trade-offs and choosing the right structure

✅ **Control Flow**
- Conditional logic with if/elif/else
- Iteration with for and while loops
- Loop control with break, continue, and else
- List comprehensions for concise transformations

✅ **Functions**
- Organizing code into reusable, testable components
- Parameters: positional, keyword, default values
- Type hints for better documentation and IDE support
- Variable scope: local vs global

### Key Takeaways

1. **Choose the Right Data Structure**: Performance matters
   - O(1) lookups with dicts and sets
   - O(n) searches with lists and tuples
   - Memory vs speed trade-offs

2. **Write Pythonic Code**: Embrace Python idioms
   - Use list comprehensions for transformations
   - Leverage f-strings for formatting
   - Follow the Zen of Python (explicit > implicit, readability counts)

3. **Think in Functions**: Organize early
   - Small, focused functions with single responsibility
   - Document with docstrings and type hints
   - Test individual components

4. **AI/ML Context**: These fundamentals power:
   - Data preprocessing with lists and dicts
   - Model configuration with dictionaries
   - Batch processing with loops and comprehensions
   - Pipeline organization with functions

### Common Patterns in AI/ML

```python
# Data loading
data = load_dataset(path)

# Preprocessing
data = [normalize(x) for x in data if validate(x)]

# Training loop
for epoch in range(num_epochs):
    for batch in dataloader:
        loss = train_step(batch)
        
# Evaluation
results = {
    'accuracy': accuracy_score(y_true, y_pred),
    'f1': f1_score(y_true, y_pred)
}
```

These patterns appear everywhere in AI code!

## Next Steps

Now that you have a solid foundation in Python fundamentals, you're ready to move on to [Part 2: Modules and Exception Handling](./02_modules_exceptions.md), where you'll learn about:

- Organizing code into modules
- Handling errors gracefully
- Working with files and JSON data
- Creating robust applications

## Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Python Basics](https://realpython.com/python-basics/)

**Practice these concepts by modifying the exercises and creating your own examples!**
