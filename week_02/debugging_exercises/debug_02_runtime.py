"""Runtime debugging practice.

These functions contain bugs that appear while code is running. Fix one section
at a time and rerun the file.
"""


def average(numbers):
    # Expected: average([10, 20, 30]) -> 20.0
    # Bug: average([]) crashes.
    return sum(numbers) / len(numbers)


def get_third_item(items):
    # Expected: get_third_item(["a", "b", "c"]) -> "c"
    # Bug: the current index asks for the fourth item.
    return items[3]


def first_letter(text):
    # Expected: first_letter("Python") -> "P"
    # Bug: None does not support indexing.
    return text[0]


def main() -> None:
    print("Case 1: empty average")
    print(average([]))

    print("Case 2: third item")
    print(get_third_item(["red", "green", "blue"]))

    print("Case 3: first letter")
    print(first_letter(None))


if __name__ == "__main__":
    main()
