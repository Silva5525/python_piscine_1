"""
pimp_image.py — Apply simple color filters to an RGB image.

Behavior:
    The module provides five filter functions:
        1) ft_invert: invert all colors of the image
        2) ft_red: keep only the red channel
        3) ft_green: keep only the green channel
        4) ft_blue: keep only the blue channel
        5) ft_grey: convert the image to grey while keeping the same shape

    Each function:
        - checks that the input is a valid RGB NumPy array
        - applies the requested transformation
        - returns the transformed image

    If an error happens, it prints a clear error message
    and returns None.
"""

# numpy is used for array validation and image manipulations.
import numpy as np


def _validate_image(array: np.ndarray) -> None:
    """Validate that the input is a 3-channel RGB NumPy array.

    Parameters:
        array:
            The image to validate.

    Raises:
        TypeError:
            If the input is not a NumPy array.
        ValueError:
            If the array does not have shape (height, width, 3).
    """
    # Check that the input is really a NumPy array.
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")

    # Check that the image has 3 dimensions
    # and exactly 3 color channels.
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("image must have shape (height, width, 3)")


def ft_invert(array: np.ndarray) -> np.ndarray | None:
    
    """Invert the colors of the image received.

    Parameters:
        array:
            A NumPy array representing an RGB image.

    Returns:
        The color-inverted image.
        None if an error occurs.
    """
    
    try:
        # Validate that the image has the correct format.
        _validate_image(array)

        # Invert each color value.
        # Example: 255 becomes 0, 0 becomes 255.
        return 255 - array
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray | None:
    """Keep only the red channel of the image.

    Parameters:
        array:
            A NumPy array representing an RGB image.

    Returns:
        The filtered image with only red information kept.
        None if an error occurs.
    """
    try:
        # Validate that the image has the correct format.
        _validate_image(array)

        # Make a copy so the original image stays unchanged.
        result = array.copy()

        # Remove the green and blue channels.
        result[:, :, 1] = result[:, :, 1] * 0
        result[:, :, 2] = result[:, :, 2] * 0
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray | None:
    """Keep only the green channel of the image.

    Parameters:
        array:
            A NumPy array representing an RGB image.

    Returns:
        The filtered image with only green information kept.
        None if an error occurs.
    """
    try:
        # Validate that the image has the correct format.
        _validate_image(array)

        # Make a copy so the original image stays unchanged.
        result = array.copy()

        # Remove the red and blue channels.
        result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
        result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray | None:
    """Keep only the blue channel of the image.

    Parameters:
        array:
            A NumPy array representing an RGB image.

    Returns:
        The filtered image with only blue information kept.
        None if an error occurs.
    """
    try:
        # Validate that the image has the correct format.
        _validate_image(array)

        # Make a copy so the original image stays unchanged.
        result = array.copy()

        # Remove the red and green channels.
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray | None:
    """Convert the image to grey while keeping the same shape.

    Parameters:
        array:
            A NumPy array representing an RGB image.

    Returns:
        A grey version of the image with 3 channels kept.
        None if an error occurs.
    """
    try:
        # Validate that the image has the correct format.
        _validate_image(array)

        # Compute one grey value per pixel by averaging the 3 channels.
        # keepdims=True keeps a third dimension of size 1.
        grey_channel = np.sum(array / 3, axis=2, keepdims=True)

        # Repeat the grey channel 3 times so the image keeps shape
        # (height, width, 3).
        result = np.repeat(grey_channel, 3, axis=2)
        return result.astype(array.dtype)
    except Exception as error:
        print(f"Error: {error}")
        return None
