from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

service= Service("Your\Chorme-driver\Path\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

SIMILAR_ACCOUNT = "Specific Instagram ID"
USERNAME = "Your Instagram ID"
PASSWORD = "Your Instagram Password"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service_win, options=options)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(10)
        id = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        id.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers')
        time.sleep(10)
        followers = self.driver.find_element(By.CSS_SELECTOR,'._ab8w ._aano')
        scroll = 0
        while scroll < 5:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers)
            scroll += 1
            time.sleep(10)

    def follow(self):
        self.follower_list = self.driver.find_elements(by="css selector", value="div._aano div div div button")
        print(len(self.follower_list))
        for follower in self.follower_list:
            # try:
            if follower.text == "팔로우":
                follower.click()
                time.sleep(random.randint(1,5))
