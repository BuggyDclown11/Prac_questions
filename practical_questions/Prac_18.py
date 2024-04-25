##18.	Write a script to capture the text from all the elements of a specific class on a webpage using Selenium WebDriver in Python.

from imports.imports import Import as imp



##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

elements=driver.find_elements(imp.By.XPATH,'//input[@class="radioButton"]')

for element in elements:
    print(element.get_attribute('value'))

driver.quit()
