##9.	How do you handle browser cookies using Selenium WebDriver in Python?


import time
##Necessary Import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()

##for accepting all cookies
driver.get("https://www.opera.com/download")
cookies=driver.find_element(By.XPATH,'//span[contains(text()."Accept cookies")]').click()
time.sleep(5)
driver.quit()

##getting cookies
driver.get('http://www.google.com')
cookie=driver.get_cookie()
print(cookie)

##adding cookie
cookie={'name':'cookiename','value':'cookievalue'}
driver.add_cookie(cookie)

##deletiig cookie
driver.delete_cookie('cookiename')

