def _is_number(value: object) -> bool:
    """Check whether a value is an int or float, but not a bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _validate_lists(
    height: list[int | float],
    weight: list[int | float],
) -> None:
    """Validate the inputs for BMI computation."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")
    for h in height:
        if not _is_number(h):
            raise TypeError("height must contain only int or float values")
        if h <= 0:
            raise ValueError("height values must be greater than 0")
    for w in weight:
        if not _is_number(w):
            raise TypeError("weight must contain only int or float values")
        if w < 0:
            raise ValueError("weight values must be non-negative")


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Return a list of BMI values from matching height and weight lists."""
    try:
        _validate_lists(height, weight)
        return [w / (h * h) for h, w in zip(height, weight)]
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value that is above the given limit."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise TypeError("limit must be an int")
        for value in bmi:
            if not _is_number(value):
                raise TypeError("bmi must contain only int or float values")
        return [value > limit for value in bmi]
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return []


def main() -> None:
    """Run a simple test for exercise 00."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
