from Spiders.CrawlerBase import CrawlerBase
from Logger import Logger

class NasdaqRealTimePrice(CrawlerBase):

    def __init__(self):
        self.spider_name = 'NasdaqRealTimePrice'
        Logger.log(self.spider_name)
