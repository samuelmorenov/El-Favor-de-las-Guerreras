#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

import parameterization.ParametrosTablero as const

class Utils(unittest.TestCase):
    
    def accionCorrecta(self, tablero, accion):
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
