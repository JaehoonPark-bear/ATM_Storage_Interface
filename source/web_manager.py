import paramlib
import loglib
import pandas as pd

class ServerConnection(object):

    def __init__(self, url):
        self._param = paramlib.PARAMETER()
        self._log = loglib.LOG()
        self._url = url
        self.data = None

        self.balance = 0
        self.dispositHistory = ""
        self.withdrawHistory = ""
        self._log.make_log(1)

    def request(self):
        try:
            self.data = pd.read_csv(self._url) # skiprows=1, sep=',', usecols = ['BALANCE', 'DISPOSIT', 'WITHDRAW'],
                # self.balance = self.data[self._param.DATA_ORDER["BALANCE"]]
                # self.dispositHistory = self.data[self._param.DATA_ORDER["DISPOSIT"]]
                # self.withdrawHistory = self.data[self._param.DATA_ORDER["WITHDRAW"]]
            return self.data

        except Exception as e:
            self._log.make_log(10)
            return e

    def disconnect(self):
        self._url = None
        self.data = None
        self.balance = 0
        self.dispositHistory = ""
        self.withdrawHistory = ""






