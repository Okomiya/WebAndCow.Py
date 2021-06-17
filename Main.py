#!/bin/python
from Game import Game
from secret_key import get_secret_key
from challenges.debutant.Batmobile_et_IA import engine_code, function_1


# Key personnelle
player_key = get_secret_key()
# Code du challenge
engine_code = engine_code.get_engine_code()


def main():
    game = Game(player_key, engine_code)
    data = game.get_game_data()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------

    reponse = function_1.main(data)

    # Permet d'envoyer la reponse du challenge
    game.push({'reponse': reponse})


main()