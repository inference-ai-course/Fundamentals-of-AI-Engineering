"""Logic debugging practice.

This file runs without crashing, but several answers are wrong. Use the expected
output printed next to the actual output to reason about the bug.
"""


def is_even(number):
    # Expected: True for even numbers, False for odd numbers.
    return number % 2 == 1


def calculate_discount(price, discount_percent):
    # Expected: 100 with 20 percent discount -> 80.0
    return price * discount_percent


def count_positive(numbers):
    # Expected: count only numbers greater than zero.
    count = 0
    for number in numbers:
        if number >= 0:
            count = count + 1
    return count


def main() -> None:
    print("Case 1: is_even")
    print("Expected True, got:", is_even(4))
    print("Expected False, got:", is_even(5))

    print("\nCase 2: calculate_discount")
    print("Expected 80.0, got:", calculate_discount(100, 20))

    print("\nCase 3: count_positive")
    print("Expected 2, got:", count_positive([-2, 0, 3, 5]))


if __name__ == "__main__":
    main()
