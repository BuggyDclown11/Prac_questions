##31.	How would you handle the scenario of testing a website with different user roles using Selenium WebDriver in Python?

from selenium import webdriver


def login(username, password):
    # Navigate to the login page
    driver.get('https://example.com/login')

    # Find username and password fields, and submit button
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('password')
    submit_button = driver.find_element_by_id('login-button')

    # Enter username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the submit button
    submit_button.click()


# Test cases for different user roles
def test_admin_functionality():
    login('admin@example.com', 'adminpassword')
    # Perform admin-specific actions


def test_regular_user_functionality():
    login('user@example.com', 'userpassword')
    # Perform actions relevant to regular users


def test_premium_user_functionality():
    login('premium@example.com', 'premiumpassword')
    # Perform actions relevant to premium users


def test_guest_functionality():
    # Perform actions available to guests (not logged in)
    pass


# Initialize the WebDriver
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Execute test cases
test_admin_functionality()
test_regular_user_functionality()
test_premium_user_functionality()
test_guest_functionality()

# Close the WebDriver
driver.quit()
