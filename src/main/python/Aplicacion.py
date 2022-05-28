# -*- coding: utf-8 -*-
import logging
import sys, os
import datetime

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
        
    elif(menu.MODO == menu.MODO_COMPETICION):
        logging.info('Seleccionado modo de competicion')
        loggerConfig.initLogger(None)
        ejecutor = ControladorGeneradorDatos()
        
    inicio = datetime.datetime.now()
    ejecutor.run()
    fin = datetime.datetime.now()
    duracion = fin - inicio
    datetime.timedelta(0, 4, 316543)
    duracion.seconds

    loggerConfig.initLogger(logging.INFO)
    logging.info('Duracion del programa: '+str(duracion.seconds)+' segundos.')
    logging.info('Fin del programa.')