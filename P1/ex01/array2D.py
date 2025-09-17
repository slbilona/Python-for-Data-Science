import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Retourne une tranche (slice) de la liste 'family' entre les indices 'start'
    et 'end'.

    Paramètres :
    ------------
    family : list
        Une liste d'éléments (chaque élément peut être de n'importe quel type).
    start : int
        L'indice de départ de la tranche (inclus). Peut être négatif.
    end : int
        L'indice de fin de la tranche (exclu). Peut être négatif.

    Retour :
    --------
    list
        Une nouvelle liste correspondant à la tranche family[start:end].

    Exceptions :
    ------------
    TypeError
        Si 'family' n'est pas une liste, ou si 'start'/'end' ne sont pas
        des entiers.
    IndexError
        Si 'start' ou 'end' sont en dehors des limites valides de la liste.
    """
    if not isinstance(family, list):
        raise TypeError("family should be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end should be integer")
    n = len(family)
    if start < -n or start >= n:
        raise IndexError("start hors limites")
    if end < -n or end > n:
        raise IndexError("end hors limites")
    arrFamily = np.array(family)
    print("My shape is :", arrFamily.shape)
    x = slice(start, end)
    print("My new shape is :", arrFamily[x].shape)
    return arrFamily[x].tolist()
