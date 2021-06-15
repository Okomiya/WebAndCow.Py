def methode(data):  # LIST & FOR

    # On recupere la data donnee 'armee'
    taille_des_ennemies = data['armee']

    # On cree une liste contenant chaque troupe de Daenerys sous forme ' [puissance, quantite_maximale] '
    armee_de_daenerys = [
        [1000, 3],  # Dragon    (troupes maximal à combattre : "1/3" )
        [15, 200],  # Immacule  (troupes maximal à combattre : "1/2" apres dragon)
        [1, 5000]  # Dothrakis (troupes maximal à combattre : "1/1" reste)
    ]

    # Nous sera utile pour diviser dans notre boucle 'for' (voir dans la liste 'armee_de_daenerys' ci-dessus)
    diviseur = 3

    # Creation d'une reponse en type 'list'
    reponse = []

    # Boucle 'for' pour chaqune des troupes de Daenerys
    for type_de_troupe in armee_de_daenerys:

        # On recupere la puissance, et la quantite maximale de la troupe choisie
        puissance = type_de_troupe[0]
        quantite_maximale = type_de_troupe[1]

        # On divise les troupes par le diviseur, puis par la puissance de la troupe
        # On recupere la donnee sous format 'int' car on n'utilise pas une moitié de dragon ¯\_(ツ)_/¯
        quantite_troupe = int(taille_des_ennemies / diviseur / puissance)

        # On verifie que la quantité de troupe qu'on utilisera ne dépasse pas la quantite maximale
        # que l'on peut déployer, si c'est le cas, on deployera le maximum de troupe que l'on peut.
        if quantite_troupe > quantite_maximale:
            quantite_troupe = quantite_maximale

        # On retire a l'armee ennemie les morts pour ne garder que le reste
        # On retire ensuite 1 au diviseur pour les operations suivantes
        taille_des_ennemies -= quantite_troupe * puissance
        diviseur -= 1

        # On ajoute a notre liste la quantite de troupe trouvée en String
        reponse.append(str(quantite_troupe))

    # La reponse doit être presentée sous forme 'X_XX_XX' donc on 'join' notre liste avec des '_'
    reponse = "_".join(reponse)

    return reponse
