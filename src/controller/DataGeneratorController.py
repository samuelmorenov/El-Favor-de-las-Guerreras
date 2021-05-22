# -*- coding: utf-8 -*-
import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')

from controller.PartidaController import PartidaController

import parameterization.ParametrosMenu as menu
import parameterization.ParametrosTablero as const
import parameterization.ParametrosDatos as data

class DataGeneratorController:
    def __init__(self):
        self.partidasGanadas1 = 0
        self.partidasGanadas2 = 0
        self.mainController = 0
        
        if(menu.MODO_ARCHIVOS == menu.MODO_ARCHIVOS_SEPARADO):
            self.__resetArchivo(data.PARTIDAS_GANADAS_JUGADAS)
            self.__resetArchivo(data.PARTIDAS_GANADAS_TABLERO)
        else:
            self.__resetArchivo(data.PARTIDAS_GANADAS_COMPLETO)
                
        for i in range(menu.NUM_SIMULACIONES):
            self.mainController = PartidaController('generacion')
            self.mainController.start()
            self.__guardarGanador(self.mainController.winner.miNumero)
                
            print("Partidas ganadas por el 1: "+ str(self.partidasGanadas1))
            print("Partidas ganadas por el 2: "+ str(self.partidasGanadas2))
            print()
            
            
    def __guardarGanador(self, jugador):
        acciones = ''
        tablero = ''
        tableroYAcciones = ''
        
        if(jugador == const.JUGADOR1):
            acciones = self.mainController.accionesj1
            tablero = self.mainController.tablerosj1
            tableroYAcciones = self.mainController.tablerosYAccionesj1
            self.partidasGanadas1 = self.partidasGanadas1 + 1
        else:
            acciones = self.mainController.accionesj2
            tablero = self.mainController.tablerosj2
            tableroYAcciones = self.mainController.tablerosYAccionesj2
            self.partidasGanadas2 = self.partidasGanadas2 + 1
            
            
        if(menu.MODO_ARCHIVOS == menu.MODO_ARCHIVOS_SEPARADO):
            self.__guardarEnArchivo(acciones, data.PARTIDAS_GANADAS_JUGADAS)
            self.__guardarEnArchivo(tablero, data.PARTIDAS_GANADAS_TABLERO)
        else:
            self.__guardarEnArchivo(tableroYAcciones, data.PARTIDAS_GANADAS_COMPLETO)
        
        if(menu.PRINT_TRACE):
            print("Ha ganado el "+str(jugador.miNombre))
            
    def __resetArchivo(self, path):
        if not os.path.exists(data.PARTIDAS_GANADAS_DIR):
            os.mkdir(data.PARTIDAS_GANADAS_DIR)
        with open(path, 'w') as f:
            f.write('')
        
        
    def __guardarEnArchivo(self, jugadas, path):
        with open(path, 'a') as f:
            f.write(jugadas)