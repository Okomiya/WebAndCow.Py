def methode(data):
    exemplaires = data['exemplaires']
    cotes = data['cotes']

    achat = 0
    valeur = 0

    for x in range(len(exemplaires)):
        price = 0
        cote = cotes[x]

        if exemplaires[x] < 2000:
            price = 30
        else:
            price = 15

        achat += price
        valeur += (price * cote)

    return valeur - achat
