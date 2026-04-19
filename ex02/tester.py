from load_image import ft_load


def main() -> None:
    """Run tests for exercise 02."""

    # Test 1: Valid JPG file
    print("\n--- 1. Valid JPG file ---")
    result = ft_load("landscape.jpg")
    print(type(result))

    # Test 2: Valid JPEG file
    print("\n--- 2. Valid JPEG file ---")
    result = ft_load("animal.jpeg")
    print(type(result))

    # Test 3: File does not exist
    print("\n--- 3. Missing file ---")
    ft_load("missing.jpg")

    # Test 4: Unsupported extension
    print("\n--- 4. Unsupported extension ---")
    ft_load("image.png")

    # Test 5: Invalid path type
    print("\n--- 5. Invalid path type ---")
    ft_load(123)


if __name__ == "__main__":
    main()
