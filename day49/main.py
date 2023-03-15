import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/Your/Chromedriver/Path/chromedriver")
driver = webdriver.Chrome(service=service)

#London Python Developer Job Search Page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3351743229&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

#Logging in Linked in
login_button = driver.find_element(by=By.LINK_TEXT, value="로그인")
login_button.click()
time.sleep(10)
email = driver.find_element(by=By.ID, value="username")
email.send_keys("YOUR@LINKEDIN.EMAIL")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("YOUR_LINKED_IN_PASSWORD")
password.send_keys(Keys.ENTER)
time.sleep(5)

#Listing up all related Positions
list = driver.find_elements(by=By.CSS_SELECTOR, value = ".job-card-container--clickable")

#Save all the positions in the list
#Scrolling down
for job in list:
    print(f"\nSaved: {job.text}\n---")
    driver.execute_script("arguments[0].click();", job)
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-save-button"))))
