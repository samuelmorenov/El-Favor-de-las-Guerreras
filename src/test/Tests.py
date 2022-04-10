#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from controller.BotTonto import BotTonto

import parameterization.ParametrosTablero as const

tablero = [[1,2,4,5,5,6,7],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]


class Test(unittest.TestCase):
    
    def __accionCorrecta(self, tablero, accion):
        listaAccionesPosibles = []
        accionesRealizadas = tablero[const.ACCIONES_USADAS_JUGADOR1]
        if(accionesRealizadas[const.TIPO_SECRETO] == 0):
            listaAccionesPosibles.append(const.TIPO_SECRETO)
        if(accionesRealizadas[const.TIPO_RENUNCIA_1] == 0):
            listaAccionesPosibles.append(const.TIPO_RENUNCIA)
        if(accionesRealizadas[const.TIPO_REGALO] == 0):
            listaAccionesPosibles.append(const.TIPO_REGALO)
        if(accionesRealizadas[const.TIPO_COMPETICION] == 0):
            listaAccionesPosibles.append(const.TIPO_COMPETICION)
            
        self.assertIn(accion[const.ACCION_REALIZADA], listaAccionesPosibles)
        
    
    def test_bot_accionCorrecta(self):
        bot = BotTonto("test", 0)
        accion = bot.decidirAccion(tablero)
        self.__accionCorrecta(tablero, accion)
        
if __name__ == "__main__":
    unittest.main()
