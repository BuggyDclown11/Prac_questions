import time

from imports.imports import Import as imp
from selenium.common.exceptions import TimeoutException


##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element('id','hide-textbox').click()
time.sleep(5)
element=driver.find_element('id','displayed-text')
if element.is_displayed():
    print("Found at the start")
else:
    print('element not found')
    driver.find_element('id', 'show-textbox').click()
    if element.is_displayed():
        print("Found after clicking show button")


# try:
#     imp.WebDriverWait(driver,10).until(imp.EC.visibility_of_element_located(('id','displayed-text'))).send_keys('sjal')
#     time.sleep(2)
#     print('Found')
#
# except TimeoutException:
#     print('element not found')