"""
Simple Math Functions
=====================

This file contains basic mathematical operations.
Use this to practice reading and understanding code.
"""

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b


def subtract_numbers(a, b):
    """Subtract the second number from the first."""
    return a - b


def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b


def divide_numbers(a, b):
    """Divide the first number by the second."""
    if b == 0:
        return None
    return a / b


def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent


def is_positive(number):
    """Check if a number is positive."""
    return number > 0


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def absolute_value(number):
    """Return the absolute value of a number."""
    if number < 0:
        return -number
    return number


def square(number):
    """Return the square of a number."""
    return number * number


def cube(number):
    """Return the cube of a number."""
    return number * number * number