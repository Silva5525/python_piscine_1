"""
array2D.py — Slice a 2D list and display its shape.

Behavior:
    The program defines a function, slice_me, that:
        1) takes a 2D list
        2) prints its original shape
        3) returns a sliced version using start and end
        4) prints the new shape after slicing

    - The input must be a rectangular 2D list.
    - All rows must have the same length.
    - Errors are handled with clear messages.
    - Slicing is done with Python's slicing syntax.
"""


def _validate_2d_list(family: list) -> None:
    """Validate that family is a rectangular 2D list.

    Checks:
        - family must be a list
        - each row must also be a list
        - each row must have the same length

    Raises:
        TypeError: if family is not a list or not a 2D list
        ValueError: if rows do not all have the same size
    """
    # First check that the outer object is really a list.
    if not isinstance(family, list):
        raise TypeError("family must be a list")

    # An empty list is accepted: shape will simply be (0, 0).
    if len(family) == 0:
        return

    # Every element inside family must also be a list.
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")

    # Save the length of the first row as the reference size.
    row_length = len(family[0])

    # Compare every row to the reference size.
    for row in family:
        if len(row) != row_length:
            raise ValueError("all rows must have the same size")


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list and return a sliced version of it.

    Parameters:
        family:
            A rectangular 2D list.
        start:
            The starting index for slicing.
        end:
            The ending index for slicing.

    Returns:
        The sliced 2D list.
        If validation fails, returns an empty list.
    """
    try:
        # Validate the structure before doing any slicing.
        _validate_2d_list(family)

        # Compute the original shape: number of rows and columns.
        rows = len(family)
        cols = len(family[0]) if rows > 0 else 0
        print(f"My shape is : ({rows}, {cols})")

        # Slice the list using Python's built-in slicing syntax.
        new_family = family[start:end]

        # Compute the new shape after slicing.
        new_rows = len(new_family)
        new_cols = len(new_family[0]) if new_rows > 0 else cols
        print(f"My new shape is : ({new_rows}, {new_cols})")

        return new_family

    except (TypeError, ValueError) as error:
        # Print a clear error message instead of crashing.
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
