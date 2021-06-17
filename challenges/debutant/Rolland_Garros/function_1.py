def main(data):
    points = data['points']
    compte = [0, 0, 0, 0]  # setD, setN, pointsD, pointsN

    for point in points:

        if point == "D":
            compte[2] = compte[2] + 1
        else:
            compte[3] = compte[3] + 1

        if compte[2] == 4:
            compte[0] += 1
            compte[2] = 0
            compte[3] = 0
        elif compte[3] == 4:
            compte[1] += 1
            compte[2] = 0
            compte[3] = 0
        else:
            pass

        if compte[1] == 6:
            compte = [0, 0, 0, 0]
        elif compte[0] == 6:
            compte = [0, 0, 0, 0]
        else:
            pass

    for x in [2, 3]:
        if compte[x] % 4 == 3:
            compte[x] = 40
        else:
            compte[x] = (compte[x] % 4) * 15

    return ":".join([str(x) for x in compte])
