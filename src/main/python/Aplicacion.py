# -*- coding: utf-8 -*-
import logging
import sys, os

base = os.path.dirname(__file__)
sys.path.insert(0, os.path.normpath(base+"/../.."))

from main.python.controladores.ControladorPartida import ControladorPartida
from main.python.controladores.ControladorGeneradorDatos import ControladorGeneradorDatos
from main.python.redNeuronal.Entrenamiento import Entrenamiento

import main.python.parametrizacion.ParametrosMenu as menu
import main.python.LoggerConfig as loggerConfig

if __name__ == "__main__":
    loggerConfig.initLogger(logging.INFO)
    logging.info('Inicio del programa.')
    
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        logging.info('Seleccionado modo de generacion de datos')
        loggerConfig.initLogger(None)
        ejecutor = ControladorGeneradorDatos()
    
    elif(menu.MODO == menu.MODO_JUGAR):
        logging.info('Seleccionado modo de juego')
        loggerConfig.initLogger(logging.INFO)
        ejecutor = ControladorPartida()
        
    elif(menu.MODO == menu.MODO_ENTRENAR_RED):
        logging.info('Seleccionado modo de entrenamiento de la red neuronal')
        loggerConfig.initLogger(logging.DEBUG)
        ejecutor = Entrenamiento()
        
    ejecutor.run()

    loggerConfig.initLogger(logging.INFO)
    logging.info('Fin del programa.')