from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("/Your/Chorme_driver/path/chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options, service=service)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(10)
        x = self.driver.find_element(By.XPATH,'//*[@id="onetrust-close-btn-container"]/button')
        x.click()
        time.sleep(2)
        button = self.driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"download speed: {self.down}")
        print(f"upload speed: {self.up}")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        time.sleep(10)

        login = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
        login.click()
        time.sleep(5)

        email = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(YOUR_TWITTER_ID)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        
        #이메일로 로그인하려는지, 트위터 아이디로 로그인 하려는지, 전화번호로 로그인 하려는지에 따라 아래 XPATH가 바뀌는 이상한 현상도 겪었다.
        password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        password.send_keys(YOUR_TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        #알림 설정 창이 뜰 수도 있다. 한번 끄면 다음 번에 실행할 때는 안 뜸
        #skip_button = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/span/span')
        #skip_button.click()

        twit_input = self.driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block')
        twit_input.send_keys(f"My internet speed is download: {self.down} / upload: {self.up}.")
        twit_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        twit_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
