# -*- coding: utf-8 -*-
import logging, os

from main.python.controladores.ControladorPartida import ControladorPartida

import main.python.parametrizacion.ParametrosMenu as menu
import main.python.parametrizacion.ParametrosTablero as const
import main.python.parametrizacion.ParametrosDatos as data

'''
Clase controladora de la generación de datos para el entrenamiento de la red 
neuronal.
'''
class ControladorGeneradorDatos:
    '''
    Método constructor de la clase ControladorGeneradorDatos, se inicializan 
    los atributos de la clase.
    '''
    def __init__(self):
        '''Atributo partidasGanadas1: Define el numero de partidas que ha 
        ganado el jugador numero 1.'''
        self.__partidasGanadas1 = 0
        '''Atributo partidasGanadas2: Define el numero de partidas que ha 
        ganado el jugador numero 2.'''
        self.__partidasGanadas2 = 0
        '''Atributo controladorPartida: Instancia la clase ControladorPartida, 
        que se va instanciando con cada nueva simulacion.'''
        self.__controladorPartida = None
        
    '''
    Método ejecutor de la clase ControladorGeneradorDatos, reinicia los 
    archivos y ejecuta partidas un número de veces parametrizado.
    '''
    def run(self):
        self.__resetArchivo(data.PARTIDAS_GANADAS_JUGADAS)
        self.__resetArchivo(data.PARTIDAS_GANADAS_TABLERO)
                
        for i in range(menu.NUM_SIMULACIONES):
            logger = logging.getLogger()
            logger.disabled = True
            
            self.__controladorPartida = ControladorPartida()
            self.__controladorPartida.run()
            self.__guardarGanador(self.__controladorPartida.getWinner())
            
            logger = logging.getLogger()
            logger.disabled = False
            logging.info("Partidas simuladas: "+str(i+1))
                
            if(menu.MODO == menu.MODO_COMPETICION):
                logging.info("Partidas ganadas por el 1: "+ str(self.__partidasGanadas1))
                logging.info("Partidas ganadas por el 2: "+ str(self.__partidasGanadas2))
            
    '''
    Método que dado un jugador obtiene los datos de su partida y los guarda en
    los ficheros de partidas ganadas.
    '''
    def __guardarGanador(self, jugador):
        acciones = ''
        tablero = ''
        
        if(jugador.getMiNumero() == const.JUGADOR1):
            acciones = self.__controladorPartida.getAccionesJ1()
            tablero = self.__controladorPartida.getTablerosJ1()
            self.__partidasGanadas1 = self.__partidasGanadas1 + 1
        else:
            acciones = self.__controladorPartida.getAccionesJ2()
            tablero = self.__controladorPartida.getTablerosJ2()
            self.__partidasGanadas2 = self.__partidasGanadas2 + 1
            
        self.__guardarEnArchivo(acciones, data.PARTIDAS_GANADAS_JUGADAS)
        self.__guardarEnArchivo(tablero, data.PARTIDAS_GANADAS_TABLERO)
        
        logging.info("Ha ganado el "+str(jugador.getMiNombre()))
            
    '''
    Método que elimina los archivos generados anteriormente y los deja limpios
    para una nueva generación.
    '''
    def __resetArchivo(self, path):
        if not os.path.exists(data.PARTIDAS_GANADAS_DIR):
            os.mkdir(data.PARTIDAS_GANADAS_DIR)
        with open(path, 'w') as f:
            f.write('')
            
    '''
    Método de escritura en fichero del texto dado.
    '''
    def __guardarEnArchivo(self, jugadas, path):
        with open(path, 'a') as f:
            f.write(jugadas)
            
