from PIL import Image
import numpy as np
from pathlib import Path


def ft_load(path: str) -> np.ndarray:
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    ext = Path(path).suffix.lower()
    if ext not in [".jpg", ".jpeg"]:
        raise TypeError("path must be a '.jpg' or '.jpeg'")
    if not Path(path).exists():
        raise FileNotFoundError(f"Le fichier '{path}' n'existe pas")
    myimg = np.array(Image.open(path))
    print("The shape of image is: ", myimg.shape)
    return myimg
