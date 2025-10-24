def ft_tqdm(lst: range) -> None:
    """
    Affiche une barre de progression pour suivre l'avancement d'une boucle.

    Cette fonction imite le comportement de `tqdm` en Python :
    - Elle affiche une barre de progression en blocs '█' proportionnelle
      à l'avancement de l'itération.
    - Elle renvoie les éléments un par un grâce au `yield`,
      permettant de l'utiliser dans une boucle `for`.

    Paramètres :
    -----------
    lst : range
        Une séquence (range ou liste) sur laquelle la boucle va itérer.

    Comportement :
    --------------
    - Affiche le pourcentage complété et la barre graphique.
    - La barre se met à jour sur la même ligne grâce à `\r`.
    - À la fin de l'itération, la barre passe à la ligne suivante.

    Exemple :
    --------
    >>> for elem in ft_tqdm(range(10)):
    ...     import time
    ...     time.sleep(0.1)
    10%|█████                                             | 1/10
    ...
    100%|█████████████████████████████████████████████████| 10/10
    """
    total = len(lst)
    bar_length = 55  # longueur de la barre de progression

    for i, elem in enumerate(lst, 1):
        percent = i / total
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        # print avec \r et end="" pour rester sur la même ligne
        print(f"\r{int(percent*100)}%|{bar}| {i}/{total}", end="")
        yield elem
    print()  # saut de ligne final


MORSE_CODE_DICT = {' ': '/',
                   'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----', }


def ft_match(c):
    """
    Retourne la valeur Morse correspondant à un caractère donné.

    Paramètres :
    -----------
    c : str
        Un caractère alphanumérique unique (lettre ou chiffre).

    Retour :
    -------
    str
        La représentation Morse du caractère.

    Exceptions :
    ------------
    AssertionError
        Si le caractère n'est pas présent dans MORSE_CODE_DICT.

    Exemple :
    --------
    >>> match('A')
    '.-'
    >>> match('@')
    AssertionError: caractère non reconnu
    """
    if MORSE_CODE_DICT.get(c):
        return MORSE_CODE_DICT.get(c)
    else:
        raise AssertionError("caractère non reconnu")


def ft_morse(string: str) -> str:
    """
    Transforme une chaîne de caractères alphanumérique en Morse
    et la retourne sous forme de chaîne.

    Paramètres :
    -----------
    string : str
        La chaîne à convertir en Morse. Les lettres seront converties
        en majuscules.

    Retour :
    -------
    str
        Une chaîne contenant les caractères Morse séparés par des espaces.

    Comportement :
    --------------
    - Convertit tous les caractères en majuscules.
    - Utilise la fonction `match` pour obtenir la représentation Morse.
    - Si un caractère n'est pas reconnu, affiche un message d'erreur
    et retourne None.

    Exemple :
    --------
    >>> ft_morse("Hello")
    '.... . .-.. .-.. ---'

    >>> ft_morse("Hello@")
    AssertionError: caractère non reconnu
    """
    try:
        upperString = string.upper()
        myList = [MORSE_CODE_DICT[c] for c in upperString if ft_match(c)]
        delimiter = ' '
        ret = delimiter.join(myList)
        return ret
    except AssertionError as error:
        print("AssertionError:", error)


def ft_filter(function, object: any) -> list:
    """
    Applique une fonction de filtrage à un objet itérable et retourne une liste
    contenant uniquement les éléments pour lesquels la fonction retourne True.

    Paramètres :
    -----------
    function : callable
        Une fonction qui prend un élément de l'objet et retourne True ou False.
    object : any (itérable)
        Un objet itérable (liste, tuple, range, etc.) dont les éléments
        seront filtrés.

    Retour :
    -------
    list
        Une nouvelle liste contenant uniquement les éléments de 'object' pour
        lesquels 'function' retourne True.

    Exemple :
    --------
    >>> def is_even(n):
    ...     return n % 2 == 0
    >>> ft_filter(is_even, [1, 2, 3, 4])
    [2, 4]
    """
    return [x for x in object if function(x)]
