##15.	How would you handle alerts that appear after certain actions on a webpage using Selenium WebDriver in Python?


from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

##dismissies alert by clicking ok
setup_driver_instance.driver.switch_to.alert.accept()

##dimissies alert by clicking cancel
setup_driver_instance.driver.switch_to.alert.dismiss()