##8.	Write code to capture all the links present on a webpage using Selenium WebDriver in Python.

import time
##Necessary Import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get("http://demoblaze.com")


## fetches all links
all_url=driver.find_elements(By.TAG_NAME,'a')
urls=[]


for i in all_url:
    urls.append(i.get_attribute('href'))
    print(urls)
print(len(urls))