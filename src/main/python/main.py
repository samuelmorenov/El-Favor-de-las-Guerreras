# -*- coding: utf-8 -*-

import logging
from controller.PartidaController import PartidaController
from training.Entrenamiento import Entrenamiento
from controller.DataGeneratorController import DataGeneratorController

import parameterization.ParametrosMenu as menu

def initLogger():
    logging.basicConfig(filename='logfile.log',level=logging.INFO)
    
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
    
    logging.getLogger().addHandler(logging.StreamHandler())

if __name__ == "__main__":
    initLogger()
    logging.info('Inicio del programa.')
    
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        logging.info('Seleccionado modo de generacion de datos')
        main = DataGeneratorController()
    
    elif(menu.MODO == menu.MODO_JUGAR):
        logging.info('Seleccionado modo de juego')
        main = PartidaController()
        
    elif(menu.MODO == menu.MODO_ENTRENAR_RED):
        logging.info('Seleccionado modo de entrenamiento de la red neuronal')
        main = Entrenamiento()

    logging.info('Fin del programa.')