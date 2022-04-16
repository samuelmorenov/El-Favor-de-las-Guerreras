#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

#import parameterization.ParametrosTablero as const

from main.python.controller.BotTonto import BotTonto
from Utils import Utils

utils = Utils() 

accionesDisponiblesTodas            = [0,0,0,0,0,0,0]
accionesDisponiblesSecreto          = [0,2,3,1,1,0,0]
accionesDisponiblesRenuncia         = [2,0,0,1,1,0,0]
accionesDisponiblesRegalo           = [2,3,4,0,1,0,0]
accionesDisponiblesCompeticion      = [2,3,4,1,0,0,0]
accionesDisponiblesNinguna          = [2,3,4,0,1,1,0]

mano7CartasDistintas = [1,2,3,4,5,6,7]
mano4Iguales = [7,7,7,7,0,0,0]
mano3Iguales = [7,7,7,0,0,0,0]
mano2Iguales = [7,7,0,0,0,0,0]
mano1Iguales = [7,0,0,0,0,0,0]
manoVacia = [7,0,0,0,0,0,0]


class Test(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.bot = BotTonto("Bot de testing", 0)
    
    '''    
    Prueba del bot, seleccion de accion con:
        4 acciones libres
        7 cartas distintas a elegir
    '''
    def test_caso_1(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesTodas)
        
    '''    
    Prueba del bot, seleccion de accion con:
        4 acciones libres
        4 cartas iguales a elegir
    '''
    def test_caso_2(self):
        utils.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesTodas)
        
    '''    
    Prueba del bot, seleccion de accion con:
        4 acciones libres
        0 cartas a elegir        
    '''
    def test_caso_3(self):
        utils.accionException(self.bot, manoVacia, accionesDisponiblesTodas)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Secreto
        7 cartas distintas a elegir        
    '''
    def test_caso_4(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesSecreto)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Secreto
        1 carta a elegir
    '''
    def test_caso_5(self):
        utils.accionCorrecta(self.bot, mano1Iguales, accionesDisponiblesSecreto)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Renuncia
        7 cartas distintas a elegir
    '''
    def test_caso_6(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRenuncia)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Renuncia
        2 de cartas a elegir, todas iguales
    '''
    def test_caso_7(self):
        utils.accionCorrecta(self.bot, mano2Iguales, accionesDisponiblesRenuncia)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Regalo
        7 cartas distintas a elegir
    '''
    def test_caso_8(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRegalo)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Regalo
        3 de cartas a elegir, todas iguales
    '''
    def test_caso_9(self):
        utils.accionCorrecta(self.bot, mano3Iguales, accionesDisponiblesRegalo)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Competicion
        7 cartas distintas a elegir
    '''
    def test_caso_10(self):
        utils.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesCompeticion)

    '''    
    Prueba del bot, seleccion de accion con:
        Accion libre de tipo Competicion
        4 de cartas a elegir, todas iguales
    '''
    def test_caso_11(self):
        utils.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesCompeticion)

    '''    
    Prueba del bot, seleccion de accion con:
        Sin acciones libres
    '''
    def test_caso_12(self):
        utils.accionException(self.bot, mano7CartasDistintas, accionesDisponiblesNinguna)

        
if __name__ == "__main__":
    unittest.main()
