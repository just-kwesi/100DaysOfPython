import requests
from dotenv import dotenv_values
import datetime as dt

CONFIG = dotenv_values('.env')


class FlightData:

    def __init__(self):
        self.URL = "https://api.tequila.kiwi.com/v2/search"
        self.request_header = {
            "apikey": CONFIG["KIWI_API_KEY"]
        }
        self.flights = []

    def getPrices(self, iata_code):
        today = dt.datetime.today()
        tomorrow = today + dt.timedelta(days=1)
        six_months_from_tomorrow = today + dt.timedelta(days=(6 * 31))

        request_params = {
            "fly_from": "NYC",
            "fly_to": iata_code,
            "data_from": tomorrow.strftime("%d/%m/%Y"),  # tomorrow,
            "date_to": six_months_from_tomorrow.strftime("%d/%m/%Y"),  # 6 months time
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 14,
            "curr": "USD",
            "limit": 75

        }

        response = requests.get(self.URL, headers=self.request_header, params=request_params)
        response.raise_for_status()
        if response.status_code == 200:
            self.flights = response.json()['data']
            return True
        return False



