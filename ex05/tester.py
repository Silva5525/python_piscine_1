import matplotlib.pyplot as plt

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def show_image(title: str, array) -> None:
    """Display one image with a title."""
    if array is None:
        return
    plt.figure()
    plt.title(title)
    plt.imshow(array)
    plt.axis("on")
    plt.show()


def main() -> None:
    """Run all filters on the input image."""
    array = ft_load("landscape.jpg")
    if array is None:
        return

    show_image("Original", array)
    show_image("Invert", ft_invert(array))
    show_image("Red", ft_red(array))
    show_image("Green", ft_green(array))
    show_image("Blue", ft_blue(array))
    show_image("Grey", ft_grey(array))

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
