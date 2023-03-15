from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

service = Service("/your/chrome_driver/path/chromedriver")
options = webdriver.ChromeOptions()

# ⬇︎테스트를 진행하는 동안 브라우저가 자꾸 꺼져서 브라우저를 유지하도록 했다.
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)
# ⬆︎

URL = "https://tinder.com/"
EMAIL = "YOUR_FACEBOOK@EMAIL.COM"
PASSWORD = "YOUR_FACEBOOK_PASSWORD"

driver.get(URL)
driver.maximize_window()
time.sleep(10)

def login():
    log_in_btn = driver.find_element(by=By.XPATH, value='//*[@id="s-662773879"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    log_in_btn.click()
    time.sleep(5)
    facebook_btn = driver.find_element(by=By.XPATH, value='//*[@id="s1903812341"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
    facebook_btn.click()
    time.sleep(5)

    base_window = driver.window_handles[0]
    facebook_login_window = driver.window_handles[1]

    driver.switch_to.window(facebook_login_window)
    print(driver.title)

    email_input = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
    email_input.send_keys(EMAIL)
    password_input = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)
    driver.switch_to.window(base_window)
    print(driver.title)

def pop_up_allow():
    location_allow_btn = driver.find_element(by=By.XPATH, value='//*[@id="s1903812341"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
    location_allow_btn.click()
    time.sleep(2)

    notification_btn = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
    notification_btn.click()
    time.sleep(10)

    darkmode_btn = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div/div[2]/button')
    darkmode_btn.click()
    time.sleep(5)

    privacy_allow_btn = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
    privacy_allow_btn.click()
    time.sleep(5)

def like_btn():
    like_btn = driver.find_element(By.XPATH, '//*[@id="s-662773879"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    like_btn.click()

def like_btn_2():
    like_btn_2 = driver.find_element(By.XPATH, '//*[@id="s-662773879"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
    like_btn_2.click()

login()
time.sleep(5)
base_window = driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
pop_up_allow()
time.sleep(15)
like_btn()
like += 1
print(like)
while like < 100:
    try:
        like_btn_2()
        like += 1
        print(like)
        time.sleep(3)
    except ElementClickInterceptedException:
        append_home = driver.find_element(by=By.XPATH, value='//*[@id="s1903812341"]/main/div/div[2]/button[2]')
        append_home.click()
        time.sleep(2)
