import web_manager
import paramlib
import loglib
import time
import threading

def updater(readerHandler):
    while True:
        data = input().split(',') # Data Type = [isDetect(boolean),PINCheck(boolean),URL,TYPE(int)]
                                  # if PIN Reader detect > isDetect = True
                                  # if PIN Check is Correct > PINCheck = True
                                  # TYPE > 0: IDLE, 1: request data , 2: EXIT
        if len(data) == 4:
            if data[0] == "True":
                readerHandler._isDetect = True
            else:
                readerHandler._isDetect = False

            if data[1] == "True":
                readerHandler._PINCheck = True
            else:
                readerHandler._PINCheck = False

            readerHandler._url = data[2]
            readerHandler._step = int(data[3])

        else:
            pass

        time.sleep(0.5)


class PIN_Reader(object):

    def __init__(self):
        self._isDetect = False
        self._url = None
        self._step = 0
        self._PINCheck = False
        self._param = paramlib.PARAMETER()
        self._log = loglib.LOG()
        self._log.make_log(4)

        self.tempInputThread = threading.Thread(target=updater, args=(self,))
        self.tempInputThread.start()

        try:
            while True:
                if self._isDetect:
                    if self._PINCheck:
                        if self._url != None:
                            self.webManager = web_manager.ServerConnection(self._url)
                            while True:
                                if self._step == self._param.SIGNAL["REQUEST"]:
                                    self._log.make_log(2)
                                    data = self.webManager.request()
                                    print(data)
                                elif self._step == self._param.SIGNAL["EXIT"]:
                                    self._log.make_log(3)
                                    self._step = self._param.SIGNAL["NONE"]
                                    self.webManager.disconnect()
                                    break
                                else:
                                    pass

                                self.initialize_data()

                time.sleep(0.5)

        except Exception:
            self._log.make_log(98)
            print("make specific H/W signal(like I/O)")
            time.sleep(0.5)

    def initialize_data(self):
        self._isDetect = False
        self._url = None
        self._PINCheck = False
        self._step = self._param.SIGNAL["NONE"]