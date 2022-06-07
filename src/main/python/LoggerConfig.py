import logging

def initLogger(level):
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    logger = logging.getLogger()
    
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
        
    if(level == None):
        return
        
    logger.setLevel(level) #INFO/DEBUG
    
    #Desde python -> main/test -> src -> main -> recursos
    path_dir = './../../main/recursos/'
    nombre = 'logger.log'
    fileHandler = logging.FileHandler(path_dir+nombre)
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    
    logger.disabled = False
    
