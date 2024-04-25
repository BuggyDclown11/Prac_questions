##49.	How do you handle the scenario of testing a website with different security configurations using Selenium WebDriver in Python?

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Chrome in this example)
driver = webdriver.Chrome()

try:
    # Navigate to the webpage with HTTP protocol
    driver.get("http://example.com")

    # Verify that the website redirects to HTTPS (if applicable)
    assert "https://example.com" in driver.current_url

    # Handle authentication (if applicable)
    # Example: Log in to the website with credentials
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    login_button = driver.find_element_by_id("login_button")

    username_input.send_keys("your_username")
    password_input.send_keys("your_password")
    login_button.click()

    # Wait for the login to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout_button"))
    )

    # Test for security headers
    security_headers = driver.execute_script("return document.head.innerHTML")
    assert "Content-Security-Policy" in security_headers
    assert "X-Content-Type-Options" in security_headers
    assert "X-Frame-Options" in security_headers
    assert "X-XSS-Protection" in security_headers

    # Test for mixed content
    mixed_content_elements = driver.find_elements_by_xpath("//img[@src='http://example.com/image.jpg']")
    assert len(mixed_content_elements) == 0

    # Test for vulnerabilities (e.g., XSS)
    # Example: Input a XSS payload into a form field
    input_field = driver.find_element_by_id("input_field")
    input_field.send_keys("<script>alert('XSS')</script>")

    # Submit the form
    submit_button = driver.find_element_by_id("submit_button")
    submit_button.click()

    # Wait for the alert to appear
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "XSS" in alert.text
    alert.accept()

    print("Security tests passed!")

except Exception as e:
    print(f"Security tests failed: {e}")

finally:
    # Close the WebDriver session
    driver.quit()
