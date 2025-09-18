import numpy as np


def ft_invert(img) -> np.ndarray:
    """
    Inverse les couleurs d'une image.

    Paramètres:
    -----------
        img (np.ndarray): Image en entrée au format tableau numpy (H, W, 3).

    Retour:
    -------
        np.nda
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("L'entrée doit être un tableau numpy (np.ndarray).")
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError("L'image doit être un tableau 3D avec 3 canaux"
                         "(H, W, 3).")
    return (255 - img)


def ft_red(img) -> np.ndarray:
    """
    Applique un filtre rouge à l'image.

    Paramètres :
    -----------
        img (np.ndarray): Image en entrée au format tableau numpy (H, W, 3).

    Retour:
    -------
        np.ndarray: Image filtrée en rouge.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("L'entrée doit être un tableau numpy (np.ndarray).")
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError("L'image doit être un tableau 3D avec 3 canaux"
                         "(H, W, 3).")
    redImg = img.copy()
    redImg[:, :, 1] = 0
    redImg[:, :, 2] = 0
    return (redImg)


def ft_green(img) -> np.ndarray:
    """
    Applique un filtre vert à l'image.

    Paramètres:
    -----------
        img (np.ndarray): Image en entrée au format tableau numpy (H, W, 3).

    Retour:
    -------
        np.ndarray: Image filtrée en vert.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("L'entrée doit être un tableau numpy (np.ndarray).")
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError("L'image doit être un tableau 3D avec 3 canaux"
                         "(H, W, 3).")
    greenImg = img.copy()
    greenImg[:, :, 0] = 0
    greenImg[:, :, 2] = 0
    return (greenImg)


def ft_blue(img) -> np.ndarray:
    """
    Applique un filtre bleu à l'image.

    Paramètres:
    -----------
        img (np.ndarray): Image en entrée au format tableau numpy (H, W, 3).

    Retour:
    -------
        np.ndarray: Image filtrée en bleu.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("L'entrée doit être un tableau numpy (np.ndarray).")
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError("L'image doit être un tableau 3D avec 3 canaux"
                         "(H, W, 3).")
    blueImg = img.copy()
    blueImg[:, :, 0] = 0
    blueImg[:, :, 1] = 0
    return (blueImg)


def ft_grey(img) -> np.ndarray:
    """
    Convertit l'image en niveaux de gris.

    Paramètres:
    -----------
        img (np.ndarray): Image en entrée au format tableau numpy (H, W, 3).

    Retour:
    -------
        np.ndarray: Image en niveaux de gris.
    """
    if not isinstance(img, np.ndarray):
        raise TypeError("L'entrée doit être un tableau numpy (np.ndarray).")
    if img.ndim != 3 or img.shape[2] != 3:
        raise ValueError("L'image doit être un tableau 3D avec 3 canaux"
                         "(H, W, 3).")
    grey = np.mean(img, axis=2, keepdims=True)
    grey = np.round(grey).astype(np.uint8)
    return np.repeat(grey, 3, axis=2)
