import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(img: np.ndarray):
    y = slice(120, 520)
    x = slice(400, 800)
    z = slice(1, 2)
    zoomedImg = img[y, x, z]

    print(f"New shape after slicing: {zoomedImg.shape} "
          f"or {zoomedImg.shape[:2]}")
    print(zoomedImg)
    plt.imshow(zoomedImg, cmap='grey')
    plt.show()


def main():
    try:
        img = ft_load("animal.jpeg")
        print(img)
        ft_zoom(img)
    except Exception as error:
        print("Error :", error)


if __name__ == "__main__":
    main()
