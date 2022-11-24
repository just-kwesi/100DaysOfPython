import requests
from dotenv import dotenv_values
import datetime as dt

config = dotenv_values(".env")

NUTRIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = config["NUTRIX_APP_ID"]
API_KEY = config["NUTRIX_API_KEY"]

exercises_done = input("Tell me which exercises you did: ")

request_body = {
    "query": exercises_done,
    "gender": "male",
    "weight_kg": 74.8427,
    "height_cm": 196.596,
    "age": 25
}
request_header = {
    "x-app-id": "795ed957",
    "x-app-key": "a9643acf2053df74713c5ce383064d94",
    "Content-Type": "application/json"
}

response = requests.post(NUTRIX_URL, json=request_body,headers=request_header)
response.raise_for_status()

print(response.json())
