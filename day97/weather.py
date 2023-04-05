import requests
import os


class OpenWeatherMap():
    def __init__(self):
        #Seoul
        self.MY_LAT = 37.566536
        self.MY_LNG = 126.977966

        self.OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
        self.api_key = os.environ.get('OPENWEATHERMAP_API')

        self.parameters = {"lat": self.MY_LAT,
                      "lon": self.MY_LNG,
                      "appid": self.api_key,
                      "exclude": "current,minutely,daily"
        }

    def call(self):
        response = requests.get(url=self.OWM_Endpoint, params=self.parameters)
        response.raise_for_status()
        weather_data = response.json()
        weather_12h = weather_data["hourly"][:12]

        will_rain = False

        for hour_data in weather_12h:
            condition_code = hour_data["weather"][0]["id"]
            if int(condition_code) < 700:
                will_rain = True

        if will_rain:
            message = "It's going to rain today. Remember to bring an umbrella!"
        else:
            message = "There will be no rain today."
        return message

