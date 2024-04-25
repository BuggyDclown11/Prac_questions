##47.	How would you handle the scenario of testing a website with different accessibility requirements using Selenium WebDriver in Python?

from selenium import webdriver
from axe_selenium_python import Axe

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Load the webpage to be tested
driver.get("https://www.example.com")

# Initialize Axe
axe = Axe(driver)
axe.inject()

# Analyze accessibility issues
results = axe.run()

# Output accessibility results
if results['violations']:
    print("Accessibility violations found:")
    for violation in results['violations']:
        print(f"- {violation['id']}: {violation['help']}")
else:
    print("No accessibility violations found.")

# Close the WebDriver session
driver.quit()
