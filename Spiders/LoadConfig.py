import yaml
from os import path
from Logger import Logger
class LoadConfig():

    def __init__(self, spider_name):
        self.spider_name = spider_name

    def __fileExist(self):
        return path.exists(self.__configPath())

    def __configPath(self):
        return 'Config/' + self.spider_name + '.yml'

    def loadValues(self):
        Logger.log(self.__configPath())
        Logger.log(str(self.__fileExist()))
        if self.__fileExist():
            with open(self.__configPath()) as f:
                return yaml.load(f, Loader=yaml.FullLoader)
