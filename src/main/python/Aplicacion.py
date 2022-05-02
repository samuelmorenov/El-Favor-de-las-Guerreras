# -*- coding: utf-8 -*-

import logging
import sys, os

from main.python.controladores.ControladorPartida import ControladorPartida
from main.python.controladores.ControladorGeneradorDatos import ControladorGeneradorDatos
from main.python.redNeuronal.Entrenamiento import Entrenamiento

import main.python.parametrizacion.ParametrosMenu as menu

def initLogger():
    logging.basicConfig(filename='logfile.log',level=logging.INFO)
    
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
    
    logging.getLogger().addHandler(logging.StreamHandler())
    
def initPath():
    base = os.path.dirname(__file__)
    sys.path.insert(0, os.path.normpath(base+"/..") )
    sys.path.insert(0, os.path.normpath(base+"/../..") )

if __name__ == "__main__":
    initLogger()
    initPath()
    logging.info('Inicio del programa.')
    
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        logging.info('Seleccionado modo de generacion de datos')
        run = ControladorGeneradorDatos()
    
    elif(menu.MODO == menu.MODO_JUGAR):
        logging.info('Seleccionado modo de juego')
        run = ControladorPartida()
        
    elif(menu.MODO == menu.MODO_ENTRENAR_RED):
        logging.info('Seleccionado modo de entrenamiento de la red neuronal')
        run = Entrenamiento()

    logging.info('Fin del programa.')