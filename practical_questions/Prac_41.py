##41.	Write a script to interact with JavaScript alerts, prompts, and confirmations using Selenium WebDriver in Python

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Alerts.html')

##Simple alert
simple_alert=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simple_alert.click()
click_btn=driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')
click_btn.click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)

##Prompt alert
prompt_alert=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
prompt_alert.click()
click_btn=driver.find_element(By.XPATH,'//*[@id="Textbox"]/button')
click_btn.click()
time.sleep(5)
Alert=driver.switch_to.alert
Alert.send_keys('Sijal')
time.sleep(5)
Alert.accept()
time.sleep(5)

##confirmation_alert
confirmation_alert=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confirmation_alert.click()
click_btn=driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
click_btn.click()
time.sleep(5)
driver.switch_to.alert.dismiss()
time.sleep(5)