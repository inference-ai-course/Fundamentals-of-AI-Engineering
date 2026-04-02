"""
Text Processing Functions
=========================

This file contains functions for processing text strings.
Use this to practice reading string manipulation code.
"""

def count_characters(text):
    """Count the total number of characters in text."""
    return len(text)


def count_words(text):
    """Count the number of words in text."""
    words = text.split()
    return len(words)


def uppercase(text):
    """Convert text to uppercase."""
    return text.upper()


def lowercase(text):
    """Convert text to lowercase."""
    return text.lower()


def capitalize_first(text):
    """Capitalize the first letter of text."""
    return text.capitalize()


def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return text.title()


def reverse_text(text):
    """Reverse the characters in text."""
    return text[::-1]


def remove_spaces(text):
    """Remove all spaces from text."""
    return text.replace(" ", "")


def replace_word(text, old_word, new_word):
    """Replace one word with another."""
    return text.replace(old_word, new_word)


def extract_numbers(text):
    """Extract all digit characters from text."""
    result = ""
    for char in text:
        if char.isdigit():
            result = result + char
    return result


def check_contains(text, substring):
    """Check if text contains a substring."""
    return substring in text


def get_first_n_characters(text, n):
    """Get the first n characters of text."""
    return text[:n]


def get_last_n_characters(text, n):
    """Get the last n characters of text."""
    return text[-n:]