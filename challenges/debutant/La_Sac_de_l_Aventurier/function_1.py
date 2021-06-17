def main(data):
    sac = data['sac']
    objets = data['objets']
    adventurer = 0

    for listing in [list(sorted(objets, reverse=True)), list(sorted(objets))]:
        for objet in listing[:10]:
            if (sac - objet) >= 0:
                sac -= objet
                adventurer += objet
            else:
                break

    return adventurer
