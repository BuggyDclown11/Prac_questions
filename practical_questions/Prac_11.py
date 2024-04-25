##11.	How would you verify that a specific text is displayed on a webpage using Selenium WebDriver in Python?


from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
driver.get('http://www.google.com')
search=driver.find_element(imp.By.XPATH,'//*[@id="APjFqb"]')
if search.is_displayed():
    print('displayed')
else:
    print('no logout dislayed')
imp.time.sleep(5)

