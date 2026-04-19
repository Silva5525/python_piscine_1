from load_image import ft_load
from zoom import ft_zoom, display_image
import numpy as np


def main() -> None:
    """Run tests for exercise 03."""

    # Test 1: Valid image load and zoom
    print("\n--- 1. Valid image ---")
    image = ft_load("animal.jpeg")
    if image.size != 0:
        zoomed = ft_zoom(image)
        if zoomed.size != 0:
            display_image(zoomed)

    # Test 2: Missing file
    print("\n--- 2. Missing file ---")
    ft_load("missing.jpeg")

    # Test 3: Unsupported file extension
    print("\n--- 3. Unsupported extension ---")
    ft_load("animal.png")

    # Test 4: Invalid path type
    print("\n--- 4. Invalid path type ---")
    ft_load(42)

    # Test 5: Invalid input for ft_zoom
    print("\n--- 5. Invalid zoom input type ---")
    ft_zoom("not an array")

    # Test 6: Empty array for ft_zoom
    print("\n--- 6. Empty array ---")
    ft_zoom(np.array([]))

    # Test 7: Wrong image shape for ft_zoom
    print("\n--- 7. Wrong image shape ---")
    ft_zoom(np.array([[1, 2], [3, 4]]))


if __name__ == "__main__":
    main()
