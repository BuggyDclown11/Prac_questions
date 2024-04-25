


from imports.imports import Import as imp



##chrome driver
driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
driver.maximize_window()
##website
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
oslo=driver.find_element('id','box1')
norway=driver.find_element('xpath','//*[@id="box101"]')
imp.ActionChains(driver).drag_and_drop(oslo,norway).perform()