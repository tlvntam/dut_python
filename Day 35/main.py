import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["AC142fe016328a50048f4b45234c8bbca9"]
auth_token = os.environ["b9766c52a0f254667686db8e49deebbd"]
api_key = "6d975a9e0737d1020dda6d00943777f9"
URL = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

weather_params = {
    "lat": 16.054407,
    "lon": 16.054407,
    "exclude": "hourly",
    "appid": api_key
}

weather_data = requests.get(URL, params=weather_params).json()
weather_data.raise_for_status()

"""Take 12 hours"""
weather_slice = weather_data["hourly"][:12]
# weather_code = weather_data["hourly"][0]["weather"][0]["id"]
wilL_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        wilL_rain = True
if wilL_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain.",
        from ="+12283386869",
        to="+84562361344"
    )
    print(message.status)
