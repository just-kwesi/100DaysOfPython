import requests
import datetime as dt


class FlightData:

    def __init__(self, config):
        self.URL = "https://api.tequila.kiwi.com/v2/search"
        self.request_header = {
            "apikey": config["KIWI_API_KEY"]
        }
        self.flights = []

    def getPrices(self, destination, stop_overs):
        today = dt.datetime.today()
        tomorrow = today + dt.timedelta(days=1)
        six_months_from_tomorrow = today + dt.timedelta(days=(6 * 31))

        request_params = {
            "fly_from": "NYC",
            "fly_to": destination["iataCode"],
            "data_from": tomorrow.strftime("%d/%m/%Y"),  # tomorrow,
            "date_to": six_months_from_tomorrow.strftime("%d/%m/%Y"),  # 6 months time
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 14,
            "curr": "USD",
            "limit": 10,
            "max_stopovers": stop_overs
        }

        response = requests.get(self.URL, headers=self.request_header, params=request_params)
        response.raise_for_status()
        flights = response.json()['data']

        if len(flights):
            self.checkForCheapFlight(flights, destination["lowestPrice"])
            return True
        return False

    def checkForCheapFlight(self, flights, lowest_price):
        for flight in flights:
            # if price of flight is less than price from Google sheets
            # append up to three flight to the flights list
            if flight["price"] <= lowest_price and len(self.flights) <= 2:
                self.flights.append(flight)
            else:
                break
