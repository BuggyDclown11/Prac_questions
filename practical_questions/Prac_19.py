##19.	How would you simulate keyboard actions such as pressing Enter or Tab using Selenium WebDriver in Python?
import time

from practical_questions.imports.imports import Import as imp
from setup.set_up import Set_Up

##creating setup instances
setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

##Navbar_login
nav_login_bar = setup_driver_instance.driver.find_element(imp.By.ID, 'login2')
nav_login_bar.click()

username_form =  imp.WebDriverWait(setup_driver_instance.driver, 10).until(imp.EC.element_to_be_clickable((imp.By.ID, 'loginusername')))
username_form.send_keys('testmorning')
imp.ActionChains(setup_driver_instance.driver).send_keys(imp.Keys.TAB).perform()

password_form = setup_driver_instance.driver.find_element(imp.By.ID,'loginpassword')
password_form.send_keys('test123')
imp.ActionChains(setup_driver_instance.driver).send_keys(imp.Keys.TAB).perform()
imp.ActionChains(setup_driver_instance.driver).send_keys(imp.Keys.TAB).perform()

##clicks on login button
imp.ActionChains(setup_driver_instance.driver).send_keys(imp.Keys.ENTER).perform()
time.sleep(5)