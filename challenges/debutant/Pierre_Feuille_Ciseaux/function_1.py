def main(data):  # IF SUCCESSIFS

    # On recupere les coups genérés aléatoirement de 'data'
    coups = data['coups']
    reponse = ""

    # Boucle 'for' pour chaque coup avec une succession de conditions qui ajoute le coup à jouer à 'reponse'
    for coup in coups:
        if coup == "P":
            reponse += "F"
        elif coup == "F":
            reponse += "C"
        else:
            reponse += "P"

    return reponse
