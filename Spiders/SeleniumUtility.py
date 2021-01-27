from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class SeleniumUtility:

    def __init__(self, config, keyword):
        self.config = config
        self.keyword = keyword

    def __targetURL(self):
        return self.config['templateURL']%(self.keyword)

    def crawl(self):
        options = Options()
        options.headless = self.config['selenium']['headless']
        driver = webdriver.Chrome('Drivers/chromedriver88', chrome_options=options)
        driver.get(self.__targetURL())
        return self.__parse(driver)

    def __parse(self, driver):
        result = {}
        for key in self.config['xpath']:
            data = driver.find_element_by_xpath(self.config['xpath'][key]).text
            result[key] = data
        driver.quit()
        return result
