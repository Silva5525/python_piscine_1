"""
rotate.py — Convert an image to grayscale, crop a square area,
transpose it manually, and display the result.

Behavior:
    The program:
        1) loads the image using ft_load
        2) checks that the loaded object is a valid RGB NumPy array
        3) converts the image to grayscale
        4) crops a centered square area from the image
        5) prints the square image shape and pixel content
        6) transposes the image manually without using transpose helpers
        7) prints the new shape and pixel content after the transpose
        8) displays the transposed grayscale image with axis labels

    If an error happens, it prints a clear error message.
"""

# matplotlib.pyplot is used to display the image.
import matplotlib.pyplot as plt

# numpy is used for array validation and array creation.
import numpy as np

# ft_load is imported from load_image.py to load the source image.
from load_image import ft_load


def to_greyscale(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to a 2D greyscale array.

    Parameters:
        array:
            A NumPy array representing an RGB image
            with shape (height, width, 3).

    Returns:
        A 2D NumPy array containing the greyscale image.
    """
    # Check that the input is really a NumPy array.
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")

    # Reject empty arrays.
    if array.size == 0:
        raise ValueError("image is empty")

    # The exercise expects a color image with 3 channels.
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("image must have shape (height, width, 3)")

    # Convert the RGB image to greyscale.
    # The coefficients reflect the visual importance
    # of red, green, and blue for human vision.
    grey = (
        0.2989 * array[:, :, 0]
        + 0.5870 * array[:, :, 1]
        + 0.1140 * array[:, :, 2]
    ).astype(np.uint8)
    return grey


def crop_square(array: np.ndarray, size: int = 400) -> np.ndarray:
    """Crop a centered square from a 2D greyscale image.

    Parameters:
        array:
            A 2D NumPy array representing a greyscale image.
        size:
            The requested square size.

    Returns:
        A centered square crop from the image.
    """
    # Check that the input is really a NumPy array.
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")

    # Reject empty arrays.
    if array.size == 0:
        raise ValueError("image is empty")

    # Greyscale images must be 2D arrays.
    if array.ndim != 2:
        raise ValueError("greyscale image must be 2D")

    # The crop size must be a positive integer.
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")

    # Use the smallest allowed size so the crop always fits in the image.
    crop_size = min(size, array.shape[0], array.shape[1])

    # Compute the top-left corner so the crop is centered.
    start_y = (array.shape[0] - crop_size) // 2
    start_x = (array.shape[1] - crop_size) // 2

    # Return the centered square crop.
    return array[start_y:start_y + crop_size, start_x:start_x + crop_size]


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D array manually without transpose helpers.

    Parameters:
        array:
            A 2D NumPy array.

    Returns:
        A new NumPy array with rows and columns swapped.
    """
    # Check that the input is really a NumPy array.
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")

    # Reject empty arrays.
    if array.size == 0:
        raise ValueError("array is empty")

    # The transpose here is only defined for 2D arrays.
    if array.ndim != 2:
        raise ValueError("array must be 2D")

    # Read the number of rows and columns of the source array.
    rows = array.shape[0]
    cols = array.shape[1]

    # Create an empty result array with swapped dimensions.
    result = np.empty((cols, rows), dtype=array.dtype)

    # Fill the result manually:
    # the value at [i][j] becomes [j][i].
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            result[j][i] = array[i][j]
            j += 1
        i += 1
    return result


def display_image(array: np.ndarray) -> None:
    """Display the transposed greyscale image.

    Parameters:
        array:
            A 2D NumPy array representing the final image.
    """
    # Do nothing if the image is empty.
    if array.size == 0:
        return

    # Display the image in greyscale mode.
    plt.imshow(array, cmap="gray")

    # Add labels for the x and y axes.
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # Show the image window.
    plt.show()


def main() -> None:
    """Load, crop, transpose, print, and display the image."""
    try:
        # Load the original image from the file.
        image = ft_load("animal.jpeg")

        # Convert the image to greyscale.
        grey = to_greyscale(image)

        # Cut a centered square from the image.
        square = crop_square(grey, 400)

        # Print the shape and the pixel values before the transpose.
        print(f"The shape of image is: {square.shape}")
        print(square)

        # Transpose the square image manually.
        transposed = manual_transpose(square)

        # Print the new shape and pixel values after the transpose.
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Display the final transposed image.
        display_image(transposed)
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
