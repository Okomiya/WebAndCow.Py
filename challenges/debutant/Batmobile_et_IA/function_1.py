def main(data):
    ennemis = data['ennemis']
    ennemis = sorted([[int(y[2:]), int(z[3:])] for y, z in [x.split(" ") for x in ennemis]])

    result = ""
    pos_bat = 0

    for eny in ennemis:
        pos_eny = eny[0]
        life = eny[1]

        while pos_eny > pos_bat:
            result += "D"
            pos_bat += 1

        while life > 0:
            result += "F"
            life -= 10

    return result
