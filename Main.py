#!/bin/python
from Game import Game
from secret_key import get_secret_key
from challenges.debutant.PIERRE_FEUILLE_CISEAUX import engice_code, methode_1, methode_2

# Key personnelle
player_key = get_secret_key()
# Code du challenge
engine_code = engice_code.get_engice_code()


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------

    reponse = methode_2.dictionnaire(data)


    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()