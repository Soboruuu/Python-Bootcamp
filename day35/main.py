import requests
import os
from twilio.rest import Client

#Seoul
MY_LAT = 37.566536 
MY_LNG = 126.977966

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "YOUR_TWILIO_SID"
auth_token = "YOUR_TWILIO_TOKEN"
api_key = "YOUR_OPENWEATHERMAP_API_KEY"

parameters = {"lat": MY_LAT,
              "lon": MY_LNG,
              "appid": api_key,
              "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_12h = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_12h:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_="YOUR_TWILIO_NUMBER",
        to="YOUR_PHONE_NUMBER"
    )
    print(message.status)
