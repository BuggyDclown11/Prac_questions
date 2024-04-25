##7.	How do you handle dropdown menus with a large number of options using Selenium WebDriver in Python?

from selenium.webdriver.support.select import Select

from practical_questions.imports.imports import Import as imp

##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


## select from dropdown
select_options=driver.find_element(imp.By.ID,'dropdown-class-example')
select=Select(select_options)

##select from index 2
select.select_by_index(2)
imp.time.sleep(2)
select.select_by_value('option1')
imp.time.sleep(2)
