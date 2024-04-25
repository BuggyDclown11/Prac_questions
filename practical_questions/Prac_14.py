##14.	Write a script to capture a screenshot of a webpage using Selenium WebDriver in Python.


from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

setup_driver_instance.driver.save_screenshot('C:\\Users\\User\\Pictures\\ss.png')