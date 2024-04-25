
##40.	How do you handle the scenario of testing a website with different operating systems using Selenium WebDriver in Python?

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to initialize WebDriver for a specific operating system
def initialize_driver_for_os(os_name):
    if os_name.lower() == "windows":
        return webdriver.Chrome()  # Use appropriate WebDriver for Windows
    elif os_name.lower() == "macos":
        return webdriver.Chrome()  # Use appropriate WebDriver for macOS
    elif os_name.lower() == "linux":
        return webdriver.Chrome()  # Use appropriate WebDriver for Linux
    else:
        raise ValueError("Unsupported operating system: " + os_name)

# Example test scenario to demonstrate testing against different operating systems
def test_different_os():
    # Test scenario on Windows
    driver = initialize_driver_for_os("Windows")
    try:
        driver.get("https://www.example.com")
        # Perform actions specific to Windows
        time.sleep(2)
    finally:
        driver.quit()

    # Test scenario on macOS
    driver = initialize_driver_for_os("macOS")
    try:
        driver.get("https://www.example.com")
        # Perform actions specific to macOS
        time.sleep(2)
    finally:
        driver.quit()

    # Test scenario on Linux
    driver = initialize_driver_for_os("Linux")
    try:
        driver.get("https://www.example.com")
        # Perform actions specific to Linux
        time.sleep(2)
    finally:
        driver.quit()

# Execute the test scenario
test_different_os()
