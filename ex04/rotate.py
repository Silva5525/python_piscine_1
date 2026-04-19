import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def to_greyscale(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to a 2D greyscale array."""
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")
    if array.size == 0:
        raise ValueError("image is empty")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("image must have shape (height, width, 3)")

    grey = (
        0.2989 * array[:, :, 0]
        + 0.5870 * array[:, :, 1]
        + 0.1140 * array[:, :, 2]
    ).astype(np.uint8)
    return grey


def crop_square(array: np.ndarray, size: int = 400) -> np.ndarray:
    """Crop a centered square from a 2D greyscale image."""
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")
    if array.size == 0:
        raise ValueError("image is empty")
    if array.ndim != 2:
        raise ValueError("greyscale image must be 2D")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")

    crop_size = min(size, array.shape[0], array.shape[1])
    start_y = (array.shape[0] - crop_size) // 2
    start_x = (array.shape[1] - crop_size) // 2
    return array[start_y:start_y + crop_size, start_x:start_x + crop_size]


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D array manually without transpose helpers."""
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if array.size == 0:
        raise ValueError("array is empty")
    if array.ndim != 2:
        raise ValueError("array must be 2D")

    rows = array.shape[0]
    cols = array.shape[1]
    result = np.empty((cols, rows), dtype=array.dtype)

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            result[j][i] = array[i][j]
            j += 1
        i += 1
    return result


def display_image(array: np.ndarray) -> None:
    """Display the transposed greyscale image."""
    if array.size == 0:
        return
    plt.imshow(array, cmap="gray")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main() -> None:
    """Load, crop, transpose, print, and display the image."""
    try:
        image = ft_load("animal.jpeg")
        grey = to_greyscale(image)
        square = crop_square(grey, 400)

        print(f"The shape of image is: {square.shape}")
        print(square)

        transposed = manual_transpose(square)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        display_image(transposed)
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
