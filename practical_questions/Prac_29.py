##29.	How do you handle SSL certificate errors that may occur while accessing a webpage using Selenium WebDriver in Python?
from selenium.webdriver import DesiredCapabilities

from imports.imports import Import as imp



##chrome

##using options
# options=imp.Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')
#driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'),options=options)

##using desired_capabilities
desired_capabilities=DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts']=True

driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'),desired_capabilities=desired_capabilities)
driver.maximize_window()




##website
driver.get("https://expired.badssl.com")
driver.implicitly_wait(10)
print(driver.find_element('xpath','//*[@id="content"]/h1').text)
