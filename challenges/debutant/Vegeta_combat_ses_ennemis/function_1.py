def main(data):
    ennemis = data['ennemis']
    force_vegeta = data['force_vegeta']
    level = 1

    for x in range(len(ennemis)):
        puissance = force_vegeta * level
        ennemi = ennemis[x]

        if puissance < ennemi:
            while (level * force_vegeta) < ennemi:
                level += 1

        force_vegeta += int(ennemi * 0.1)

    return force_vegeta * level
