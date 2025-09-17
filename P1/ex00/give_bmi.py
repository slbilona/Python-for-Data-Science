import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Les listes doivent avoir la même taille.")
    for h, w in zip(height, weight):
        if not isinstance(h, (float, int)) or not isinstance(w, (int, float)):
            raise TypeError("seul les int ou float sont accepté")
    bmi = np.array(weight) / (np.array(height)**2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmiBool = np.array(bmi) > limit
    return bmiBool.tolist()
