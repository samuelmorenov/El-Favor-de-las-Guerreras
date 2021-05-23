# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from training.Prediccion import Prediccion

class JugadorController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.Prediccion = Prediccion()
        
    def decidirAccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def __pedirAccion(self, tablero):
        return self.Prediccion.predecir(tablero)
    
    def finish(self):
        return
