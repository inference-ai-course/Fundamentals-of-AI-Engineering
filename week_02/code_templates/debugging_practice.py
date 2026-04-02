"""
Debugging Practice
==================

This file contains code with intentional bugs.
Use this to practice debugging with AI assistance.

Instructions:
1. Try to run this file - you'll see errors
2. Ask AI to help you understand and fix each error
3. Document your fixes
"""

# Bug 1: Syntax error (missing colon)
def greet(name)
    print("Hello, " + name)


# Bug 2: Syntax error (incorrect indentation)
def add(a, b):
return a + b


# Bug 3: Runtime error (division by zero)
def divide(a, b):
    return a / b


# Bug 4: Type error (adding string and number)
def add_string_and_number(text, number):
    return text + number


# Bug 5: Index error (accessing beyond list bounds)
def get_third_element(items):
    return items[3]


# Bug 6: Logic error (wrong condition)
def is_greater_than_ten(value):
    return value < 10


# Bug 7: Logic error (wrong calculation)
def double_value(value):
    return value + value + value


# Bug 8: Missing return statement
def get_first_element(items):
    first = items[0]


# Bug 9: Incorrect function call
def calculate_square_and_cube(number):
    square = square_number(number)
    cube = cube_number(number)
    return square, cube


# Bug 10: Variable name mismatch
def print_user_info():
    name = "Alice"
    age = 25
    print("User: " + userName + ", Age: " + str(userAge))


# Helper functions that are correctly defined
def square_number(n):
    return n * n


def cube_number(n):
    return n * n * n