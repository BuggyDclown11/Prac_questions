##45.	How do you handle the scenario of testing a website with different browser versions using Selenium WebDriver in Python?

from selenium import webdriver

# Initialize WebDriver for Chrome browser (specific version)
chrome_driver_path = "path/to/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--ignore-certificate-errors")

chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Initialize WebDriver for Firefox browser (specific version)
firefox_driver_path = "path/to/geckodriver.exe"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_options.set_preference("dom.disable_beforeunload", True)
firefox_options.set_preference("browser.tabs.remote.autostart", False)

firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# Execute test scenarios with Chrome browser
# Example: chrome_driver.get("https://www.example.com")
# Example: Perform test assertions

# Execute test scenarios with Firefox browser
# Example: firefox_driver.get("https://www.example.com")
# Example: Perform test assertions

# Close WebDriver instances
chrome_driver.quit()
firefox_driver.quit()
