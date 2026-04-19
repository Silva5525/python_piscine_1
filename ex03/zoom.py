"""
zoom.py — Convert an image to grayscale, crop a square area,
and display the zoomed result.

Behavior:
    The program:
        1) loads the image using ft_load
        2) checks that the loaded object is a valid RGB NumPy array
        3) converts the image to grayscale
        4) crops a centered square area from the image
        5) prints the new shape and pixel content
        6) displays the zoomed grayscale image with axis labels

    If an error happens, it prints a clear error message
    and returns an empty NumPy array.
"""

# matplotlib.pyplot is used to display the image.
import matplotlib.pyplot as plt

# numpy is used for array checks and pixel manipulations.
import numpy as np

# ft_load is imported from load_image.py to load the source image.
from load_image import ft_load


def ft_zoom(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale and crop a square zoomed area.

    Parameters:
        array:
            A NumPy array representing an RGB image
            with shape (height, width, 3).

    Returns:
        A cropped grayscale NumPy array.
        If an error occurs, returns an empty NumPy array.
    """
    try:
        # Check that the input is really a NumPy array.
        if not isinstance(array, np.ndarray):
            raise TypeError("image must be a numpy array")

        # Reject empty arrays.
        if array.size == 0:
            raise ValueError("image is empty")

        # The exercise expects a color image with 3 channels.
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("image must have shape (height, width, 3)")

        # Convert the RGB image to grayscale.
        # The coefficients represent the visual importance
        # of red, green, and blue for human vision.
        grey = (
            0.2989 * array[:, :, 0]
            + 0.5870 * array[:, :, 1]
            + 0.1140 * array[:, :, 2]
        ).astype(np.uint8)

        # Define the size of the square crop.
        # It will be at most 400x400, but smaller if the image is smaller.
        crop_size = min(400, grey.shape[0], grey.shape[1])

        # Compute the top-left corner so the crop is centered.
        start_y = (grey.shape[0] - crop_size) // 2
        start_x = (grey.shape[1] - crop_size) // 2

        # Extract the centered square from the grayscale image.
        zoomed = grey[
            start_y:start_y + crop_size,
            start_x:start_x + crop_size
        ]

        # Print the shape and pixel values of the cropped image.
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed

    # Handle invalid type or invalid image content.
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return np.array([])


def display_image(array: np.ndarray) -> None:
    """Display the zoomed grayscale image with axis scale.

    Parameters:
        array:
            A NumPy array representing the grayscale image.
    """
    # Do nothing if the image is empty.
    if array.size == 0:
        return

    # Display the image in grayscale mode.
    plt.imshow(array, cmap="gray")

    # Add labels for the x and y axes.
    plt.xlabel("X axis")
    plt.ylabel("Y axis")

    # Show the image window.
    plt.show()


def main() -> None:
    """Load the image, zoom into it, and display the result."""
    # Load the original image from the file.
    image = ft_load("animal.jpeg")

    # Create the grayscale cropped version.
    zoomed = ft_zoom(image)

    # Display the final zoomed image.
    display_image(zoomed)


if __name__ == "__main__":
    main()
