##10.	Write a script to upload a file to a website using Selenium WebDriver in Python.

from practical_questions.imports.imports import Import as imp

from setup.set_up import Set_Up

##creating setup instances
setup_driver_instance=Set_Up()
setup_driver_instance.needed_driver()

uploadfiles=setup_driver_instance.driver.find_element(imp.By.XPATH,'xpath').send_keys('location_of_the_file_in_the_devive')

##here xpath is the xpath of upload_files_btn in the form
# and in send_keys,we send location of the file to be uploaded in our device