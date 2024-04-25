
##44.	Write code to simulate user interactions such as scrolling, zooming, and mouse movements using Selenium WebDriver in Python.


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Scroll down the webpage
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Create an instance of ActionChains
actions = ActionChains(driver)

# Perform various user interactions
# Scroll to a specific element
element = driver.find_element_by_css_selector("#some_element")
actions.move_to_element(element).perform()

# Mouse hover over an element
hover_element = driver.find_element_by_css_selector("#hover_element")
actions.move_to_element(hover_element).perform()

# Click an element
click_element = driver.find_element_by_css_selector("#click_element")
actions.click(click_element).perform()

# Double click an element
double_click_element = driver.find_element_by_css_selector("#double_click_element")
actions.double_click(double_click_element).perform()

# Right click an element
right_click_element = driver.find_element_by_css_selector("#right_click_element")
actions.context_click(right_click_element).perform()

# Drag and drop an element
source_element = driver.find_element_by_css_selector("#source_element")
target_element = driver.find_element_by_css_selector("#target_element")
actions.drag_and_drop(source_element, target_element).perform()

# Zoom in/out
# Note: Zooming may not be supported in all browsers
# You may need to change browser settings or use third-party libraries/extensions
driver.execute_script("document.body.style.zoom='80%'")  # Zoom in to 80%
driver.execute_script("document.body.style.zoom='120%'")  # Zoom out to 120%

# Close the WebDriver session
driver.quit()
