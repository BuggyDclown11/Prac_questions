import pytest
from selenium import webdriver
import time

@pytest.fixture(params=[(1920, 1080), (1366, 768), (1280, 800)])
def resolution(request):
    return request.param

@pytest.fixture(scope="function")
def driver(resolution):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--window-size={resolution[0]},{resolution[1]}")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_with_resolution(driver, resolution):
    driver.get("https://www.google.com")
    time.sleep(2)

    # Check the visibility of the search image
    assert driver.find_element('xpath','/html/body/div[1]/div[2]/div/img').is_displayed()

    # Assert the title of the webpage
    assert "Google" in driver.title
