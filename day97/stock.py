import requests
import os

class Stock():
    def __init__(self):
        self.STOCK = "AAPL"
        self.COMPANY_NAME = "Apple"

        # Alpha Vantage 주가정보 API
        self.alpha_vantage_api_key=os.environ.get("ALPHA_VANTAGE_API_KEY")
        self.alpha_vantage_url= "https://www.alphavantage.co/query"
        self.alpha_vantage_parm= {"function":"TIME_SERIES_DAILY_ADJUSTED",
                             "symbol": self.STOCK,
                             "apikey": self.alpha_vantage_api_key}
    
    def get_price(self):
        # 1. Alpha Vantage로 주가 정보 가져오기
        self.response = requests.get(url=self.alpha_vantage_url, params=self.alpha_vantage_parm)
        self.stock = self.response.json()["Time Series (Daily)"]

        self.yesterday= [value for (key,value) in self.stock.items()][0]
        self.yesterday_closing= self.yesterday["4. close"]

        self.day_before_yesterday= [value for (key,value) in self.stock.items()][1]
        self.day_before_yesterday_closing = self.day_before_yesterday["4. close"]

        # 2. 주가 정보 그제 대비 어제 증감율 알아보기(+5 % /-5 % 로 설정)
        self.price_difference = float(self.yesterday_closing) - float(self.day_before_yesterday_closing)
        self.growth_rate = self.price_difference/float(self.yesterday_closing)
        self.percentage = round(self.growth_rate * 100,2)

        self.message = f"{self.COMPANY_NAME}'s Yesterday Closing price: ${self.yesterday_closing}\n\n" \
                       f"{self.COMPANY_NAME}'s Day Before Yesterday Closing price: ${self.day_before_yesterday_closing}\n\n" \
                       f"Growth rate: {self.percentage}%"
        return self.message