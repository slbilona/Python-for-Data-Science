def ft_tqdm(lst: range) -> None:
    """
    fonction pour afficher l'avancer d'une boucle
    """
    total = len(lst)
    longueur_barre = 70

    for i, elem in enumerate(lst, 1):
        percent = i / total
        long_remplissage = int(longueur_barre * percent)
        bar = '█' * long_remplissage + ' ' * (longueur_barre
                                              - long_remplissage)
        # print avec \r et end="" pour rester sur la même ligne
        print(f"\r{int(percent*100)}%|{bar}| {i}/{total}", end="")
        yield elem
    print()  # saut de ligne final
