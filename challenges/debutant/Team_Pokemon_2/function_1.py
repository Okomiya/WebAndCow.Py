def main(data):
    pokemons = data['pokemons']

    type_eau = [int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Eau']
    type_herbe = [int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Herbe']
    type_feu = [int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] == 'Feu']
    type_rare = [int(t[t.index(':') + 1:]) for t in pokemons if t[:t.index(':')] not in ['Eau', 'Herbe', 'Feu']]

    return max(type_eau) + max(type_herbe) + max(type_feu) + max(type_rare)
