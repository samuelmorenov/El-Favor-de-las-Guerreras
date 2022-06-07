# -*- coding: utf-8 -*-
import configparser

config = configparser.RawConfigParser()

#Desde python -> main/test -> src -> main
PATH_MAIN       = './../../main/'
PATH_PARAMETROS = PATH_MAIN + 'recursos/'
PATH_LOGGER     = PATH_MAIN + 'recursos/'
PATH_GENERADOS  = PATH_MAIN + 'recursos/entrenamiento/generados/'
PATH_MODELO     = PATH_MAIN + 'recursos/entrenamiento/modelo/'
PATH_IMAGENES   = PATH_MAIN + 'recursos/estaticos/'

ARCHIVO_PARAMETROS = 'parametros.properties'
config.read(PATH_PARAMETROS+ARCHIVO_PARAMETROS)

#Parametros del modo de ejecucion del programa

MODO = int(config.get('Menu', 'MODO'))

MODO_GENERAR_DATOS = int(1)
MODO_ENTRENAR_RED = int(2)
MODO_JUGAR = int(3)
MODO_COMPETICION = int(4)

NUM_SIMULACIONES = int(config.get('Menu', 'NUM_SIMULACIONES'))

MODO_DIFICULTAD = int(config.get('Menu', 'DIFICULTAD'))

MODO_FACIL = int(1)
MODO_DIFICIL = int(2)
