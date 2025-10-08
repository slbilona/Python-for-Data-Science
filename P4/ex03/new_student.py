import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Génère un identifiant aléatoire composé de 15 lettres minuscules.

    Retourne :
        str : un identifiant unique de 15 caractères.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Classe représentant un étudiant. Chaque étudiant a un nom, un prénom,
    un statut actif, un login et un identifiant unique.
    'name' et 'surname' sont obligatoires à l'initialisation.
    'active' est True par défaut,
    'login' est généré automatiquement à partir du nom et du prénom,
    'id' est généré automatiquement par generate_id().
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default="")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Méthode appelée automatiquement après l'initialisation de l'objet.
        Vérifie que le nom et le prénom ne sont pas vides et génère le login.

        Format du login : première lettre du nom en majuscule + prénom
        en minuscules.
        """
        try:
            if len(self.name) <= 0:
                raise Exception("Name cannot be empty")
            if len(self.surname) <= 0:
                raise Exception("Surname cannot be empty")
            self.login = self.name[0].upper() + self.surname.lower()
        except Exception as e:
            print("AssertionError:", e)
