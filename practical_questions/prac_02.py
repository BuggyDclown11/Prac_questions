##2.	Write code to search for a product on an e-commerce website using Selenium WebDriver in Python.


import time
##Necessary Import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

##chrome driver
driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website ecommerce
driver.get("https://qaopen.bishalkarki.xyz")


##send keyword for searching
search=driver.find_element(By.ID,'search_query_top').send_keys('printed dress')

ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.implicitly_wait(5)
time.sleep(5)


