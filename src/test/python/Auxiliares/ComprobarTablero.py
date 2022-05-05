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
                    
    def __seleccionarCartasDeMano(self, tablero, accion, nCartas):
        accionSeleccionada = []
        cartasSeleccionadas = []
        
        listaDeCartasEnMano = self.__getListaCartasEnMano(tablero[const.MANO_JUGADOR1])
                
        for i in range(const.NCOLUMNA):
            if(i == 0):
                accionSeleccionada.append(accion)
            if(i < nCartas):
                posicion = np.random.randint(len(listaDeCartasEnMano))
                carta = listaDeCartasEnMano.pop(posicion)
                accionSeleccionada.append(carta)
                cartasSeleccionadas.append(carta)
            else:
                accionSeleccionada.append(0)
        
        return accionSeleccionada, cartasSeleccionadas
    
    def __seleccionarCartasDeAccionPendiente(self, tablero, tipoAccion, accionCount, seleccionCount):
        accionSeleccionada = []
        cartasSeleccionadas = []
        cartasASeleccionar = []

        for i in range(len(tablero[const.ACCION_PENDIENTE])):
            if(i != const.PENDIENTE_TIPO and tablero[const.ACCION_PENDIENTE][i] != 0):
                cartasASeleccionar.append(tablero[const.ACCION_PENDIENTE][i])
                
        for i in range(const.NCOLUMNA):
            if(i == 0):
                accionSeleccionada.append(tipoAccion)
            elif(i <= seleccionCount):
                posicion = np.random.randint(len(cartasASeleccionar))
                carta = cartasASeleccionar.pop(posicion)
                accionSeleccionada.append(carta)
                cartasSeleccionadas.append(carta)
            else:
                accionSeleccionada.append(0)
        
        return accionSeleccionada, cartasSeleccionadas
    
    def __getListaCartasEnMano(self, mano):
        listaDeCartasEnMano = []
        for i in range(len(mano)):
            if(mano[i] != 0):
                listaDeCartasEnMano.append(mano[i])
        return listaDeCartasEnMano
             
    def __comprobarQueSeRealizaLaAccion(self, controladorTablero, accionARealizar, cartasUsadas, jugador, indexMano):
        cartasUsadas = np.sort(cartasUsadas)
        
        #Preparacion de datos:
        tableroAux = controladorTablero.getVistaTablero(jugador)
        manoAntes = tableroAux[indexMano]
        
        #Ejecucion de la accion:
        controladorTablero.realizarAccion(jugador, accionARealizar)
        
        #Preparacion de datos:
        tableroAux = controladorTablero.getVistaTablero(jugador)
        manoDespues = tableroAux[indexMano]
        
        #Comprobación de que se ha guardado en las acciones realizadas
        if(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_SECRETO):
            self.assertEqual(tableroAux[const.ACCIONES_USADAS_JUGADOR1][const.TIPO_SECRETO], cartasUsadas[0])
        elif(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_RENUNCIA):
            self.assertEqual(tableroAux[const.ACCIONES_USADAS_JUGADOR1][const.TIPO_RENUNCIA_1], cartasUsadas[0])
            self.assertEqual(tableroAux[const.ACCIONES_USADAS_JUGADOR1][const.TIPO_RENUNCIA_2], cartasUsadas[1])
        elif(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_REGALO):
            self.assertNotEqual(tableroAux[const.ACCIONES_USADAS_JUGADOR1][const.TIPO_REGALO], 0)
        elif(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_COMPETICION):
            self.assertNotEqual(tableroAux[const.ACCIONES_USADAS_JUGADOR1][const.TIPO_COMPETICION], 0)
            
        #Comprobacion de que se han usado las cartas
        if(accionARealizar[const.ACCION_REALIZADA] != const.TIPO_REGALO and accionARealizar[const.ACCION_REALIZADA] == const.TIPO_COMPETICION):
            listaDeCartasEnManoAntes = self.__getListaCartasEnMano(manoAntes)
            listaDeCartasEnManoDespues = self.__getListaCartasEnMano(manoDespues)
            for i in range(len(cartasUsadas)):
                listaDeCartasEnManoDespues.append(cartasUsadas[i])
                
            listaDeCartasEnManoAntesOrdenada = np.sort(listaDeCartasEnManoAntes)
            listaDeCartasEnManoDespuesOrdenada = np.sort(listaDeCartasEnManoDespues)
            for i in range(len(listaDeCartasEnManoAntes)):
                self.assertEquals(listaDeCartasEnManoAntesOrdenada[i], listaDeCartasEnManoDespuesOrdenada[i])
            
        #Comprobacion de que si es tipo 3 o 4 hay una accion pendiente
        if(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_REGALO):
            self.assertNotEqual(tableroAux[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO], accionARealizar[const.ACCION_REALIZADA])
        elif(accionARealizar[const.ACCION_REALIZADA] == const.TIPO_COMPETICION):
            self.assertNotEqual(tableroAux[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO], accionARealizar[const.ACCION_REALIZADA])
        
        
    def __comprobarExceptionAlRealizarLaAccion(self, controladorTablero, accionARealizar):
        with self.assertRaises(Exception):
            controladorTablero.realizarAccion(const.JUGADOR1, accionARealizar)
            
    def __getAccionCount(self, tipo):
        if(tipo == const.TIPO_SECRETO):
            return const.ACCION_1_COUNT
        
        elif(tipo == const.TIPO_RENUNCIA):
            return const.ACCION_2_COUNT
        
        elif(tipo == const.TIPO_REGALO):
            return const.ACCION_3_COUNT
        
        elif(tipo == const.TIPO_COMPETICION):
            return const.ACCION_4_COUNT
        
        elif(tipo == const.TIPO_DECISION_REGALO):
            return const.PENDIENTE_5_ELEGIDA_COUNT
        
        elif(tipo == const.TIPO_DECISION_COMPETICION):
            return const.PENDIENTE_6_ELEGIDA_COUNT
            
    def comprobarAccionDisponibleYBienFormada(self, controladorTablero, tipoAccion):
        controladorTablero.initRonda()
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        accionCount = self.__getAccionCount(tipoAccion)
        accion, cartas = self.__seleccionarCartasDeMano(tableroAux, tipoAccion, accionCount)
        
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accion, cartas, const.JUGADOR1, const.MANO_JUGADOR1)
        
    def comprobarAccionNoDisponible(self, controladorTablero, tipoAccion):
        controladorTablero.initRonda()
        accionCount = self.__getAccionCount(tipoAccion)
        
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = self.__seleccionarCartasDeMano(tableroAux, tipoAccion, accionCount)
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accion, cartas, const.JUGADOR1, const.MANO_JUGADOR1)
        for _ in range(accionCount):
            controladorTablero.jugadorRobaCarta(const.JUGADOR1)
        
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = self.__seleccionarCartasDeMano(tableroAux, tipoAccion, accionCount)
        self.__comprobarExceptionAlRealizarLaAccion(controladorTablero, accion)
        
    def comprobarAccionMalFormada(self, controladorTablero, tipoAccion):
        controladorTablero.initRonda()
        accionCount = self.__getAccionCount(tipoAccion)
        
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = self.__seleccionarCartasDeMano(tableroAux, tipoAccion, accionCount+1)
        
        self.__comprobarExceptionAlRealizarLaAccion(controladorTablero, accion)
        
    def comprobarAccionDeSeleccionDisponibleYBienFormada(self, controladorTablero, tipoAccion):
        controladorTablero.initRonda()
        
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR2)
        if(tipoAccion == const.TIPO_DECISION_REGALO):
            tipoAccionPreparacion = const.TIPO_REGALO
            accionCount = self.__getAccionCount(const.TIPO_REGALO)
        else:
            tipoAccionPreparacion = const.TIPO_COMPETICION
            accionCount = self.__getAccionCount(const.TIPO_COMPETICION)
        accionPreparacion, cartasPreparacion = self.__seleccionarCartasDeMano(tableroAux, tipoAccionPreparacion, accionCount)
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accionPreparacion, cartasPreparacion, const.JUGADOR2, const.MANO_JUGADOR2)

        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        seleccionCount = self.__getAccionCount(tipoAccion)
        accion, cartas = self.__seleccionarCartasDeAccionPendiente(tableroAux, tipoAccion, accionCount, seleccionCount)
        
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accion, cartas, const.JUGADOR1, const.MANO_JUGADOR1)
        
    def comprobarAccionDeSeleccionNoDisponible(self, controladorTablero, tipoAccion):

        if(tipoAccion == const.TIPO_DECISION_REGALO):
            accionCount = self.__getAccionCount(const.TIPO_REGALO)
            tipoAccionPreparacion = const.TIPO_COMPETICION
            accionCountPreparacion = self.__getAccionCount(const.TIPO_COMPETICION)
        else:
            accionCount = self.__getAccionCount(const.TIPO_COMPETICION)
            tipoAccionPreparacion = const.TIPO_REGALO
            accionCountPreparacion = self.__getAccionCount(const.TIPO_REGALO)
            
        controladorTablero.initRonda()
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR2)
        
        accionPreparacion, cartasPreparacion = self.__seleccionarCartasDeMano(tableroAux, tipoAccionPreparacion, accionCountPreparacion)
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accionPreparacion, cartasPreparacion, const.JUGADOR2, const.MANO_JUGADOR2)

        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        seleccionCount = self.__getAccionCount(tipoAccion)
        accion, cartas = self.__seleccionarCartasDeAccionPendiente(tableroAux, tipoAccion, accionCount, seleccionCount)
        
        self.__comprobarExceptionAlRealizarLaAccion(controladorTablero, accion)
        
    def comprobarAccionDeSeleccionMalFormada(self, controladorTablero, tipoAccion):
        controladorTablero.initRonda()
        
        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR2)
        if(tipoAccion == const.TIPO_DECISION_REGALO):
            tipoAccionPreparacion = const.TIPO_REGALO
            accionCount = self.__getAccionCount(const.TIPO_REGALO)
        else:
            tipoAccionPreparacion = const.TIPO_COMPETICION
            accionCount = self.__getAccionCount(const.TIPO_COMPETICION)
        accionPreparacion, cartasPreparacion = self.__seleccionarCartasDeMano(tableroAux, tipoAccionPreparacion, accionCount)
        self.__comprobarQueSeRealizaLaAccion(controladorTablero, accionPreparacion, cartasPreparacion, const.JUGADOR2, const.MANO_JUGADOR2)

        tableroAux = controladorTablero.getVistaTablero(const.JUGADOR1)
        seleccionCount = self.__getAccionCount(tipoAccion)
        accion, cartas = self.__seleccionarCartasDeAccionPendiente(tableroAux, tipoAccion, accionCount, seleccionCount+1)
        
        self.__comprobarExceptionAlRealizarLaAccion(controladorTablero, accion)
            
