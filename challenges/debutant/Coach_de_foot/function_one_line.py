def main(data):  # J'adore les methodes en une seule ligne

    # On recupere la data, et on cree une seconde liste trier dans l'ordre decroissant
    joueurs = data['joueurs']

    return "-".join([str(joueurs.index(x)) for x in list(reversed(sorted(joueurs)))[:11]])
