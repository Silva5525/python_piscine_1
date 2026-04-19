def _validate_2d_list(family: list) -> None:
    """Validate that family is a rectangular 2D list."""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if len(family) == 0:
        return
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")
    row_length = len(family[0])
    for row in family:
        if len(row) != row_length:
            raise ValueError("all rows must have the same size")


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list and return a sliced version of it."""
    try:
        _validate_2d_list(family)
        rows = len(family)
        cols = len(family[0]) if rows > 0 else 0
        print(f"My shape is : ({rows}, {cols})")

        new_family = family[start:end]
        new_rows = len(new_family)
        new_cols = len(new_family[0]) if new_rows > 0 else cols
        print(f"My new shape is : ({new_rows}, {new_cols})")
        return new_family
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return []


def main() -> None:
    """Run a simple test for exercise 01."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2],
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
