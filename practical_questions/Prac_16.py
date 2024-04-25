##16.	Write code to perform mouse hover actions on an element using Selenium WebDriver in Python.
import time

from practical_questions.imports.imports import Import as imp
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website ecommerce
driver.get("https://qaopen.bishalkarki.xyz")

category_women=driver.find_element(imp.By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/a')
casual_drs=driver.find_element(imp.By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/ul/li[1]/a')

##hovers to women_category and moves to dresses and then click
imp.ActionChains(driver).move_to_element(category_women).move_to_element(casual_drs).click().perform()
time.sleep(5)