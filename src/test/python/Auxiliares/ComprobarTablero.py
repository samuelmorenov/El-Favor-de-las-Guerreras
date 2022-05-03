#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import numpy as np

import main.python.parametrizacion.ParametrosTablero as const

lineaVacia = np.zeros(const.NCOLUMNA, dtype=int)

class ComprobarTablero(unittest.TestCase):
    
    def tableroCreacion(self, tablero):
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
    
    def tableroInicioPrimeraRonda(self, tablero):
        self.assertFalse(np.array_equal(tablero[const.MANO_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
        
    def tableroInicioSegundaRonda(self, tablero):
        self.assertFalse(np.array_equal(tablero[const.MANO_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
        
    def tableroMitadSegundaRonda(self, tablero):
        self.assertFalse(np.array_equal(tablero[const.MANO_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
        
    def tableroFinSegundaRonda(self, tablero):
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR1], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.MANO_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR1], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ACCIONES_USADAS_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR1], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.ARMAS_USADAS_JUGADOR2], lineaVacia))
        self.assertFalse(np.array_equal(tablero[const.FAVOR_DE_GUERRERA], lineaVacia))
        self.assertTrue(np.array_equal(tablero[const.ACCION_PENDIENTE], lineaVacia))
        
    def manoConNCartas(self, tablero, nCartas):
        mano = tablero[const.MANO_JUGADOR1]
        for i in range(0, const.NCOLUMNA, 1):
            carta = mano[i]
            if(i < const.NCOLUMNA-nCartas):
                self.assertEqual(carta, 0)
            else:
                self.assertNotEqual(carta, 0)
                
    def seVenLasCartasDeLasAcciones(self, acciones):
        self.assertNotEqual(acciones[const.TIPO_SECRETO], 0)
        self.assertNotEqual(acciones[const.TIPO_RENUNCIA_1], 0)
        self.assertNotEqual(acciones[const.TIPO_RENUNCIA_2], 0)
        self.assertEqual(acciones[const.TIPO_REGALO], 1)
        self.assertEqual(acciones[const.TIPO_COMPETICION], 1)
        
    def noSeVenLasCartasDeLasAcciones(self, acciones):
        self.assertEqual(acciones[const.TIPO_SECRETO], 1)
        self.assertEqual(acciones[const.TIPO_RENUNCIA_1], 1)
        self.assertEqual(acciones[const.TIPO_RENUNCIA_2], 1)
        self.assertEqual(acciones[const.TIPO_REGALO], 1)
        self.assertEqual(acciones[const.TIPO_COMPETICION], 1)
        
            
    def prepararTableroJugador1(self, turnos, controladorTablero, jugador1, jugador2):
        for _ in range(0, turnos, 1):
            self.__accion(controladorTablero, const.JUGADOR1, const.JUGADOR2, jugador1, jugador2)
            self.__accion(controladorTablero, const.JUGADOR2, const.JUGADOR1, jugador2, jugador1)
            
        return controladorTablero
            
    def __accion(self, controladorTablero, numeroJugador1, numeroJugador2, jugadorSeleccionadoComo1, jugadorSeleccionadoComo2):
        controladorTablero.jugadorRobaCarta(numeroJugador1)
        tablero = controladorTablero.getVistaTablero(numeroJugador1)
        accion = jugadorSeleccionadoComo1.decidirAccion(tablero)
        controladorTablero.realizarAccion(numeroJugador1, accion)
        
        if(controladorTablero.hayAccionPendiente()):
            tablero = controladorTablero.getVistaTablero(numeroJugador2)
            accionDeSeleccion = jugadorSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            controladorTablero.realizarAccion(numeroJugador2, accionDeSeleccion)

    def prepararAccionSeleccionJugador1(self, controladorTablero, jugador1, jugador2, tipo):
        for _ in range(0, const.N_ACCIONES, 1):
            self.__accionSimple(controladorTablero, const.JUGADOR1, const.JUGADOR2, jugador1, jugador2)
            if(controladorTablero.hayAccionPendiente()):
                self.__accionSeleccion(controladorTablero, const.JUGADOR2, jugador2)
            
            self.__accionSimple(controladorTablero, const.JUGADOR2, const.JUGADOR1, jugador2, jugador1)
            if(controladorTablero.hayAccionPendiente()):
                tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
                accionPendiente = tableroAux[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO]
                if(accionPendiente == tipo):
                    break
                else:
                    self.__accionSeleccion(controladorTablero, const.JUGADOR1, jugador1)
                
            
        return controladorTablero
    
    def __accionSimple(self, controladorTablero, numeroJugador1, numeroJugador2, jugadorSeleccionadoComo1, jugadorSeleccionadoComo2):
        controladorTablero.jugadorRobaCarta(numeroJugador1)
        tablero = controladorTablero.getVistaTablero(numeroJugador1)
        accion = jugadorSeleccionadoComo1.decidirAccion(tablero)
        controladorTablero.realizarAccion(numeroJugador1, accion)
        
    def __accionSeleccion(self, controladorTablero, numeroJugador2, jugadorSeleccionadoComo2):
        tablero = controladorTablero.getVistaTablero(numeroJugador2)
        accionDeSeleccion = jugadorSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
        controladorTablero.realizarAccion(numeroJugador2, accionDeSeleccion)

    def accionSeleccionCorrecta(self, accionSeleccion, tipoAccionEsperada):
        if(tipoAccionEsperada == const.TIPO_DECISION_REGALO):
            for i in range(len(accionSeleccion)):
                if(i == const.PENDIENTE_TIPO):
                    self.assertEqual(accionSeleccion[i], tipoAccionEsperada)
                elif(i == const.PENDIENTE_5_1):
                    self.assertNotEqual(accionSeleccion[i], 0)
                elif(i == const.PENDIENTE_5_2):
                    self.assertNotEqual(accionSeleccion[i], 0)
                elif(i == const.PENDIENTE_5_3):
                    self.assertNotEqual(accionSeleccion[i], 0)
                else:
                    self.assertEqual(accionSeleccion[i], 0)
                    
        if(tipoAccionEsperada == const.TIPO_DECISION_COMPETICION):
            for i in range(len(accionSeleccion)):
                if(i == const.PENDIENTE_TIPO):
                    self.assertEqual(accionSeleccion[i], tipoAccionEsperada)
                elif(i == const.PENDIENTE_6_1_1):
                    self.assertNotEqual(accionSeleccion[i], 0)
                elif(i == const.PENDIENTE_6_1_2):
                    self.assertNotEqual(accionSeleccion[i], 0)
                elif(i == const.PENDIENTE_6_2_1):
                    self.assertNotEqual(accionSeleccion[i], 0)
                elif(i == const.PENDIENTE_6_2_2):
                    self.assertNotEqual(accionSeleccion[i], 0)
                else:
                    self.assertEqual(accionSeleccion[i], 0)
                    
