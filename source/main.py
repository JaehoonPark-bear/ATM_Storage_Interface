import broker
import paramlib
import loglib
import time
import os
import sys

def main():

    broker.PIN_Reader()
    param = paramlib.PARAMETER()
    log = loglib.LOG()

    pingCnt = 0

    while True:
        pingchecker = os.system(param.PING_CMD)

        if pingchecker:
            pingCnt = 0
        else:
            pingCnt += 1
            if pingCnt == param.EXCEPTION_COUNT:
                log.make_log(99)
                print("make specific H/W signal(like I/O)")
                time.sleep(0.5)
                sys.exit(0)

        time.sleep(0.5)

if __name__ == "__main__":
    main()