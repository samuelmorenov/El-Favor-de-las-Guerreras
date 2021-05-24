# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import parameterization.ParametrosTablero as const
import parameterization.ParametrosMenu as menu

from training.Prediccion import Prediccion

class NeuralNetworkController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.Prediccion = Prediccion()
        
    def decidirAccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def __pedirAccion(self, tablero):
        if(menu.PRINT_TRACE):
            if(self.miNumero == const.JUGADOR1):
                print("\033[;33m",end="") #Amarillo
            if(self.miNumero == const.JUGADOR2):
                print("\033[;36m",end="") #Cian
            
            print("Soy "+self.miNombre)
            
            print("- Este es el tablero que me llega:")
            print(tablero)
            
        accion = self.Prediccion.predecir(tablero)
    
        if(menu.PRINT_TRACE):
            print("- Esta es la accion que realizo:")
            print(accion)
            print("\033[0m",end="")
            print("___________________________________") #Separador de bots
            
        return accion
    
    def finish(self):
        return
