from Logger import Logger
from Spiders.LoadConfig import LoadConfig
from Spiders.ValidateURL import ValidateURL
from Spiders.SeleniumUtility import SeleniumUtility as su
class CrawlerBase:

    def __init__(self, spider_name):
        self.status = None
        self.spider_name = spider_name
        self.config = None
    def __readConfig(self):
        self.status = 'loading Config'
        Logger.log(self.status)
        configValues = LoadConfig(self.spider_name)
        return configValues.loadValues()

    # validate if url in config file is valid
    def __validateURL(self):
        self.status = 'validating URL'
        validateURL = ValidateURL(self.config['validateURL'])
        if self.config['selenium']['use_selenium']:
            return validateURL.validateBySelenium(self.config['selenium']['headless'])
        else:
            pass

    # fetch and parse data
    def __crawl(self):
        self.status = 'saving'
        Logger.log(self.status)
        crawler = su(self.config,'nio')
        print(crawler.crawl())

    # save result of __crawl
    def __saveData(self):
        self.status = 'saving'
        Logger.log(self.status)
        pass

    #activates crawler to collect info
    def getData(self):
        self.status = 'initializing'
        Logger.log(self.status)
        self.config = self.__readConfig()
        if self.__validateURL():
            self.__crawl()
            self.__saveData()
            return True
        else:
            return False





