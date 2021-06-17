def main(data):  # Exactement la meme que function_1.py mais en plus compresser
    pokemons = data['pokemons']

    return sum([
        max([int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Eau']),
        max([int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Herbe']),
        max([int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Feu']),
        max([int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] not in ['Eau', 'Herbe', 'Feu']])
    ])
