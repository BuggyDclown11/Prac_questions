##39.	How would you handle the scenario of testing a website with different browser configurations using Selenium WebDriver in Python?

import pytest
from selenium import webdriver

# Fixture to initialize WebDriver for Chrome
@pytest.fixture(scope="class")
def chrome_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

# Fixture to initialize WebDriver for Firefox
@pytest.fixture(scope="class")
def firefox_driver(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.quit()

# Test class to execute test scenarios against different browser configurations
@pytest.mark.usefixtures("chrome_driver")
class TestChromeBrowser:
    def test_example_scenario(self):
        # Test scenario using Chrome WebDriver
        pass

@pytest.mark.usefixtures("firefox_driver")
class TestFirefoxBrowser:
    def test_example_scenario(self):
        # Test scenario using Firefox WebDriver
        pass
