#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import numpy as np

import main.python.parametrizacion.ParametrosTablero as const

lineaVacia = np.zeros(const.NCOLUMNA, dtype=int)

class ComprobarTablero(unittest.TestCase):
    
    def tableroVacio(self, tablero):
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
