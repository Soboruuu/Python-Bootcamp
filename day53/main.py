from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

FORM = 'https://forms.gle/pkkDJ4MEhHr9RgCR9'

service= Service("Your/Chrome_driver/Path/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

    def sheet(self):
        self.driver = webdriver.Chrome(service=service_win, options=options)
        for i in range(len(self.all_addresses)):
            self.driver.get(FORM)
            time.sleep(5)
            self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.all_addresses[i])
            self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.all_prices[i])
            self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(self.all_links[i])
            self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
            time.sleep(random.randint(1,5))

prop = Property()
prop.get_prop_info()
prop.sheet()
