import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, config):
        self.flights = []
        self.users = []
        self.URL = "https://api.sheety.co/c1a1a1c435cf5e09284c0a35de9c44b1/flightDeals/"
        self.request_header = {
            "Authorization": config["SHETTY_AUTH"]
        }

    def getFlight(self):
        response = requests.get(f"{self.URL}prices", headers=self.request_header)
        response.raise_for_status()
        result = response.json()
        self.flights = result["prices"]
        return self

    def postToFlight(self, city, lowest_price):
        request_body = {
            "price": {
                "city": city,
                "lowestPrice": lowest_price,
            }
        }
        response = requests.post(f"{self.URL}prices", headers=self.request_header, json=request_body)
        response.raise_for_status()
        return response.status_code

    def updateFlight(self, flight_id, flight_obj):
        put_url = f"{self.URL}/{flight_id}"
        requests_body = {
            "price": flight_obj
        }

        response = requests.put(f"{self.URL}prices", headers=self.request_header, json=requests_body)
        response.raise_for_status()
        return response.status_code

    def addUser(self, user):
        request_body = {
            "user": {
                "First Name": user["first_name"],
                "Last Name": user["last_name"],
                "Email": user["email"]
            }
        }

        response = requests.post(f"{self.URL}users", headers=self.request_header, json=request_body)
        response.raise_for_status()
        return response.status_code

    def getUsers(self):
        response = requests.get(f"{self.URL}users", headers=self.request_header)
        response.raise_for_status()
        result = response.json()
        self.users = result["users"]
        return self
