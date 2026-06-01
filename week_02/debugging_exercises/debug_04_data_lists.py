"""List and dictionary debugging practice.

These examples prepare you for Week 3 data profiling. They use simple Python
data structures before pandas enters the course.
"""


def count_missing(values):
    # Expected: count None and empty strings as missing.
    missing = 0
    for value in values:
        if value is None:
            missing = missing + 1
    return missing


def get_column_names(profile):
    # Expected: return ["name", "age", "country"].
    return profile["column"]


def summarize_counts(counts):
    # Expected: {"total": 6, "unique": 3}
    total = 0
    for value in counts:
        total = total + value
    return {"total": total, "unique": len(counts)}


def main() -> None:
    print("Case 1: missing values")
    print("Expected 2, got:", count_missing(["US", "", None, "SG"]))

    print("\nCase 2: profile keys")
    profile = {"columns": ["name", "age", "country"]}
    try:
        print(get_column_names(profile))
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)

    print("\nCase 3: count summary")
    try:
        print("Expected {'total': 6, 'unique': 3}, got:", summarize_counts({"US": 3, "SG": 2, "CA": 1}))
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)


if __name__ == "__main__":
    main()
