import requests
import os
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple"

# Alpha Vantage 주가정보 API
alpha_vantage_api_key=os.environ.get("YOUR_ALPHA_VANTAGE_API_KEY")
alpha_vantage_url= "https://www.alphavantage.co/query"
alpha_vantage_parm= {"function":"TIME_SERIES_DAILY",
                     "symbol": STOCK,
                     "apikey": alpha_vantage_api_key}

# News API 뉴스 API
news_api_key = os.environ.get("YOUR_NEWS_API_KEY")
news_url="https://newsapi.org/v2/top-headlines"
news_param={"q": COMPANY_NAME,
            "sortBy":"popularity",
            "apiKey":news_api_key}

# TWILIO 문자메시지 API SID, 토큰
account_sid = os.environ.get("TWILIO_SID") 
auth_token = os.environ.get("TWILIO_TOKEN")


# 1. Alpha Vantage로 주가 정보 가져오기
response = requests.get(url=alpha_vantage_url, params=alpha_vantage_parm)
stock = response.json()["Time Series (Daily)"]

yesterday= [value for (key,value) in stock.items()][0]
yesterday_closing= yesterday["4. close"]

day_before_yesterday= [value for (key,value) in stock.items()][1]
day_before_yesterday_closing = day_before_yesterday["4. close"]

# 2. 주가 정보 그제 대비 어제 증감율 알아보기(+5 % /-5 % 로 설정)
price_difference = float(yesterday_closing) - float(day_before_yesterday_closing)
growth_rate = price_difference/float(yesterday_closing)
percentage = round(growth_rate * 100,2)

# 3. 주가 5% 이상 상승/하락했을 경우, News API로 기업 관련 뉴스 3개(타이틀, 간략) 가져오기
if percentage > 5 or percentage < -5:
    news_response= requests.get(news_url,news_param)
    news_for_3days = news_response.json()['articles'][:3]    
    news = [{"Headline":news_for_3days[i]["title"],"Brief":news_for_3days[i]["description"]} for i in range(3)]
    # news 리스트를 가져오는 방법이 이해가 안된다면, 다음과 같이 풀어서도 가능하다.
    # news_3days_title = [i["title"] for i in news_for_3days]
    # news_3days_description = [i["description"] for i in news_for_3days]
    # news = [{"Headline":news_3days_title[i],"Brief":news_3days_description[i]} for i in range(3)]

#4. TWILIO로 가져온 뉴스 3개 각각 문자메시지 보내기     
    client = Client(account_sid, auth_token)
    for i in range(3):
        message = client.messages \
                        .create(
                             body=f"{STOCK}: {percentage}\n "
                                  f"Headline: {news[i]['Headline']}\n "
                                  f"Brief:{news[i]['Brief']} ",
                             from_=os.environ.get("MY_TWILIO_NUMBER"),
                             to=os.environ.get("MY_NUMBER")
                         )
        print(message.sid)
