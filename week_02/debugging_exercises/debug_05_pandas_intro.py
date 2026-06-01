"""Optional pandas debugging practice.

Run this only after Week 2 environment setup succeeds. It previews common Week 3
data issues: missing columns, wrong dtypes, and missing values.
"""

import pandas as pd


def average_age(df):
    # Bug: the DataFrame uses "age", not "Age".
    return df["Age"].mean()


def add_total_score(df):
    # Bug: quiz_score contains strings, so + does string concatenation.
    df["total_score"] = df["quiz_score"] + 10
    return df


def count_missing_country(df):
    # Bug: this checks only None, not pandas missing values.
    count = 0
    for value in df["country"]:
        if value is None:
            count = count + 1
    return count


def main() -> None:
    df = pd.DataFrame(
        {
            "name": ["Ada", "Grace", "Katherine"],
            "age": [22, 35, 29],
            "quiz_score": ["80", "90", "85"],
            "country": ["US", None, pd.NA],
        }
    )

    print("Case 1: average age")
    try:
        print(average_age(df))
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)

    print("\nCase 2: total score")
    try:
        print(add_total_score(df)[["name", "total_score"]])
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)

    print("\nCase 3: missing country")
    try:
        print("Expected 2, got:", count_missing_country(df))
    except Exception as exc:
        print(type(exc).__name__ + ":", exc)


if __name__ == "__main__":
    main()
