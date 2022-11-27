import requests
from dotenv import dotenv_values

CONFIG = dotenv_values('.env')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flights = []
        self.URL = "https://api.sheety.co/c1a1a1c435cf5e09284c0a35de9c44b1/flightDeals/prices"
        self.request_header = {
            "Authorization": CONFIG["SHETTY_AUTH"]
        }

    def getFlight(self):
        response = requests.get(self.URL, headers=self.request_header)
        response.raise_for_status()
        result = response.json()
        self.flights = result["prices"]
        return self.flights

    def postToFlight(self, city, lowest_price):
        request_body = {
            "price": {
                "city": city,
                "lowestPrice": lowest_price,
                "iataCode": "XXX"

            }
        }
        response = requests.post(self.URL, headers=self.request_header, json=request_body)
        response.raise_for_status()
        return response.status_code

    def updateFlight(self, flight_id, flight_obj):
        put_url = f"{self.URL}/{flight_id}"
        requests_body = {
            "price" : flight_obj
        }

        response = requests.put(put_url, headers=self.request_header, json=requests_body)
        response.raise_for_status()
        return response.status_code
