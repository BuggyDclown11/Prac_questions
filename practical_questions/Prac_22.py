##22.	Write a script to extract data from a table on a webpage using Selenium WebDriver in Python


from imports.imports import Import as imp



##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

table=driver.find_element('xpath','//*[@id="product"]/tbody')
table_row=table.find_elements('xpath','//tr')

data=[]

for tr in table_row:
    row=[item.text for item in tr.find_elements('xpath','.//td')]
    data.append(row)
    print(data)
