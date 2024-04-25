##12.	Write code to scroll down to the bottom of a webpage using Selenium WebDriver in Python.

import time

from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

##scrolling by pixels
# setup_driver_instance.driver.execute_script('window.scrollBy(0,1000)')

##scrolling till finding  specific element
element=setup_driver_instance.driver.find_element(imp.By.XPATH,'//*[@id="fotcont"]/div[3]/div/div/h4')
setup_driver_instance.driver.execute_script('arguments[0].scrollIntoView();',element)
time.sleep(5)

##Scrolling to end of the page
setup_driver_instance.driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')