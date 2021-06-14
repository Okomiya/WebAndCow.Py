import base64
import json
import urllib.request


def display_errors(errors):
    for error in errors:
        print('Erreur : ' + error)


class Game:

    def __init__(self, key, code_engine):
        self.token = ''
        self.key = key
        self.code_engine = code_engine
        self.base_url = 'https://code-challenge.webandcow.com/'

    def get_game_data(self):
        data = self.request_api('games/launch/' + self.key + '/' + self.code_engine)
        self.token = data['token']

        data = self.request_api('games/init/' + self.token)
        return data['game']

    def push(self, player_data):
        if not player_data['reponse']:
            display_errors(['Votre tableau de retour doit contenir une cle "reponse"'])
            return

        player_data = base64.b64encode(json.dumps(player_data).encode('ascii')).decode('ascii')

        data = self.request_api('games/push/' + self.token + '/' + str(player_data))

        print('\n' + data['message'] + '\n' + 'Le token de ta Game : ' + self.base_url + 'games/story/' + self.token)

    def request_api(self, url):
        request = urllib.request.Request(self.base_url + url)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        if not data['success']:
            display_errors(data['errors'])
            return

        return data['data']