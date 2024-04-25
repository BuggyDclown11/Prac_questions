from practical_questions.imports.imports import Import as imp
class Set_Up:

    def needed_driver(self):
        self.driver = imp.webdriver.Chrome(service=imp.Service('../driver/chromedriver.exe'))
        self.driver.maximize_window()
        ##website
        self.driver.get("http://demoblaze.com")
