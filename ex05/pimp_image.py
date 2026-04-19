import numpy as np


def _validate_image(array: np.ndarray) -> None:
    """Validate that the input is a 3-channel RGB numpy array."""
    if not isinstance(array, np.ndarray):
        raise TypeError("image must be a numpy array")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("image must have shape (height, width, 3)")


def ft_invert(array: np.ndarray) -> np.ndarray | None:
    """Invert the colors of the image received."""
    try:
        _validate_image(array)
        return 255 - array
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray | None:
    """Keep only the red channel of the image."""
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 1] = result[:, :, 1] * 0
        result[:, :, 2] = result[:, :, 2] * 0
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray | None:
    """Keep only the green channel of the image."""
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
        result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray | None:
    """Keep only the blue channel of the image."""
    try:
        _validate_image(array)
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        return result
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray | None:
    """Convert the image to grey while keeping the same shape."""
    try:
        _validate_image(array)
        grey_channel = np.sum(array / 3, axis=2, keepdims=True)
        result = np.repeat(grey_channel, 3, axis=2)
        return result.astype(array.dtype)
    except Exception as error:
        print(f"Error: {error}")
        return None
