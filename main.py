from Spiders.CrawlerBase import CrawlerBase
from Spiders.NasdaqRealTimePrice import NasdaqRealTimePrice as nasdaq

cb = nasdaq()

cb.getData()