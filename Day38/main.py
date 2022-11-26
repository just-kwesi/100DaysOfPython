import requests
from dotenv import dotenv_values
import datetime as dt

config = dotenv_values(".env")

APP_ID = config["NUTRIX_APP_ID"]
API_KEY = config["NUTRIX_API_KEY"]
SHEETY_AUTH = config["SHETTY_AUTH"]

NUTRIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/c1a1a1c435cf5e09284c0a35de9c44b1/pythonWorkoutProject/workouts"


def main():
    exercises_done = input("Tell me which exercises you did: ")
    exercise = getExercise(exercises_done)
    post_to_sheety_rows = postToRows(exercise)

    return 0



def getExercise(exercises_done):
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

    response = requests.post(NUTRIX_URL, json=request_body, headers=request_header)
    response.raise_for_status()
    return response.json()


def postToRows(rows_data):
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%I:%M:%S %p")

    response_list = []
    request_header = {
        "Authorization": SHEETY_AUTH
    }
    for exercise in rows_data["exercises"]:

        request_body = {
            "workout": {
                'date': date,
                'time': time,
                'exercise': exercise["name"],
                'duration': exercise["duration_min"],
                'calories': exercise["nf_calories"]
            }
        }

        response = requests.post(SHEETY_URL, headers=request_header, json=request_body)
        response.raise_for_status()
        response_list.append(response.status_code)

    return response_list


def getRows():
    request_header = {
        "Authorization": SHEETY_AUTH
    }
    response = requests.get(SHEETY_URL, headers=request_header)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    main()
