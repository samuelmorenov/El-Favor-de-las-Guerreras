# -*- coding: utf-8 -*-

import numpy as np

import Constantes as const


class Controller:
    def __init__(self):
        self.__tablero = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        self.__initMazo()
        
    def __initMazo(self):
        self.__mazoArmas = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        
    #Elimina del mazo de cartas una carta random y la devuelve en el return
    def __robarCarta(self):
        if(len(self.__mazoArmas) < 1):
            raise Exception("Mazo vacio")
        return self.__mazoArmas.pop(np.random.randint(len(self.__mazoArmas)))
        
    #Se reparten 6 cartas del mazo a cada jugador
    def __repartoDeCartas(self):
        for i in range(const.N_CARTAS_INICIAL):
            self.__conseguirCarta(const.MANO_JUGADOR1)
            self.__conseguirCarta(const.MANO_JUGADOR2)
            
    #Se le asigna una carta del mazo a la mano del jugador
    def __conseguirCarta(self, jugador):
        mano = self.__tablero[jugador]
        mano = np.delete(mano, [0]) #Eliminamos un hueco sin usar
        carta = self.__robarCarta()
        mano = np.append(mano, carta)
        self.__tablero[jugador] = mano
        
    #Se inicializa el mazo con todas las cartas menos una y se reparten las cartas iniciales
    def initRonda(self):
        self.__initMazo()
        self.__robarCarta()
        self.__repartoDeCartas()
    
    def getVistaTablero(self, jugador):
        tableroParcial = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        
        """MANO"""
        tableroParcial[const.MANO_JUGADOR1] = self.__tablero[jugador]

        """ACCIONES"""
        accionesJugador = const.ACCIONES_USADAS_JUGADOR1
        accionesAdversario = const.ACCIONES_USADAS_JUGADOR2
        if(jugador == const.JUGADOR2):
            accionesJugador = const.ACCIONES_USADAS_JUGADOR2
            accionesAdversario = const.ACCIONES_USADAS_JUGADOR1
        
        tableroParcial[const.ACCIONES_USADAS_JUGADOR1] = self.__tablero[accionesJugador]

        accionesVistas = self.__tablero[accionesAdversario]
        print(accionesVistas)
        accionesOcultas = np.zeros(const.NCOLUMNA, dtype=int)
        for i in range(const.NCOLUMNA):
            if(accionesVistas[i] != 0):
                accionesOcultas[i] = 1
            
        tableroParcial[const.ACCIONES_USADAS_JUGADOR2] =  accionesOcultas
        
        """ARMAS USADAS"""
        armasJugador = const.ARMAS_USADAS_JUGADOR1
        armasAdversario = const.ARMAS_USADAS_JUGADOR2
        if(jugador == const.JUGADOR2):
            armasJugador = const.ARMAS_USADAS_JUGADOR2
            armasAdversario = const.ARMAS_USADAS_JUGADOR1
        
        tableroParcial[const.ARMAS_USADAS_JUGADOR1] = self.__tablero[armasJugador]
        tableroParcial[const.ARMAS_USADAS_JUGADOR2] = self.__tablero[armasAdversario]
        
        tableroParcial[const.FAVOR_DE_GUERRERA] = self.__tablero[const.FAVOR_DE_GUERRERA]
        tableroParcial[const.ACCION_PENDIENTE] = self.__tablero[const.ACCION_PENDIENTE]
        
        return tableroParcial
    
    def hacerRecuento(self):
        #TODO
        return True
        
"""
    #Metodos auxiliares, en el futuno deben ser borrados
    
    def printMazo(self):
        print("Mazo:")
        print(self.__mazoArmas)
        
    def printTablero(self):
        print("Tablero:")
        print(self.__tablero)
          
#"""