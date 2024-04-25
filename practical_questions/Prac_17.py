import time

##17.	How do you handle iframes embedded within a webpage using Selenium WebDriver in Python?


from practical_questions.imports.imports import Import as imp
from selenium.webdriver.chrome.options import Options

##use options so that browser doesnt close itself after the execution of code
options=Options()
options.add_experimental_option('detach',True)


##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'),options=options)
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


frame_element=driver.find_element('xpath','//iframe[@id="courses-iframe"]')
##first we need to switch to frame before clicking element inside the frame
driver.switch_to.frame(frame_element)
time.sleep(3)

driver.find_element('xpath','//a[@href="consulting"]').click()


##Use default_content() to switch to main html tag body
driver.switch_to.default_content()
driver.find_element('id','name').send_keys('sijal')



