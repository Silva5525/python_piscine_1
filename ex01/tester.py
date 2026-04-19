from array2D import slice_me


def run_test(name: str, family, start: int, end: int) -> None:
    """Run one test case for slice_me."""
    print(f"\n--- {name} ---")
    result = slice_me(family, start, end)
    print(result)


def main() -> None:
    """Run all tests for exercise 01."""

    # Test 1: Official subject example
    run_test(
        "1. Subject example 1",
        [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2],
        ],
        0,
        2,
    )

    # Test 2: Official subject example with negative end
    run_test(
        "2. Subject example 2",
        [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2],
        ],
        1,
        -2,
    )

    # Test 3: Empty list
    run_test(
        "3. Empty list",
        [],
        0,
        1,
    )

    # Test 4: Non-list input
    run_test(
        "4. Invalid input type",
        "not a list",
        0,
        1,
    )

    # Test 5: Not a 2D list
    run_test(
        "5. Not a 2D list",
        [1, 2, 3],
        0,
        2,
    )

    # Test 6: Rows with different lengths
    run_test(
        "6. Different row sizes",
        [
            [1.80, 78.4],
            [2.15],
            [2.10, 98.5],
        ],
        0,
        2,
    )

    # Test 7: Full slice
    run_test(
        "7. Full slice",
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ],
        0,
        3,
    )

    # Test 8: Slice resulting in empty list
    run_test(
        "8. Empty slice result",
        [
            [1, 2],
            [3, 4],
        ],
        5,
        8,
    )


if __name__ == "__main__":
    main()
