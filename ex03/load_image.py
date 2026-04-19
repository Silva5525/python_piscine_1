from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image, print its shape, and return it as an RGB array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("only JPG and JPEG formats are supported")

        image = Image.open(path)
        image = image.convert("RGB")
        array = np.array(image)

        print(f"The shape of image is: {array.shape}")
        print(array)
        return array
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
    except PermissionError:
        print(f"Error: permission denied for '{path}'")
    except TypeError as error:
        print(f"TypeError: {error}")
    except ValueError as error:
        print(f"ValueError: {error}")
    except OSError:
        print(f"Error: '{path}' is not a valid image file")
    return np.array([])
