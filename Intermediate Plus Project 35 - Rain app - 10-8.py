"""
Project Thirty-Five - Rain Notification App
This project looks at apis that require authentication, and then utilizes them in order to
notify us for when it's going to rain.
"""

import requests as rq

email = "dxxcfgaceasevutyln@uivvn.net"
password = ""

city_name = 'Brisbane'
state_code = 'QLD'
country_code = 'AUS'
API_key = '81b70ccacbcfd05369e64b939bb0af62'

api_endpoint =\
    f"http://api.openweathermap.org/data/2.5/weather" \
    f"?q={city_name},{state_code},{country_code}&appid={API_key}"

parameters = {
    'lat': -27.469,
    'lon': 153.0235,
    'appid': API_key,
    'exclude': 'current,minutely,daily'
}
api_endpoint2 = "https://api.openweathermap.org/data/2.5/onecall"
response = rq.get(api_endpoint2, params=parameters)
response.raise_for_status()
data = response.json()['hourly'][:12]
umb = False
list_ids = []
for i in range(len(data)):
    temp = data[i]['weather'][0]['id']
    list_ids.append(temp)
    if int(temp) < 700:
        umb = True

print(data)
if umb:
    print("Bring an umbrella")


# Can add either email functionality using SMTPLib or SMS using Twillio
