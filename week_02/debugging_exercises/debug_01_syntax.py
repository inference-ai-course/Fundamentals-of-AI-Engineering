"""Syntax and indentation debugging practice.

Each exercise uses exec() so one syntax error does not prevent the rest of the
file from loading. Fix one code string at a time, rerun, and document the error.
"""


def run_case(title: str, code: str) -> None:
    print("\n===", title, "===")
    try:
        exec(code)
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)


run_case(
    "missing colon",
    """
def greet(name)
    return "Hello, " + name

print(greet("Ada"))
""",
)


run_case(
    "bad indentation",
    """
def add(a, b):
return a + b

print(add(2, 3))
""",
)


run_case(
    "unclosed string",
    """
message = "AI helps me debug
print(message)
""",
)


print("\nFix each code string until every case prints the expected result.")
