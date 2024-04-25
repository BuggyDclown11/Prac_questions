##3.	How do you verify that a certain element is present on a webpage using Selenium WebDriver in Python?


from practical_questions.imports.imports import Import as imp

##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website ecommerce
driver.get("https://qaopen.bishalkarki.xyz")

try:
        ##send keyword for searching

    select =imp.WebDriverWait(driver, 10).until(imp.EC.presence_of_element_located((imp.By.ID, 'search_query_top')))
    print('presence of element located')
except imp.TimeoutException:
    print('absence of element')
imp.time.sleep(5)


