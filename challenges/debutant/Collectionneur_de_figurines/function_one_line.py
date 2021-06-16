def methode(data):  # Exotic One Line Method

    e = data['exemplaires']
    c = data['cotes']

    # on retourne la somme totale des deux compréhension de liste pour les deux cas (30 si < 2000 exemplaire et 15 si >= 2000)
    return sum([30 * y - 30 for x, y in zip(e, c) if x < 2000] + [15 * y - 15 for x, y in zip(e, c) if x >= 2000])
