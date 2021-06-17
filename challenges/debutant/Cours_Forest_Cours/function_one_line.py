def main(data):
    kms = data['kms']
    runners = data['runners']
    stop = data['stop']

    return sum([runners[x] * (stop - kms[x]) for x in range(len(kms))]) + stop
