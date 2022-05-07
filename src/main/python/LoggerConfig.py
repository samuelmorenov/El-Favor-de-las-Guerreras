import logging

def initLogger(level):
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    
    while rootLogger.hasHandlers():
        rootLogger.removeHandler(rootLogger.handlers[0])
        
    rootLogger.setLevel(level) #INFO/DEBUG
    
    fileHandler = logging.FileHandler("logfile.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)