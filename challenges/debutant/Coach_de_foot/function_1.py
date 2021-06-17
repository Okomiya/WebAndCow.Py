def main(data):
    # On recupere la data, et on cree une seconde liste trier dans l'ordre decroissant
    jouers = data['joueurs']
    r_joueurs = list(reversed(sorted(jouers)))

    reponse = []

    # Boucle for avec les 11 premieres valeurs de notre seconde liste, puis on ajoute à
    # notre reponse l'index que possede notre valeur dans la liste originale
    for joueur in r_joueurs[:11]:
        reponse.append(str(jouers.index(joueur)))

    # On retourne reponse en joignant par des tiret.
    return "-".join(reponse)
