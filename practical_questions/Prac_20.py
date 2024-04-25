##20.	Write code to switch between different windows or tabs opened by the browser using Selenium WebDriver in Python.


from imports.imports import Import as imp



##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.window_handles)
print('**************')
driver.find_element('id','opentab').click()
print(driver.window_handles)
print('**************')
driver.find_element('id','openwindow').click()
print(driver.window_handles)
print('**************')
driver.switch_to.window(driver.window_handles[1])
driver.find_element('xpath','//a[contains(@href,"/blog")]').click() 

