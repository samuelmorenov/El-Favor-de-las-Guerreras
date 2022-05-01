#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

#import parameterization.ParametrosTablero as const

from main.python.controller.BotTonto import BotTonto
from main.python.controller.NeuralNetworkController import NeuralNetworkController
from utils.Utils import Utils

utils = Utils() 

accionesDisponiblesTodas            = [0,0,0,0,0,0,0]
accionesDisponiblesSecreto          = [0,2,3,1,1,0,0]
accionesDisponiblesRenuncia         = [2,0,0,1,1,0,0]
accionesDisponiblesRegalo           = [2,3,4,0,1,0,0]
accionesDisponiblesCompeticion      = [2,3,4,1,0,0,0]
accionesDisponiblesNinguna          = [2,3,4,1,1,1,0]

mano7CartasDistintas = [1,2,3,4,5,6,7]
mano4Iguales = [7,7,7,7,0,0,0]
mano3Iguales = [7,7,7,0,0,0,0]
mano2Iguales = [7,7,0,0,0,0,0]
mano1Iguales = [7,0,0,0,0,0,0]
manoVacia = [0,0,0,0,0,0,0]

cartasAccionSeleccionRegalo0Iguales = [5,1,2,3,0,0,0]
cartasAccionSeleccionRegalo2Iguales = [5,1,1,2,0,0,0]
cartasAccionSeleccionRegalo3Iguales = [5,4,4,4,0,0,0]

cartasAccionSeleccionCompeticionIguales = [6,7,7,7,7,0,0]
cartasAccionSeleccionCompeticionDistintas = [6,7,7,6,6,0,0]

class Test(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.bot = BotTonto("Bot de testing", 0)
        self.redNeuronal = NeuralNetworkController("Red neuronal de testing", 0)
        
    #-----------------------Bot Seleccionar accion-----------------------   
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    7 cartas distintas a elegir
    def test_caso_1(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_2(self):
        utils.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_3(self):
        utils.accionException(self.bot, manoVacia, accionesDisponiblesTodas)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_4(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_5(self):
        utils.accionCorrecta(self.bot, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_6(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_7(self):
        utils.accionCorrecta(self.bot, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_8(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_9(self):
        utils.accionCorrecta(self.bot, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_10(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_11(self):
        utils.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_12(self):
        utils.accionException(self.bot, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Bot Seleccionar accion de seleccion-----------------'''
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_13(self):
        utils.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_14(self):
        utils.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_15(self):
        utils.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_16(self):
        utils.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_17(self):
        utils.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionDistintas)
        
    #-----------------------Red neuronal Seleccionar accion-----------------------   
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    7 cartas distintas a elegir
    def test_caso_18(self):
        utils.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_19(self):
        utils.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_20(self):
        utils.accionException(self.redNeuronal, manoVacia, accionesDisponiblesTodas)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_21(self):
        utils.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_22(self):
        utils.accionCorrecta(self.redNeuronal, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_23(self):
        utils.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_24(self):
        utils.accionCorrecta(self.redNeuronal, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_25(self):
        utils.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_26(self):
        utils.accionCorrecta(self.redNeuronal, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_27(self):
        utils.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_28(self):
        utils.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_29(self):
        utils.accionException(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Red neuronal Seleccionar accion de seleccion-----------------'''
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_30(self):
        utils.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_31(self):
        utils.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_32(self):
        utils.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_33(self):
        utils.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_34(self):
        utils.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionDistintas)
        
    
if __name__ == "__main__":
    unittest.main()
