##5.	How do you handle dynamic elements that have changing IDs or classes using Selenium WebDriver in Python?


from practical_questions.imports.imports import Import as imp


driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website facebook
driver.get("https://www.facebook.com")


##Using contains
using_contains=driver.find_element(imp.By.XPATH,'//*[contains(@id,"u_0_5")]').click()


imp.time.sleep(2)