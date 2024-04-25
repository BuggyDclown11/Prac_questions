## 24.	Write code to verify the presence of a specific attribute in an element using Selenium WebDriver in Python.


from imports.imports import Import as imp

##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
attribute = imp.WebDriverWait(driver, 10).until(imp.EC.presence_of_element_located(('id', 'name')))

try:
    placeholder_attribute = attribute.get_attribute('placholder')
    if placeholder_attribute is not None:
        print(f"Placeholder attribute found: {placeholder_attribute}")
    else:
        print("Placeholder attribute not found")
except AttributeError:
    print("Placeholder attributvdfjnvfdvofde not found")
