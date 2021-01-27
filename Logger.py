import logging
from datetime import datetime

class Logger:

    @staticmethod
    def log(msg):
       print(str(datetime.now()) + '-' + msg)