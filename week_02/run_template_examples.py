"""Run simple Week 2 template functions.

This script gives beginners a concrete "run code first" checkpoint before
they start modifying or debugging Python files.
"""

from code_templates.data_processing import calculate_average, filter_positive
from code_templates.simple_math import add_numbers, divide_numbers
from code_templates.text_processing import count_words, uppercase


def main() -> None:
    print("add_numbers(2, 3) =", add_numbers(2, 3))
    print("divide_numbers(10, 2) =", divide_numbers(10, 2))
    print("count_words('AI helps me learn Python') =", count_words("AI helps me learn Python"))
    print("uppercase('hello ai') =", uppercase("hello ai"))
    print("calculate_average([10, 20, 30]) =", calculate_average([10, 20, 30]))
    print("filter_positive([-2, 0, 3, 5]) =", filter_positive([-2, 0, 3, 5]))


if __name__ == "__main__":
    main()
