##6.	Write a script to select multiple checkboxes on a webpage using Selenium WebDriver in Python.

from practical_questions.imports.imports import Import as imp

##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(imp.By.XPATH,'//input[starts-with(@name,"checkBoxOption")]')
print(checkboxes)

##select only 2 top checkboxes
for check_box in checkboxes:
    if checkboxes.index(check_box)+1<3:
        check_box.click()

imp.time.sleep(5)