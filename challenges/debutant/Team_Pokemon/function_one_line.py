def methode(data):  # Theoriquement ... One line

    # On recupere la data
    types = data['types']

    # Comme la methode_1 mais avec des comprehension list et en une ligne
    return min([
        len([x for x in types if x == "Eau"]),
        len([x for x in types if x == "Feu"]),
        len([x for x in types if x == "Herbe"]),
        len([x for x in types if x not in ["Eau", "Feu", "Herbe"]]),
    ])
