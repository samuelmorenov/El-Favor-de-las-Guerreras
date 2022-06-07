# -*- coding: utf-8 -*-
import configparser

config = configparser.RawConfigParser()

#Desde python -> main/test -> src -> main -> recursos
path_dir = './../../main/recursos/'
nombre = 'parametros.properties'
config.read(path_dir+nombre)

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
