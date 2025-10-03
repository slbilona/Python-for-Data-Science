from abc import ABC, abstractmethod


class Character(ABC):
    """
    Classe abstraite représentant un personnage générique.

    Cette classe ne peut pas être instanciée directement.
    Elle sert de base aux différentes familles/personnages
    (ex: Stark, Lannister).

    Attributs :
        first_name (str) : le prénom du personnage
        is_alive (bool) : indique si le personnage est
        vivant (True) ou mort (False)
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initialise les attributs de base d'un personnage.

        Args:
            first_name (str) : le prénom du personnage
            is_alive (bool, optional) : True si le personnage est
                                        vivant, False sinon.
                                        Par défaut True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Marque le personnage comme mort.

        Modifie l'attribut `is_alive` pour le passer à False
        si le personnage est actuellement vivant.
        """
        if self.is_alive:
            self.is_alive = False


class Stark(Character):
    """
    Classe représentant un personnage de la maison Stark.

    Hérite de la classe Character.
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
