# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import numpy as np

import parameterization.ParametrosTablero as const
import parameterization.ParametrosMenu as menu

from training.Prediccion import Prediccion

class NeuralNetworkController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.Prediccion = Prediccion()
        
    def decidirAccion(self, tablero):
        return #TODO
    
    def decidirAccionDeSeleccion(self, tablero):
        return #TODO
    
    def finish(self):
        return
