# Loading.py

def ft_tqdm(lst: range) -> None:
    """
    fonction pour afficher l'avancer d'une boucle
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
