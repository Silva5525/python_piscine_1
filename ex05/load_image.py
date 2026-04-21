"""
load_image.py — Load a JPG or JPEG image as an RGB array.

Behavior:
    The function ft_load:
        1) checks that the path is a string
        2) checks that the file extension is .jpg or .jpeg
        3) opens the image
        4) converts it to RGB format
        5) converts it into a NumPy array
        6) prints the shape and pixel content
        7) returns the array

    If an error happens, it prints a clear error message
    and returns None.
"""

# Image from PIL is used to open and convert image files.
from PIL import Image

# numpy is used to convert the image into an array of pixels.
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Load an image, print its shape, and return it as an RGB array.

    Parameters:
        path:
            The path to the image file.

    Returns:
        A NumPy array in RGB format if the image is loaded successfully.
        None if an error occurs.
    """
    try:
        # Check that the given path is really a string.
        if not isinstance(path, str):
            raise TypeError("path must be a string")

        # Accept only JPG and JPEG files for this exercise.
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("only JPG and JPEG formats are supported")

        # Open the image file.
        image = Image.open(path)

        # Convert the image to RGB so it always has 3 color channels.
        image = image.convert("RGB")

        # Transform the image into a NumPy array.
        array = np.array(image)

        # Print the shape and the full pixel content.
        print(f"The shape of image is: {array.shape}")
        print(array)

        return array

    # Error if the file does not exist.
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")

    # Error if the program is not allowed to access the file.
    except PermissionError:
        print(f"Error: permission denied for '{path}'")

    # Error for wrong argument type.
    except TypeError as error:
        print(f"TypeError: {error}")

    # Error for unsupported extension or invalid value.
    except ValueError as error:
        print(f"ValueError: {error}")

    # Error if the file exists but is not a valid image.
    except OSError:
        print(f"Error: '{path}' is not a valid image file")

    return None
