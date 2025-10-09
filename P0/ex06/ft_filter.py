def ft_filter(function, object: any):
    """
    Filtre les éléments d'un itérable en appliquant une fonction de test.

    Cette fonction reproduit le comportement de la fonction intégrée `filter`.
    Elle parcourt chaque élément de l'itérable fourni et ne conserve que ceux
    pour lesquels la fonction passée en argument retourne une valeur évaluée
    comme vraie (True).

    Paramètres :
        function (callable) :
            Une fonction qui prend un élément de l'itérable en argument et
            retourne True si cet élément doit être conservé, False sinon.
        object (iterable) :
            Un objet itérable (liste, tuple, chaîne de caractères, etc.)
            contenant les éléments à filtrer.

    Retour :
        list :
            Une nouvelle liste contenant uniquement les éléments de l'itérable
            initial pour lesquels la fonction de test a renvoyé True.

    Exemple :
        >>> def est_pair(x): return x % 2 == 0
        >>> ft_filter(est_pair, [1, 2, 3, 4, 5])
        [2, 4]
    """
    return [x for x in object if function(x)]
