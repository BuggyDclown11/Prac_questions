# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Function to launch the browser based on the input parameter
def launch_browser(browser):
    # Check if the browser parameter is 'chrome'
    if browser.lower() == "chrome":
        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        # Add any desired options here (if needed)
        # Create and return an instance of Chrome WebDriver
        return webdriver.Chrome(options=chrome_options)
    # Check if the browser parameter is 'firefox'
    elif browser.lower() == "firefox":
        # Configure Firefox options
        firefox_options = webdriver.FirefoxOptions()
        # Add any desired options here (if needed)
        # Create and return an instance of Firefox WebDriver
        return webdriver.Firefox(options=firefox_options)
    # If an unsupported browser is specified, raise an error
    else:
        raise ValueError("Unsupported browser specified")


# Main function to execute the test case
def main(browser):
    # Launch the specified browser
    driver = launch_browser(browser)
    try:
        # Example test case: Open a website
        driver.get("https://example.com")
        # Write test steps here to interact with the website

        # Example: Find an element by its ID and perform an action
        # element = driver.find_element_by_id("element_id")
        # element.click()

    finally:
        # Close the browser window after the test execution
        driver.quit()


# Entry point of the script
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    import sys

    if len(sys.argv) != 2:
        # Print usage information and exit if the number of arguments is incorrect
        print("Usage: python script.py <browser>")
        sys.exit(1)
    # Call the main function with the browser specified as the command-line argument
    main(sys.argv[1])
