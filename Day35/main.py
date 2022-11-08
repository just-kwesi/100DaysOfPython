import requests
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")

parameters = {
    "appid": config["APPID"],
    "lat": 40.664943,
    "lon": -73.882736,
    "units": "imperial"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)

print(response.status_code)
