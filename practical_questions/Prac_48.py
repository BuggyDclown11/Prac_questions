##48.	Write code to handle dynamic elements that load asynchronously on a webpage using Selenium WebDriver in Python.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

try:
    # Wait for the dynamic element to be present on the page
    dynamic_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dynamic_element_id"))
    )

    # Once the dynamic element is present, interact with it
    dynamic_element.click()  # Example: Click on the dynamic element

    # Continue with other interactions or assertions on the page

except Exception as e:
    print(f"Exception occurred while waiting for dynamic element: {e}")

finally:
    # Close the WebDriver session
    driver.quit()
