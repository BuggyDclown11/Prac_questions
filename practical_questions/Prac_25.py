## 25.	How do you handle the scenario of testing a website on different devices/resolutions using Selenium WebDriver in Python?

from practical_questions.imports.imports import Import as imp

chrome_options=imp.webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--start-maximized')

driver = imp.webdriver.Chrome(options=chrome_options,service=imp.Service('../driver/chromedriver.exe'))
driver.get("http://demoblaze.com")

nav_login_bar = driver.find_element(imp.By.ID, 'login2')
nav_login_bar.click()

##Passing username and password
username_form =  imp.WebDriverWait(driver, 10).until(imp.EC.element_to_be_clickable((imp.By.ID, 'loginusername')))
username_form.send_keys('testmorning')
password_form = driver.find_element(imp.By.ID,'loginpassword')
password_form.send_keys('test123')
login_button=driver.find_element(imp.By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()
imp.time.sleep(5)

