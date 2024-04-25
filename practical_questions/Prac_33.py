##33.	How do you handle the scenario of testing a website with different data sets using Selenium WebDriver in Python?

import unittest
from imports.imports import Import as imp

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
        self.driver.maximize_window()
        self.driver.get("https://qaopen.bishalkarki.xyz/index.php")
    def perform_search_query(self,search_query):
        self.driver.find_element('id', 'search_query_top').send_keys(search_query)
        imp.ActionChains(self.driver).send_keys(imp.Keys.ENTER).perform()
        self.driver.find_element('id', 'search_query_top').clear()
        imp.time.sleep(2)
        query_results = self.driver.find_elements('xpath', '//*[@id="product_list"]/li/div/div/div[1]/div')
        self.assertTrue(len(query_results) > 0,f"No result found for query: {search_query}")
        print(f'total results found for {search_query} is : {len(query_results)}')

    def test_something(self):
        queries = ['tshirt', 'blouse', 'printed']
        for query in queries:
            try:
                self.perform_search_query(query)
            except AssertionError as e:
                print(f"Assertion failed: {e}")
                continue


if __name__ == '__main__':
    unittest.main()
