from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class ValidateURL():

    def __init__(self, url):
        self.url = url

    def validateBySelenium(self, headless):
        options = Options()
        options.headless = headless
        driver = webdriver.Chrome('Drivers/chromedriver88', chrome_options=options)
        driver.get(self.url)
        valid = False
        if driver.current_url == self.url:
            valid = True
        driver.quit()
        return valid

