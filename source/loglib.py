import logging
from logging.handlers import RotatingFileHandler
import paramlib

class LOG(object):

    def __init__(self):
        self._param = paramlib.PARAMETER()
        self.logger = logging.getLogger()
        self.logger.setLevel(self._param.LOG["INFORM_LEVEL"])
        self.logFormat = logging.Formatter(fmt=self._param.LOG["FORMAT"])

        self.handler = RotatingFileHandler(filename=self._param.LOG["PATH"] + self._param.LOG["FILE_NAME"],
                                           maxBytes=self._param.LOG["FILE_MAX_SIZE"],
                                           backupCount=self._param.LOG["FILE_MAX_NUMBER"])
        self.handler.setFormatter(self.logFormat)
        self.logger.addHandler(self.handler)


        self.LIST = {
            1: (self._param.LOG["LEVEL"]["INFO"], "Connect to server"),
            2: (self._param.LOG["LEVEL"]["INFO"], "Received Request"),
            3: (self._param.LOG["LEVEL"]["INFO"], "Received Exit"),
            4: (self._param.LOG["LEVEL"]["INFO"], "Start PIN Reader Process"),
            10: (self._param.LOG["LEVEL"]["ERROR"], "Invalid URL!"),
            98: (self._param.LOG["LEVEL"]["CRITICAL"], "PIN Reader Error!"),
            99: (self._param.LOG["LEVEL"]["CRITICAL"], "Internet disconnected!")
        }

    def make_log(self, errorCode):
        logLevel, message = self.LIST[errorCode]

        if logLevel == self._param.LOG["LEVEL"]["INFO"]:
            self.logger.info(message)
        elif logLevel == self._param.LOG["LEVEL"]["WARNING"]:
            self.logger.warning(message)
        elif logLevel == self._param.LOG["LEVEL"]["ERROR"]:
            self.logger.error(message)
        elif logLevel == self._param.LOG["LEVEL"]["CRITICAL"]:
            self.logger.critical(message)