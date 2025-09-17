import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calcule l'indice de masse corporelle (IMC) pour chaque paire taille/poids.

    Paramètres :
    ------------
    height : list[int | float]
        Liste des tailles en mètres.
    weight : list[int | float]
        Liste des poids en kilogrammes.
        Doit avoir la même longueur que 'height'.

    Retour :
    --------
    list[int | float]
        Liste des valeurs d'IMC calculées comme poids / (taille^2).

    Exceptions :
    ------------
    ValueError
        Si les listes 'height' et 'weight' n'ont pas la même longueur.
    TypeError
        Si un élément de 'height' ou 'weight' n'est pas un int ou un float.
    """
    if len(height) != len(weight):
        raise ValueError("Les listes doivent avoir la même taille.")
    for h, w in zip(height, weight):
        if not isinstance(h, (float, int)) or not isinstance(w, (int, float)):
            raise TypeError("seul les int ou float sont accepté")
    bmi = np.array(weight) / (np.array(height)**2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Retourne une liste de booléens indiquant quels IMC dépassent
    une limite donnée.

    Paramètres :
    ------------
    bmi : list[int | float]
        Liste des valeurs d'IMC.
    limit : int
        Valeur seuil d'IMC pour la comparaison.

    Retour :
    --------
    list[bool]
        Liste de booléens. True si l'IMC correspondant dépasse 'limit',
        False sinon.
    """
    bmiBool = np.array(bmi) > limit
    return bmiBool.tolist()
