##42.	How Write code to perform assertions on the attributes of an element using Selenium WebDriver in Python.
from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

##creating setup instances
setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

nav_login_bar = setup_driver_instance.driver.find_element(imp.By.ID, 'login2')
nav_login_bar.click()

##Passing username and password
username_form =  imp.WebDriverWait(setup_driver_instance.driver, 10).until(imp.EC.element_to_be_clickable((imp.By.ID, 'loginusername')))
attribute=username_form.get_attribute('type')
assert attribute=='text','attribute doesnt exist or match'