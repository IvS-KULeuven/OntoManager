"""
A crude and simple logging module.
"""

###################################################################################################
# the loglevels
LOGLEVEL_ERROR = "ERROR"
LOGLEVEL_INFO  = "INFO"
LOGLEVEL_DEBUG = "DEBUG"
LOGLEVEL_OFF   = "OFF"
###################################################################################################

###################################################################################################
# global variable that determines the current loglevel. OFF by default.
LOGLEVEL = LOGLEVEL_OFF
###################################################################################################



def SET_LOGLEVEL(loglevel):
    """
    Set the loglevel to a new value
    """
    global LOGLEVEL
    LOGLEVEL = loglevel


def LOG(text=""):
    """
    Log the given text, regardless of the loglevel.
    """
    print(("%s" %str(text)))


def do_DEBUG():
    """
    Find out if debugging is being done: i.e. if the loglevel is set to DEBUG.
    """
    global LOGLEVEL, LOGLEVEL_DEBUG
    return LOGLEVEL == LOGLEVEL_DEBUG


def DEBUG(text=""):
    """
    Log the given text in case the loglevel is set to DEBUG.
    """
    global LOGLEVEL, LOGLEVEL_DEBUG
    if LOGLEVEL in [LOGLEVEL_DEBUG]:
        print(("%s" %str(text)))


def INFO(text=""):
    """
    Log the given text in case the loglevel is set to INFO or DEBUG.
    """
    global LOGLEVEL, LOGLEVEL_INFO, LOGLEVEL_DEBUG
    if LOGLEVEL in [LOGLEVEL_INFO, LOGLEVEL_DEBUG]:
        print(("%s" %str(text)))


def ERROR(text=""):
    """
    Log the given text as an error.
    """
    print(("!! %s" %text))
