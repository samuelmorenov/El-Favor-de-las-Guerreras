# -*- coding: utf-8 -*-

import logging
import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../../../')

from controller.PartidaController import PartidaController

import parameterization.ParametrosMenu as menu
import parameterization.ParametrosTablero as const
import parameterization.ParametrosDatos as data

class DataGeneratorController:
    def __init__(self):
        self.partidasGanadas1 = 0
        self.partidasGanadas2 = 0
        self.mainController = 0
        
        self.__resetArchivo(data.PARTIDAS_GANADAS_JUGADAS)
        self.__resetArchivo(data.PARTIDAS_GANADAS_TABLERO)
                
        for i in range(menu.NUM_SIMULACIONES):
            self.mainController = PartidaController()
            self.__guardarGanador(self.mainController.winner)
                
            logging.info("Partidas ganadas por el 1: "+ str(self.partidasGanadas1))
            logging.info("Partidas ganadas por el 2: "+ str(self.partidasGanadas2))
            
            
    def __guardarGanador(self, jugador):
        acciones = ''
        tablero = ''
        
        if(jugador.miNumero == const.JUGADOR1):
            acciones = self.mainController.accionesj1
            tablero = self.mainController.tablerosj1
            self.partidasGanadas1 = self.partidasGanadas1 + 1
        else:
            acciones = self.mainController.accionesj2
            tablero = self.mainController.tablerosj2
            self.partidasGanadas2 = self.partidasGanadas2 + 1
            
        self.__guardarEnArchivo(acciones, data.PARTIDAS_GANADAS_JUGADAS)
        self.__guardarEnArchivo(tablero, data.PARTIDAS_GANADAS_TABLERO)
        
        logging.info("Ha ganado el "+str(jugador.miNombre))
            
    def __resetArchivo(self, path):
        if not os.path.exists(data.PARTIDAS_GANADAS_DIR):
            os.mkdir(data.PARTIDAS_GANADAS_DIR)
        with open(path, 'w') as f:
            f.write('')
        
        
    def __guardarEnArchivo(self, jugadas, path):
        with open(path, 'a') as f:
            f.write(jugadas)