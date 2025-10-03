from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Classe représentant un roi, héritant des maisons Baratheon et Lannister.

    Permet de gérer les attributs spécifiques comme la couleur des yeux
    et des cheveux, et de récupérer ces informations via des méthodes
    d’accès.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un roi avec un prénom et un statut de vie.

        Args:
            first_name (str) : le prénom du roi
            is_alive (bool, optional) : True si le roi est vivant, False sinon.
                                        Par défaut True.

        Raises:
            Exception : relance toute exception provenant des classes parentes
                        Baratheon et Lannister.
        """
        try:
            super().__init__(first_name, is_alive)
        except Exception as e:
            raise e

    def set_eyes(self, color: str):
        """
        Définit la couleur des yeux du roi.

        Args:
            color (str) : la couleur des yeux

        Raises:
            TypeError : si color n'est pas une chaîne
        """
        if not isinstance(color, str):
            raise TypeError("eyes color must be a str")
        self.eyes = color

    def set_hairs(self, color: str):
        """
        Définit la couleur des cheveux du roi.

        Args:
            color (str) : la couleur des cheveux

        Raises:
            TypeError : si color n'est pas une chaîne
        """
        if not isinstance(color, str):
            raise TypeError("hairs color must be a str")
        self.hairs = color

    def get_eyes(self):
        """
        Retourne la couleur des yeux du roi.

        Returns:
            str : couleur des yeux
        """
        return self.eyes

    def get_hairs(self):
        """
        Retourne la couleur des cheveux du roi.

        Returns:
            str : couleur des cheveux
        """
        return self.hairs
