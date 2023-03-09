import requests
import datetime as dt
import smtplib
import time

# ISS DATA
api_endpoint="http://api.open-notify.org/iss-now.json"
response = requests.get(url=api_endpoint)
response.raise_for_status()
iss_longitude = response.json()["iss_position"]["longitude"]
iss_latitude = response.json()["iss_position"]["latitude"]
iss_location=(iss_latitude,iss_longitude)

# SUNSET TIME DATA
SEOUL_LAT = 37.566536
SEOUL_LNG = 126.977966
endpoint = "https://api.sunrise-sunset.org/json"
parameter = {"lat": SEOUL_LAT, "lng":SEOUL_LNG, "formatted": 0}
response= requests.get(url=endpoint, params=parameter)
response.raise_for_status()
data = response.json()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']
sunset_hour = int(sunset.split("T")[1].split(":")[0]) + 9
sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) + 9

# UTC -> KST TIME CONVERTER
if sunset_hour > 24:
    sunset_hour = sunset_hour - 24
elif sunrise_hour > 24:
    sunrise_hour = sunrise_hour - 24

# CURRENT TIME INFO
now = str(dt.datetime.now())
current_hour = int(now.split(" ")[1].split(":")[0])

# LOOP-IF
while True:
    time.sleep(60)      # 60초 마다 반복
    if current_hour >= sunset_hour or current_hour <= sunrise_hour: # 현재 시간이 일몰 이후이고 일출 이전일 때
        if (SEOUL_LAT - 5) <= iss_latitude <= (SEOUL_LAT + 5) and (SEOUL_LNG - 5) <= iss_longitude <= (SEOUL_LNG + 5): # Iss의 위치가 내 위도 경도의 +-5 사이일때

# SEND EMAIL
            my_email = "YOUR_GMAIL@gmail.com"
            password = "YOUR_SECRET_CODE"  # <-----Gmail 앱 비밀번호로 만든 16자리 비밀번호
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject: Look up the sky! \n\n ISS is above your head.")
