class calculator:
    """
    Classe fournissant des opérations de calcul sur des vecteurs.

    Les méthodes sont des méthodes de classe et effectuent des calculs
    entre deux vecteurs de même longueur.
    """

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """
        Calcule le produit scalaire (dot product) de deux vecteurs.

        Args:
            V1 (list[float]) : premier vecteur
            V2 (list[float]) : deuxième vecteur

        Affiche :
            Le résultat du produit scalaire.
        """
        i = 0
        for x, y in zip(V1, V2):
            i = (i + x * y)
        print("Dot product is:", i)

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        Additionne deux vecteurs élément par élément.

        Args:
            V1 (list[float]) : premier vecteur
            V2 (list[float]) : deuxième vecteur

        Affiche :
            La liste résultante de l'addition.
        """
        myList = []
        for x, y in zip(V1, V2):
            myList.append(x + y)
        print("Add Vector is :", myList)

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        Soustrait le deuxième vecteur du premier élément par élément.

        Args:
            V1 (list[float]) : premier vecteur
            V2 (list[float]) : deuxième vecteur

        Affiche :
            La liste résultante de la soustraction.
        """
        myList = []
        for x, y in zip(V1, V2):
            myList.append(x - y)
        print("Add Vector is :", myList)
