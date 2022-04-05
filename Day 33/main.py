"""API - Application Programming Interface"""
import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
"""httpstatuses.com"""
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude,latitude)
# print(iss_position)

MY_LAT = 16.054407
MY_LONG = 108.202164
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters).json()
# print(response)
sunrise = response["results"]["sunrise"].split("T")
print(sunrise)

time_now = datetime.now()
print(time_now.hour)