def main(data):
    group = data['group']
    scores = data['scores']

    reponse = dict(zip(group, [0 for i in range(len(group))]))

    for x in range(len(scores)):
        match = scores[x].split("_")

        if match[2] > match[3]:
            reponse[match[0]] += 3
        elif match[2] < match[3]:
            reponse[match[1]] += 3
        else:
            reponse[match[0]] += 1
            reponse[match[1]] += 1

    reponse = [p[0] for p in sorted(reponse.items(), key=lambda k: k[1], reverse=True)]

    return "".join(reponse)
