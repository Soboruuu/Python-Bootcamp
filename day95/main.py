import requests
import os
import datetime
import smtplib

my_email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

service_key = os.environ.get('SERVICE_KEY')

today = datetime.date.today().strftime('%Y%m%d')
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : service_key, 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : today, 'base_time' : '0600', 'nx' : '61', 'ny' : '128' }

response = requests.get(url, params=params)
print(response.url)
data = response.json()
rain_chance = data['response']['body']['items']['item'][0]['obsrValue']
precipitation_hour = data['response']['body']['items']['item'][2]['obsrValue']

if rain_chance == '0':
    rain_chance = 'no Rain'
else:
    rain_chance = 'Rain'
    message = f'There will be {rain_chance} today.\n{precipitation_hour}% chance of rain.'
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Today's rain forecast\n\n{message}")
    connection.close()
    print(message)
