##30.	Write a script to capture all the images present on a webpage using Selenium WebDriver in Python.

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
imgs=driver.find_elements(By.TAG_NAME,'img')

img_url= [img.get_attribute('src') for img in imgs]

for url in img_url:
    print(url)