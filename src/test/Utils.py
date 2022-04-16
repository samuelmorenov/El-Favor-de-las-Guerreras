#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

import numpy as np

import parameterization.ParametrosTablero as const

tableroVacio = [[0,0,0,0,0,0,0], #MANO_JUGADOR1
               [0,0,0,0,0,0,0], #MANO_JUGADOR2
               [0,0,0,0,0,0,0], #ACCIONES_USADAS_JUGADOR1
               [0,0,0,0,0,0,0], #ACCIONES_USADAS_JUGADOR2
               [0,0,0,0,0,0,0], #ARMAS_USADAS_JUGADOR1
               [0,0,0,0,0,0,0], #ARMAS_USADAS_JUGADOR2
               [0,0,0,0,0,0,0], #FAVOR_DE_GUERRERA
               [0,0,0,0,0,0,0]] #ACCION_PENDIENTE

class Utils(unittest.TestCase):
    
    
    def accionCorrecta(self, actor, mano, accionesDisponibles):
        tablero = tableroVacio
        tablero[const.ACCIONES_USADAS_JUGADOR1] = accionesDisponibles
        tablero[const.MANO_JUGADOR1] = mano
        
        #Realización de accion a probar
        accion = actor.decidirAccion(tablero)
        
        #Comprobación de datos obtenidos
        #LA accion esta dentro de las posibles
        self.accionPosible(accion, accionesDisponibles)
        #La accion tiene un numero de cartas correcto
        numero = self.accionNumeroCartasCorrecto(accion)
        #La accion usa cartas disponibles en la mano
        self.accionCartasDisponibles(accion, mano, numero)
        
    def accionException(self, actor, mano, accionesDisponibles):
        tablero = tableroVacio
        tablero[const.ACCIONES_USADAS_JUGADOR1] = accionesDisponibles
        tablero[const.MANO_JUGADOR1] = mano
        
        with self.assertRaises(Exception):
            actor.decidirAccion(tablero)
    
    '''
        Comprueba que la accion esta dentro de las acciones no realizadas
        accion: es el array de la accion completa realizada
        accionesRealizadas: es el array del estado de las acciones realizadas
    '''
    def accionPosible(self, accion, accionesRealizadas):
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
    def accionNumeroCartasCorrecto(self, accion):
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
    def accionCartasDisponibles(self, accion, mano, numero):
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
