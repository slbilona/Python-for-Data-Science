def callLimit(limit: int):
    """
    Crée un décorateur qui limite le nombre d'appels d'une fonction.

    Paramètres :
        limit (int) : le nombre maximum d'appels autorisés pour
        la fonction décorée.

    Retourne :
        function : un décorateur qui limite le nombre d'appels.
    """
    count = 0

    def callLimiter(function):
        """
        Décorateur qui applique la limite d'appels à la fonction passée
        en argument.

        Paramètres :
            function (callable) : la fonction à décorer.

        Retourne :
            function : la version décorée de la fonction avec limitation
            d'appels.
        """

        def limit_function(*args: any, **kwds: any):
            """
            Fonction décorée qui vérifie si le nombre d'appels a dépassé
            la limite.

            Paramètres :
                *args : arguments positionnels à passer à la fonction originale
                **kwds : arguments nommés à passer à la fonction originale

            Retourne :
                le résultat de la fonction originale si la limite n'est pas
                atteinte, None sinon.
            """
            try:
                nonlocal count
                if limit < 0:
                    raise TypeError("Error : limit must be greater than 0")
                if count >= limit:
                    raise Exception(f"Error: {function} call too many times")
                count += 1
                return function(*args, **kwds)
            except Exception as e:
                print(e)
                return None
        return limit_function
    return callLimiter
