##46.	Write a script to verify the correctness of form submissions on a webpage using Selenium WebDriver in Python.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver (Chrome in this example)
driver = webdriver.Chrome()

try:
    # Navigate to the form page
    driver.get("https://example.com/form")

    # Fill the form fields
    driver.find_element_by_id("name").send_keys("John Doe")
    driver.find_element_by_id("email").send_keys("john.doe@example.com")
    driver.find_element_by_id("message").send_keys("This is a test message")

    # Submit the form
    driver.find_element_by_id("submit_button").click()

    # Validate the submission (for example, by checking for success message)
    success_message = driver.find_element_by_class_name("success-message").text
    assert "Form submitted successfully" in success_message

    print("Form submission test passed!")

except Exception as e:
    print(f"Form submission test failed: {e}")

finally:
    # Close the WebDriver session
    driver.quit()
