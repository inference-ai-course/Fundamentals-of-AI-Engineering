"""
Data Processing Functions
=========================

This file contains functions for processing lists of numbers.
Use this to practice reading more complex code.
"""

def calculate_sum(numbers):
    """Calculate the sum of all numbers in a list."""
    total = 0
    for num in numbers:
        total = total + num
    return total


def calculate_average(numbers):
    """Calculate the average of numbers in a list."""
    total = calculate_sum(numbers)
    count = len(numbers)
    if count == 0:
        return None
    return total / count


def find_minimum(numbers):
    """Find the smallest number in a list."""
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_maximum(numbers):
    """Find the largest number in a list."""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def filter_positive(numbers):
    """Return only the positive numbers from a list."""
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


def filter_negative(numbers):
    """Return only the negative numbers from a list."""
    result = []
    for num in numbers:
        if num < 0:
            result.append(num)
    return result


def count_occurrences(numbers, target):
    """Count how many times target appears in the list."""
    count = 0
    for num in numbers:
        if num == target:
            count = count + 1
    return count


def remove_duplicates(numbers):
    """Remove duplicate values from a list."""
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


def sort_numbers(numbers):
    """Sort numbers from smallest to largest."""
    return sorted(numbers)


def reverse_list(numbers):
    """Reverse the order of elements in a list."""
    return numbers[::-1]