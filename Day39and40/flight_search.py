import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, config):
        self.URL = "https://api.tequila.kiwi.com/locations/query"
        self.request_header = {
            "apikey": config["KIWI_API_KEY"]
        }

    def getIataCode(self, city):
        request_params = {
            'term': city,
            'limit': 1
        }

        response = requests.get(self.URL, headers=self.request_header, params=request_params)
        response.raise_for_status()

        return response.json()['locations']
