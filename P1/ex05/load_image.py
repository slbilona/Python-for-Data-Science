from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from rotate import ft_rotate


def ft_load(path: str) -> np.ndarray:
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    ext = Path(path).suffix.lower()
    if ext not in [".jpg", ".jpeg"]:
        raise TypeError("path must be a '.jpg' or '.jpeg'")
    if not Path(path).exists():
        raise FileNotFoundError(f"Le fichier '{path}' n'existe pas")
    myimg = np.array(Image.open(path))
    print("", myimg.shape)
    return myimg


def main():
    try:
        img = ft_load("animal.jpeg")
        zoomedImg = ft_zoom(img)
        rotatedImg = ft_rotate(zoomedImg)
        print(f"New shape after Transpose: {rotatedImg.shape}")
        print(rotatedImg)
        plt.imshow(rotatedImg, cmap='grey')
        plt.show()
    except Exception as error:
        print("Error :", error)


if __name__ == "__main__":
    main()
