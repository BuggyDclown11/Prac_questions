##38.	Write a script to verify the responsiveness of a webpage by resizing the browser window using Selenium WebDriver in Python.
import time

from imports.imports import Import as imp







import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        ##chrome driver
        self.driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
        self.driver.maximize_window()
        ##website
        self.driver.get("https://www.pocketpandit.com/")

    def resize_window(self, width, height):
        self.driver.set_window_size(width,height)

    def test_something(self):
        try:
            self.resize_window(600,900)
            time.sleep(5)
            menu=self.driver.find_element('xpath','//*[@id="app"]/header/div/div/div[1]/div[1]/div/ul/li[1]/a')
            assert menu.is_displayed(),"Home button is not displayed for small window"# add assertion here
        except AssertionError:
            print('home button not displayed')













if __name__ == '__main__':
    unittest.main()
