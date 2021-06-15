def methode(data):  # DICTIONNAIRE ASSOCIATIF

    # On recupere les coups genérés aléatoirement de 'data'
    coups = data['coups']
    reponse = ""

    # Dictionnaire associatif donnant les coups à jouer selon ceux donnés
    associations = {
        "P": "F",
        "F": "C",
        "C": "P"
    }

    # Boucle 'for' en utilisant le dicionnaire
    for letter in coups:
        reponse += associations[letter]

    return reponse
