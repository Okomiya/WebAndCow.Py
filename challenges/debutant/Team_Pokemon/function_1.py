def methode(data):  # list + min

    # On recupere la data
    types = data['types']
    # On cree une liste pour stocker la quantite par type
    equipe = [0, 0, 0, 0]

    # boucle for pour enumerer les types disponibles
    for t in types:
        if t == "Eau":
            equipe[0] += 1
        elif t == "Feu":
            equipe[1] += 1
        elif t == "Herbe":
            equipe[2] += 1
        else:
            equipe[3] += 1

    # On retourne le minimum d'equipe faisable
    return min(equipe)
