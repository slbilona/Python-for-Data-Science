from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    img = ft_load("landscape.jpg")
    invertedImg = ft_invert(img)
    redImg = ft_red(img)
    greenImg = ft_green(img)
    blueImg = ft_blue(img)
    greyImg = ft_grey(img)
    plt.subplot(321)
    plt.imshow(img)
    plt.subplot(322)
    plt.imshow(invertedImg)
    plt.subplot(323)
    plt.imshow(redImg)
    plt.subplot(324)
    plt.imshow(greenImg)
    plt.subplot(325)
    plt.imshow(blueImg)
    plt.subplot(326)
    plt.imshow(greyImg)
    plt.show()
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
