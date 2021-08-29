import requests
import configparser


class faceit:

    def __init__(self):
        self.baseUrl = 'https://open.faceit.com/data/v4'
        self.cfg = configparser.ConfigParser()
        self.cfg.read('cfg.cfg')
        self.session = requests.Session()
        self.session.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + self.cfg['faceit']['client_key']
        }

    def championship(self, game='csgo', type='all', offset=0, limit=10):
        """
        :param game: The id of the game
        :param type: Kind of matches to return. Can be all(default), upcoming, ongoing or past
        :param offset: The starting item position
        :param limit: The number of items to return
        :return: Retrieve all championships of a game
        """
        params = {
            'game': game,
            'type': type,
            'offset': offset,
            'limit': limit
        }
        r = self.session.get(self.baseUrl + '/championships', params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return print(f'An error occured №:' + str(r.status_code))

    def detailsChampionships(self, championship_id: str, expanded: str):
        """
        :param championship_id: The id of the championship
        :param expanded: List of entity names to expand in request. Allowed: organizer and game
        :return: Retrieve championship details
        """

        params = {
            'expanded': expanded
        }

        r = self.session.get(self.baseUrl + f'/championships/{championship_id}', params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return print(f'An error occured №:' + str(r.status_code))

    def championshipsMatches(self, championship_id=None, type='all', offset=0, limit=20):
        """
        :param championship_id: The id of the championship
        :param type: Kind of matches to return. Can be all(default), upcoming, ongoing or past. Available values : all, upcoming, ongoing, past
        :param offset: The starting item position. Default value: 0
        :param limit: The number of items to return. Default value: 20
        :return: Retrieve all matches of a championship
        """
        params = {
            'type': type,
            'offset': offset,
            'limit': limit
        }
        r = self.session.get(self.baseUrl + f'/championships/{championship_id}/matches', params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return print(f'An error occured №:' + str(r.status_code))

    def championshipSubscriptions(self, championship_id=None, offset=0, limit=10):
        """
        :param championship_id: The id of the championship
        :param offset: The starting item position. Default value : 0
        :param limit: The number of items to return. Default value : 10
        :return: Retrieve all subscriptions of a championship
        """
        params = {
            'offset': offset,
            'limit': limit
        }
        r = self.session.get(self.baseUrl + f'/championships/{championship_id}/subscriptions', params=params)
        if r.status_code == 200:
            return r.json()
        else:
            return print(f'An error occured №:' + str(r.status_code))