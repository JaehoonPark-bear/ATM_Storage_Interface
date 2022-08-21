
class PARAMETER(object):

    VERSION = "0.0.1.0"

    SIGNAL = {
        "NONE"        : 0,
        "REQUEST"     : 1,
        "EXIT"        : 2
    }

    DATA_ORDER = {
        "BALANCE"   : 0,
        "DISPOSIT"  : 1,
        "WITHDRAW"  : 2
    }

    LOG = {
        "PATH"              : "../log/",
        "FORMAT"            : "[%(asctime)s] [%(levelname)s] : %(message)s",
        "INFORM_LEVEL"      : 10,
        "FILE_NAME"         : "ATM_log.txt",
        "FILE_MAX_SIZE"     : 1024 * 1024 * 10,
        "FILE_MAX_NUMBER"   : 10,

        "LEVEL": {
            "INFO"      : 1,
            "WARNING"  : 2,
            "ERROR"     : 3,
            "CRITICAL"  : 4
        }
    }

    ACCESS_COUNTER = 30

    HOST = "google.com"
    PING_OPTION = "-c"
    PING_COUNT = 1
    PING_OPTION2 = "-w"
    PING_WAITING = 5
    EXCEPTION_COUNT = 30

    PING_CMD = "ping " + PING_OPTION + ' ' + str(PING_COUNT) + ' ' + PING_OPTION2 + ' ' + str(PING_WAITING) + ' ' + HOST

