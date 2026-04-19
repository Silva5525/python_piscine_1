import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray | None:
    """Load a JPG/JPEG image, print its shape and pixels, and return it."""
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
        print("Error: file not found")
    except Exception as error:
        print(f"Error: {error}")
    return None
