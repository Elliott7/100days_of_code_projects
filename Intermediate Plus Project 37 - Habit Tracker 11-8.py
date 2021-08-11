"""
Project Thirty-Seven - Habit Tracker
Uses Pixela API to track habits. Essentially just using the API, haven't really integrated it into anything.
Will be good to add to a future project
"""
import requests
import os
import datetime as dt

USERNAME = "elliott"
TOKEN = os.environ.get('TOKEN')

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    'token': TOKEN,
    'username': 'elliott',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

pixela_graph_endpoint = "https://pixe.la/v1/users/elliott/graphs"

graph_params = {
    'id':'graph1',
    'name':'Tasks',
    'unit':'Completion',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers )
today = dt.datetime.now()
pixal_params = {
    'date':today.strftime("%Y%m%d"),
    'quantity': '1'
}
ep = "https://pixe.la/v1/users/elliott/graphs/graph1"
response = requests.post(url=ep, json=pixal_params, headers=headers)
print(response.text)

