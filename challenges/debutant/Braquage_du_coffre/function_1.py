def main(data):
    depart = data['depart']
    chemin = data['chemin']

    for x in range(len(chemin)):
        p = 0
        for y in range(len(chemin[x])):
            p = 10 ** y

        if chemin[x][0] == "+":
            depart += p
        else:
            depart -= p

    return depart
