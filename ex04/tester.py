from load_image import ft_load
from rotate import to_greyscale, crop_square, manual_transpose, display_image
import numpy as np


def main() -> None:
    """Run tests for exercise 04."""

    # Test 1: Valid full workflow
    print("\n--- 1. Valid image workflow ---")
    image = ft_load("animal.jpeg")
    if image.size != 0:
        grey = to_greyscale(image)
        square = crop_square(grey, 400)
        print(f"The shape of image is: {square.shape}")
        print(square)

        transposed = manual_transpose(square)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        display_image(transposed)

    # Test 2: Missing file
    print("\n--- 2. Missing file ---")
    ft_load("missing.jpeg")

    # Test 3: Unsupported file extension
    print("\n--- 3. Unsupported extension ---")
    ft_load("animal.png")

    # Test 4: Invalid path type
    print("\n--- 4. Invalid path type ---")
    ft_load(42)

    # Test 5: Invalid input for grayscale conversion
    print("\n--- 5. Invalid grayscale input ---")
    try:
        to_greyscale("not an array")
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")

    # Test 6: Invalid input for square crop
    print("\n--- 6. Invalid crop input ---")
    try:
        crop_square(np.array([1, 2, 3]), 2)
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")

    # Test 7: Invalid input for manual transpose
    print("\n--- 7. Invalid transpose input ---")
    try:
        manual_transpose(np.array([1, 2, 3]))
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
