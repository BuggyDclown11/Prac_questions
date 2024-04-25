
from imports.imports import Import as imp



from setup.set_up import Set_Up

##creating setup instances
setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

##Navbar_login
nav_login_bar = setup_driver_instance.driver.find_element(imp.By.ID, 'login2')
nav_login_bar.click()

##Passing username and password
username_form =  imp.WebDriverWait(setup_driver_instance.driver, 10).until(imp.EC.element_to_be_clickable((imp.By.ID, 'loginusername')))
username_form.send_keys('testmorning')
password_form = setup_driver_instance.driver.find_element(imp.By.ID,'loginpassword')
password_form.send_keys('test123')
login_button=setup_driver_instance.driver.find_element(imp.By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
login_button.click()
imp.time.sleep(5)


logs=setup_driver_instance.driver.get_log('browser')
for log in logs:
     print(log)