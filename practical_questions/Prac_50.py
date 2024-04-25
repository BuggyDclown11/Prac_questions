##50.	Write a script to automate the entire checkout process on an e-commerce website using Selenium WebDriver in Python.
import time
from practical_questions.imports.imports import Import as imp

##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website ecommerc
driver.get("https://qaopen.bishalkarki.xyz")

##variables
sum_drs_id_2='//img[contains(@src,"https://qaopen.bishalkarki.xyz/img/p/2/0/20-home_default.jpg")]'


add_cart='//*[@id="add_to_cart"]/button/span'
alert='//*[@id="center_column"]/div/p[1]'
blouse='//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[2]/a'
blouse_image='/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[1]/div/a[1]/img'
check_box='//*[@id="form"]/div/div[4]/p/label'
continue_shopping='//*[@id="center_column"]/p[2]/a[2]/i'
dresses=imp.WebDriverWait(driver,10).until(imp.EC.presence_of_element_located(('xpath','//*[@id="block_top_menu"]/ul/li[2]/a')))
drs_id=imp.WebDriverWait(driver,10).until(imp.EC.presence_of_element_located(('xpath',sum_drs_id_2)))
email='//input[@id="email"]'
password='//input[@id="passwd"]'
proceed_address='//button[@name="processAddress"]'
proceed_payment='//*[@id="center_column"]/p[2]/a[1]'
process_carrier='//button[@name="processCarrier"]'
signup_btn='//button[@id="SubmitLogin"]'
summer_dress='//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a'
women=driver.find_element('xpath','//*[@id="block_top_menu"]/ul/li[1]/a')


def hover_over(element):
    imp.ActionChains(driver).move_to_element(element).perform()

def click_ele(xpath):
    imp.WebDriverWait(driver, 10).until(
        imp.EC.element_to_be_clickable(('xpath', xpath))).click()
    time.sleep(2)

def send_credentials(xpath,cred):
    imp.WebDriverWait(driver, 10).until(
        imp.EC.element_to_be_clickable(('xpath', xpath))).send_keys(cred)


##click on women and blouse
hover_over(women)
click_ele(blouse)

##click on product image
click_ele(blouse_image)
driver.implicitly_wait(10)

##switch to frame
frame_element=driver.find_element('xpath','//iframe[@class="fancybox-iframe"]')
driver.switch_to.frame(frame_element)

##click on add to cart
click_ele(add_cart)

# driver.switch_to.default_content()

##proceed to paymanet
click_ele(proceed_payment)

# ##login user account
send_credentials(email,'shresthasijal9@gmail.com')
send_credentials(password,'12345678')
#
##click login_btn
click_ele(signup_btn)


# ##click on proceed to payment
click_ele(proceed_address)
#
# ##cick on accept terms
click_ele(check_box)
#
# ##clcik on proced button
click_ele(process_carrier)

def test_success():
    alert_text=driver.find_element('xpath',alert).text
    assert alert_text=='No payment modules have been installed.','not success'


