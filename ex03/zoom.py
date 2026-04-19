import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def ft_zoom(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale and crop a square zoomed area."""
    try:
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

        crop_size = min(400, grey.shape[0], grey.shape[1])
        start_y = (grey.shape[0] - crop_size) // 2
        start_x = (grey.shape[1] - crop_size) // 2
        zoomed = grey[
            start_y:start_y + crop_size,
            start_x:start_x + crop_size
        ]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
        return np.array([])


def display_image(array: np.ndarray) -> None:
    """Display the zoomed grayscale image with axis scale."""
    if array.size == 0:
        return
    plt.imshow(array, cmap="gray")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main() -> None:
    """Load the image, zoom into it, and display the result."""
    image = ft_load("animal.jpeg")
    zoomed = ft_zoom(image)
    display_image(zoomed)


if __name__ == "__main__":
    main()
    