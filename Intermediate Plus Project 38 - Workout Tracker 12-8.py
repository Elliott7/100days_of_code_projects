"""
Project Thirty-Eight - Workout Tracker
Uses multiple APIs to figure out what the user is doing using natural language processing, then updates a
google sheet with that information
"""
import requests as rq
import datetime
from requests.auth import HTTPBasicAuth
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')


# Headers for Nutritionix website
HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}


get_response = input("What exercises did you do?")
parameters = {
    "query": get_response,
    'gender': 'male',
    'weight_kg': 80,
    'height_cm': 190,
    "age": 23
}

# Makes response to Nutritionix and saves the response
response = rq.post(API_END_POINT, json=parameters, headers=HEADERS)
result = response.json()

today = datetime.datetime.now()
date = (today.strftime("%d-%m-%Y"))
time = today.strftime('%T')

# Iterates through all of the responses and then sends the details to the google sheet document
for item in result['exercises']:
    exercise_var = item['name']
    duration_var = item['duration_min']
    calories_var = item['nf_calories']

    workout = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise_var,
            'duration': duration_var,
            'calories': calories_var,
        }
    }
    sh_headers = {
        "Authorization": BEARER_TOKEN
    }

    sheety_response = rq.post(
        SHEETY_ENDPOINT,
        json=workout,
        headers=sh_headers)
    sheety_result = sheety_response.json()
    print(sheety_result)



