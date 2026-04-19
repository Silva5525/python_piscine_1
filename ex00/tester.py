# from give_bmi import give_bmi, apply_limit

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))


# My own tests for the exercise

from give_bmi import give_bmi, apply_limit


def run_test(
    name: str,
    height,
    weight,
    limit=None,
) -> None:
    """Run one test case and print the result."""
    print(f"\n--- {name} ---")
    bmi = give_bmi(height, weight)
    print("BMI:", bmi, type(bmi))
    if limit is not None:
        print("Above limit:", apply_limit(bmi, limit))


def main() -> None:
    """Run all tests for exercise 00."""

    # Test 1: Official example from the subject
    run_test(
        "1. Subject example",
        [2.71, 1.15],
        [165.3, 38.4],
        26,
    )

    # Test 2: Normal valid values
    run_test(
        "2. Normal valid values",
        [1.80, 1.65, 1.90],
        [80, 60, 100],
        25,
    )

    # Test 3: Empty lists
    run_test(
        "3. Empty lists",
        [],
        [],
        25,
    )

    # Test 4: Lists with different sizes
    run_test(
        "4. Different list sizes",
        [1.80, 1.70],
        [80],
        25,
    )

    # Test 5: Invalid type in height list
    run_test(
        "5. Invalid type in height",
        [1.80, "1.70"],
        [80, 70],
        25,
    )

    # Test 6: Invalid type in weight list
    run_test(
        "6. Invalid type in weight",
        [1.80, 1.70],
        [80, "70"],
        25,
    )

    # Test 7: Zero height
    run_test(
        "7. Zero height",
        [1.80, 0],
        [80, 70],
        25,
    )

    # Test 8: Negative height
    run_test(
        "8. Negative height",
        [1.80, -1.70],
        [80, 70],
        25,
    )

    # Test 9: Negative weight
    run_test(
        "9. Negative weight",
        [1.80, 1.70],
        [80, -70],
        25,
    )

    # Test 10: Direct valid test for apply_limit
    print("\n--- 10. Direct apply_limit valid test ---")
    print(apply_limit([22.5, 29.0, 18.2], 25))

    # Test 11: Invalid BMI content for apply_limit
    print("\n--- 11. Direct apply_limit invalid BMI content ---")
    print(apply_limit([22.5, "29.0", 18.2], 25))

    # Test 12: Invalid limit type for apply_limit
    print("\n--- 12. Direct apply_limit invalid limit type ---")
    print(apply_limit([22.5, 29.0, 18.2], 25.5))


if __name__ == "__main__":
    main()
