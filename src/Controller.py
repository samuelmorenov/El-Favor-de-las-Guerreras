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
        self.__ordenarMano(const.MANO_JUGADOR1)
        self.__ordenarMano(const.MANO_JUGADOR2)
            
    #Se le asigna una carta del mazo a la mano del jugador
    def __conseguirCarta(self, jugadorIndex):
        manoList = self.__tablero[jugadorIndex]
        cartaNula = 0
        manoList = self.__eliminarCarta(manoList, cartaNula) #Eliminamos un hueco sin usar
        cartaValue = self.__robarCarta()
        manoList = np.append(manoList, cartaValue)
        self.__tablero[jugadorIndex] = manoList
        
    def __soltarCarta(self, manoList, cartaValue):
        manoList = self.__eliminarCarta(manoList, cartaValue)
        cartaNula = 0
        manoList = np.append(manoList, cartaNula)
        return manoList
        
    def __eliminarCarta(self, manoList, cartaValue):
        return np.delete(manoList, np.argwhere(manoList == cartaValue)[0])
    
    def __getFilaAcciones(self, jugadorIndex):
        filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR2
            
        return filaAccionesIndex
    
    def __getMano(self, jugadorIndex):
        manoIndex = const.MANO_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            manoIndex = const.MANO_JUGADOR2
        return manoIndex
    
    def __ordenarMano(self, manoIndex):
        manoList = self.__tablero[manoIndex]
        manoList = np.sort(manoList)
        self.__tablero[manoIndex] = manoList

    #Se inicializa el mazo con todas las cartas menos una y se reparten las cartas iniciales
    def initRonda(self):
        self.__initMazo()
        self.__robarCarta()
        self.__repartoDeCartas()
        
    def jugadorRobaCarta(self, jugador):
        mano = self.__getMano(jugador)
        self.__conseguirCarta(mano)
        self.__ordenarMano(mano)
    
    def getVistaTablero(self, jugadorIndex):
        if(jugadorIndex != const.JUGADOR1 and jugadorIndex != const.JUGADOR2):
            raise Exception("Jugador no existente")
        
        tableroParcial = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        
        """MANO"""
        manoIndex = self.__getMano(jugadorIndex)
        tableroParcial[const.MANO_JUGADOR1] = self.__tablero[manoIndex].copy()

        """ACCIONES"""
        accionesJugador = const.ACCIONES_USADAS_JUGADOR1
        accionesAdversario = const.ACCIONES_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            accionesJugador = const.ACCIONES_USADAS_JUGADOR2
            accionesAdversario = const.ACCIONES_USADAS_JUGADOR1
        
        tableroParcial[const.ACCIONES_USADAS_JUGADOR1] = self.__tablero[accionesJugador].copy()

        accionesVistas = self.__tablero[accionesAdversario].copy()
        accionesOcultas = np.zeros(const.NCOLUMNA, dtype=int)
        for i in range(const.NCOLUMNA):
            if(accionesVistas[i] != 0):
                accionesOcultas[i] = 1
            
        tableroParcial[const.ACCIONES_USADAS_JUGADOR2] =  accionesOcultas
        
        """ARMAS USADAS"""
        armasJugador = const.ARMAS_USADAS_JUGADOR1
        armasAdversario = const.ARMAS_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            armasJugador = const.ARMAS_USADAS_JUGADOR2
            armasAdversario = const.ARMAS_USADAS_JUGADOR1
        
        tableroParcial[const.ARMAS_USADAS_JUGADOR1] = self.__tablero[armasJugador].copy()
        tableroParcial[const.ARMAS_USADAS_JUGADOR2] = self.__tablero[armasAdversario].copy()
        
        tableroParcial[const.FAVOR_DE_GUERRERA] = self.__tablero[const.FAVOR_DE_GUERRERA].copy()
        tableroParcial[const.ACCION_PENDIENTE] = self.__tablero[const.ACCION_PENDIENTE].copy()
        
        return tableroParcial.copy()
    
    
    def realizarAccion(self, jugadorIndex, accionArray):
        if(jugadorIndex != const.JUGADOR1 and jugadorIndex != const.JUGADOR2):
            raise Exception("Jugador no existente")
            
        filaAcciones = self.__getFilaAcciones(jugadorIndex)
        manoIndex = self.__getMano(jugadorIndex)
            
        if(accionArray[const.ACCION_REALIZADA] == const.TIPO_SECRETO): 
            if(self.__tablero[filaAcciones][0] == 0):
                self.__accion1(manoIndex, filaAcciones,
                               accionArray[const.ACCION_1])
            else:
                raise Exception("Accion 1 ya usada")
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_RENUNCIA): 
            if(self.__tablero[filaAcciones][1] == 0 and self.__tablero[filaAcciones][2] == 0):
                self.__accion2(manoIndex, filaAcciones,
                               accionArray[const.ACCION_2_1],
                               accionArray[const.ACCION_2_2])
            else:
                raise Exception("Accion 2 ya usada")
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_REGALO): 
            if(self.__tablero[filaAcciones][3] == 0):
                self.__accion3(manoIndex, filaAcciones,
                               accionArray[const.ACCION_3_1],
                               accionArray[const.ACCION_3_2],
                               accionArray[const.ACCION_3_3])
            else:
                raise Exception("Accion 3 ya usada")
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_COMPETICION): 
            if(self.__tablero[filaAcciones][4] == 0):
                self.__accion4(manoIndex, filaAcciones,
                           accionArray[const.ACCION_4_1_1], 
                           accionArray[const.ACCION_4_1_2], 
                           accionArray[const.ACCION_4_2_1], 
                           accionArray[const.ACCION_4_2_2])
            else:
                raise Exception("Accion 4 ya usada")
            
        else:
            raise Exception("Accion no encontrada")
        
    def __accion1(self, manoIndex, filaAccionesIndex, carta1):
        self.__tablero[filaAccionesIndex][const.TIPO_SECRETO] = carta1
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        self.__tablero[manoIndex] = manoList
        
    def __accion2(self, manoIndex, filaAccionesIndex, carta1, carta2):
        if(carta1 > carta2):
            carta1,carta2 = carta2,carta1
        
        self.__tablero[filaAccionesIndex][const.TIPO_RENUNCIA_1] = carta1
        self.__tablero[filaAccionesIndex][const.TIPO_RENUNCIA_2] = carta2
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        self.__tablero[manoIndex] = manoList
        
    def __accion3(self, manoIndex, filaAccionesIndex, carta1, carta2, carta3):
        self.__tablero[filaAccionesIndex][const.TIPO_REGALO] = 1
        #TODO: Preparar decision
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        manoList = self.__soltarCarta(manoList, carta3)
        self.__tablero[manoIndex] = manoList
        
        
    def __accion4(self, manoIndex, filaAccionesIndex, carta1, carta2, carta3, carta4):
        self.__tablero[filaAccionesIndex][const.TIPO_COMPETICION] = 1
        #TODO: Preparar decision
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        manoList = self.__soltarCarta(manoList, carta3)
        manoList = self.__soltarCarta(manoList, carta4)
        self.__tablero[manoIndex] = manoList
        
    def hacerRecuento(self):
        #TODO
        print("Haciendo recuento... Fin de pertida")
        print(self.__tablero)
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