def main(data):
    kms = data['kms']
    runners = data['runners']
    stop = data['stop']

    distance_parcouru = stop

    for x in range(len(kms)):
        r = runners[x]
        distance_parcouru += r * (stop - kms[x])

    return distance_parcouru
