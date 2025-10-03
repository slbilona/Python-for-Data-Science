from S1E9 import Character


class Baratheon(Character):
    """
    Classe représentant un personnage de la maison Baratheon.

    Hérite de la classe abstraite Character. Définit des attributs spécifiques
    à la maison Baratheon comme family_name, yeux et cheveux.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un personnage Baratheon.

        Args:
            first_name (str) : le prénom du personnage
            is_alive (bool, optional) : True si le personnage est vivant,
                                        False sinon.
                                        Par défaut True.

        Raises:
            Exception : relance toute exception provenant de la classe parente.
        """
        try:
            super().__init__(first_name, is_alive)
            self.family_name = "Baratheon"
            self.eyes = "brown"
            self.hairs = "dark"
        except Exception as e:
            raise e

    def __str__(self):
        """
        Retourne une représentation lisible du personnage pour l'utilisateur.

        Returns:
            str : description lisible du personnage
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """
        Retourne une représentation technique du personnage pour le debug.

        Returns:
            str : description du personnage utilisable pour le debug
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"


class Lannister(Character):
    """
    Classe représentant un personnage de la maison Lannister.

    Hérite de la classe abstraite Character. Définit des attributs spécifiques
    à la maison Lannister comme family_name, yeux et cheveux, et fournit
    une méthode de classe pour créer des personnages.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialise un personnage Lannister.

        Args:
            first_name (str) : le prénom du personnage
            is_alive (bool, optional) : True si le personnage est vivant,
                                        False sinon.
                                        Par défaut True.

        Raises:
            Exception : relance toute exception provenant de la classe parente.
        """
        try:
            super().__init__(first_name, is_alive)
            self.family_name = "Lannister"
            self.eyes = "blue"
            self.hairs = "light"
        except Exception as e:
            raise e

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Crée une nouvelle instance de Lannister.

        Args:
            first_name (str) : le prénom du personnage
            is_alive (bool, optional) : True si le personnage est vivant,
                                        False sinon.
                                        Par défaut True.

        Returns:
            Lannister : nouvelle instance de Lannister
        """
        return cls(first_name, is_alive)

    def __str__(self):
        """
        Retourne une représentation lisible du personnage pour l'utilisateur.

        Returns:
            str : description lisible du personnage
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """
        Retourne une représentation technique du personnage pour le debug.

        Returns:
            str : description du personnage utilisable pour le debug
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"
