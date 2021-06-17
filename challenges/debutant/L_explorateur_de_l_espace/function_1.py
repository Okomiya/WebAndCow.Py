def main(data):
    planetes = data['planetes']
    climat = data['climat']

    reponse = [p[:3] for p in planetes if climat in p[p.find(':') + 1:].replace(" ", "").split(',')]
    return "".join(reponse) if reponse else 'NOPLANET'
