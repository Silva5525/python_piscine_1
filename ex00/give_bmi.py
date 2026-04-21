"""
give_bmi.py — Compute BMI values and compare them to a limit.

This module defines two main functions:

    give_bmi(height, weight)
        Takes two lists of numbers and returns a list of BMI values.

    apply_limit(bmi, limit)
        Takes a list of BMI values and returns a list of booleans,
        where each value is True if the BMI is above the given limit.

The module also includes small helper functions for input validation.
"""


def _is_number(value: object) -> bool:
    """Check whether a value is an int or float, but not a bool.

    Why exclude bool?
        In Python, bool is a subclass of int.
        That means True and False would otherwise count as numbers.
        For this exercise, we only want real numeric values.
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)


# This helper function validates both input lists before BMI calculation.
# It checks:
# - both arguments are lists
# - both lists have the same size
# - height values are valid positive numbers
# - weight values are valid non-negative numbers
def _validate_lists(
    height: list[int | float],
    weight: list[int | float],
) -> None:
    """Validate the inputs for BMI computation."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")

    # Check every height value.
    # Height must be numeric and greater than 0,
    # because BMI uses height² in the denominator.
    for h in height:
        if not _is_number(h):
            raise TypeError("height must contain only int or float values")
        if h <= 0:
            raise ValueError("height values must be greater than 0")

    # Check every weight value.
    # Weight must be numeric and cannot be negative.
    for w in weight:
        if not _is_number(w):
            raise TypeError("weight must contain only int or float values")
        if w < 0:
            raise ValueError("weight values must be non-negative")


# give_bmi pairs matching height and weight values using zip().
# For each pair, it computes:
#     BMI = weight / (height * height)
#
# If invalid input is found, the function prints the error type and message,
# then returns an empty list instead of crashing.
def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Return a list of BMI values from matching height and weight lists."""
    try:
        _validate_lists(height, weight)

        # List comprehension:
        # create one BMI value for each (height, weight) pair.
        return [w / (h * h) for h, w in zip(height, weight)]
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return []


# apply_limit checks whether each BMI value is above the given limit.
# Example:
#     bmi = [22.5, 29.0]
#     limit = 26
#     result = [False, True]
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value that is above the given limit."""
    try:
        # bmi must be a list.
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")

        # limit must be an int.
        # bool is excluded because True/False are also ints in Python.
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError("limit must be an int")

        # Each BMI value must be numeric.
        for value in bmi:
            if not _is_number(value):
                raise TypeError("bmi must contain only int or float values")

        # List comprehension:
        # compare every BMI value with the limit.
        return [value > limit for value in bmi]
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return []
