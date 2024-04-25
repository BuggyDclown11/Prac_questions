##32.	Write code to simulate browser navigation actions such as back, forward, and refresh using Selenium WebDriver in Python.
import time

from imports.imports import Import as imp



##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://www.google.com")
driver.find_element(imp.By.XPATH,'//*[@id="APjFqb"]').send_keys('hello world')
imp.ActionChains(driver).send_keys(imp.Keys.ENTER).perform()
driver.implicitly_wait(10)
# driver.navigate().to("https://www.facebook.com")
# time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.forward()
time.sleep(2)
