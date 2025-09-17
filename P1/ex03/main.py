from zoom import ft_zoom
from load_image import ft_load


def main():
    img = ft_load("animal.jpeg")
    ft_zoom(img)


if __name__ == "__main__":
    main()