#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

import numpy as np

import parameterization.ParametrosTablero as const

tableroVacio = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)

class Utils(unittest.TestCase):
    
    
    def accionCorrecta(self, actor, mano, accionesDisponibles):
        tablero = tableroVacio
        tablero[const.ACCIONES_USADAS_JUGADOR1] = accionesDisponibles
        tablero[const.MANO_JUGADOR1] = mano
        
        #Realización de accion a probar
        accion = actor.decidirAccion(tablero)
        
        #Comprobación de datos obtenidos
        #LA accion esta dentro de las posibles
        self.__accionPosible(accion, accionesDisponibles)
        #La accion tiene un numero de cartas correcto
        numero = self.__accionNumeroCartasCorrecto(accion)
        #La accion usa cartas disponibles en la mano
        self.__accionCartasDisponibles(accion, mano, numero)
        
    def accionException(self, actor, mano, accionesDisponibles):
        tablero = tableroVacio
        tablero[const.ACCIONES_USADAS_JUGADOR1] = accionesDisponibles
        tablero[const.MANO_JUGADOR1] = mano
        
        with self.assertRaises(Exception):
            actor.decidirAccion(tablero)
            
            
    def accionSeleccionCorrecta(self, actor, accionSeleccion):
        #Neuronal Network : Esta es la accion pendiente que me llega: [5 4 5 6 0 0 0]
        #Neuronal Network : Esta es la accion completa que realizo: [5 5 0 0 0 0 0]
        tablero = tableroVacio
        tablero[const.ACCION_PENDIENTE] = accionSeleccion
        
        accion = actor.decidirAccionDeSeleccion(tablero)
        
        self.assertEqual(accion[const.PENDIENTE_TIPO], accionSeleccion[const.PENDIENTE_TIPO])
        
        cartasSeleccionadas = 0
        cartasPosibles = []
        
        if(accion[const.PENDIENTE_TIPO] == const.TIPO_DECISION_REGALO):
            cartasSeleccionadas = accion[const.PENDIENTE_5_ELEGIDA]
            cartasPosibles.append(accionSeleccion[const.PENDIENTE_5_1])
            cartasPosibles.append(accionSeleccion[const.PENDIENTE_5_2])
            cartasPosibles.append(accionSeleccion[const.PENDIENTE_5_3])
        if(accion[const.PENDIENTE_TIPO] == const.TIPO_DECISION_COMPETICION):
            cartasSeleccionadas = []
            cartasSeleccionadas.append(accion[const.PENDIENTE_6_ELEGIDA_1])
            cartasSeleccionadas.append(accion[const.PENDIENTE_6_ELEGIDA_1])
            
            cartasPosibles1 = []
            cartasPosibles1.append(accionSeleccion[const.PENDIENTE_6_1_1])
            cartasPosibles1.append(accionSeleccion[const.PENDIENTE_6_1_2])
            cartasPosibles2 = []
            cartasPosibles2.append(accionSeleccion[const.PENDIENTE_6_2_1])
            cartasPosibles2.append(accionSeleccion[const.PENDIENTE_6_2_2])
            
            cartasPosibles.append(cartasPosibles1)
            cartasPosibles.append(cartasPosibles2)
            
        self.assertIn(cartasSeleccionadas, cartasPosibles)
        
        
    
    '''
        Comprueba que la accion esta dentro de las acciones no realizadas
        accion: es el array de la accion completa realizada
        accionesRealizadas: es el array del estado de las acciones realizadas
    '''
    def __accionPosible(self, accion, accionesRealizadas):
        listaAccionesPosibles = []
        if(accionesRealizadas[const.TIPO_SECRETO] == 0):
            listaAccionesPosibles.append(const.TIPO_SECRETO)
        if(accionesRealizadas[const.TIPO_RENUNCIA] == 0):
            listaAccionesPosibles.append(const.TIPO_RENUNCIA)
        if(accionesRealizadas[const.TIPO_REGALO] == 0):
            listaAccionesPosibles.append(const.TIPO_REGALO)
        if(accionesRealizadas[const.TIPO_COMPETICION] == 0):
            listaAccionesPosibles.append(const.TIPO_COMPETICION)
            
        self.assertIn(accion[const.ACCION_REALIZADA], listaAccionesPosibles)
        
    '''
        Comprueba que el numero de cartas seleccionado corresponde con la accion
        accion: es el array de la accion completa realizada
    '''
    def __accionNumeroCartasCorrecto(self, accion):
        num = self.__getNumeroCartasSeleccionadas(accion)
        self.assertNotEqual(num, 0) #Comprobamos que no es 0
        
        numObjetivo = 0
        
        if(accion[const.ACCION_REALIZADA] == const.TIPO_SECRETO):
            numObjetivo = const.ACCION_1_COUNT
        if(accion[const.ACCION_REALIZADA] == const.TIPO_RENUNCIA):
            numObjetivo = const.ACCION_2_COUNT
        if(accion[const.ACCION_REALIZADA] == const.TIPO_REGALO):
            numObjetivo = const.ACCION_3_COUNT
        if(accion[const.ACCION_REALIZADA] == const.TIPO_COMPETICION):
            numObjetivo = const.ACCION_4_COUNT
        
        self.assertEqual(num, numObjetivo)
        
        return numObjetivo
    
    '''
        Comprueba que las cartas de la accion estan en la mano
        accion: es el array de la accion completa realizada
        mano: es el array de las cartas que hay en mano
        numero: es el numero de cartas que tiene la accion
    '''
    def __accionCartasDisponibles(self, accion, mano, numero):
        manoRestante = mano
        for i in range(1, numero+1, 1):
            carta = accion[i]
            self.assertIn(carta, manoRestante)
            manoRestante = self.__eliminarCarta(manoRestante, carta)
            
        
    def __getNumeroCartasSeleccionadas(self, accion):
        num = 0
        empiezanLosCeros = False
        error = False
        for i in range(1, len(accion), 1):
            if((accion[i] != 0) & (not empiezanLosCeros)):
                num = num + 1
            elif((accion[i] == 0) & (not empiezanLosCeros)):
                empiezanLosCeros = True
            elif((accion[i] != 0) & empiezanLosCeros):
                error = True
                break
            elif((accion[i] == 0) & empiezanLosCeros):
                continue
        if(error):
            return 0
        else:
            return num
        
    def __eliminarCarta(self, lista, valor):
        return np.delete(lista, np.argwhere(lista == valor)[0])
