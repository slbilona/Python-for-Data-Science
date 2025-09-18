from PIL import Image
import numpy as np
from pathlib import Path


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image à partir d'un fichier JPEG et la convertit en tableau
    numpy.
    Paramètres:
        path (str): Chemin du fichier image à charger. Doit être un fichier
        '.jpg' ou '.jpeg'.
    Retour:
        np.ndarray: Image chargée sous forme de tableau numpy de type uint8
                    avec la forme (hauteur, largeur, 3) pour une image
                    couleur.
    Exceptions:
        TypeError: Si 'path' n'est pas une chaîne de caractères ou si
                   l'extension n'est pas '.jpg' ou '.jpeg'.
        FileNotFoundError: Si le fichier spécifié n'existe pas.
    """
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    ext = Path(path).suffix.lower()
    if ext not in [".jpg", ".jpeg"]:
        raise TypeError("path must be a '.jpg' or '.jpeg'")
    if not Path(path).exists():
        raise FileNotFoundError(f"Le fichier '{path}' n'existe pas")
    myimg = np.array(Image.open(path))
    print("The shape of image is: ", myimg.shape)
    print(myimg)
    return myimg
