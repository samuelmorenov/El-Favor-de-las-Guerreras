# -*- coding: utf-8 -*-

import numpy as np
from random import randrange

N_CARTAS_INICIAL = 6

#Disposicion de las filas del tablero
MANO_JUGADOR1 = 0
MANO_JUGADOR2 = 1
ACCIONES_USADAS_JUGADOR1 = 1
ACCIONES_USADAS_JUGADOR2 = 2
ARMAS_USADAS_JUGADOR1 = 2
ARMAS_USADAS_JUGADOR2 = 3
FAVOR_DE_GUERRERA = 4
ACCION_PENDIENTE = 5

NFILA = 8 #Este numero depende de el numero de filas definidas arriba
NCOLUMNA = 7 #Este numero depende del numero maximo de cartas en la mano


class Controller:
    def __init__(self):
        self.__tablero = np.zeros((NFILA,NCOLUMNA), dtype=int)
        self.__initMazo()
        
    def __initMazo(self):
        self.__mazoArmas = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        
    #Elimina del mazo de cartas una carta random y la devuelve en el return
    def __robarCarta(self):
        if(len(self.__mazoArmas) < 1):
            raise Exception("Mazo vacio")
        return self.__mazoArmas.pop(randrange(len(self.__mazoArmas)))
        
    #Se reparten 6 cartas del mazo a cada jugador
    def __repartoDeCartas(self):
        for i in range(N_CARTAS_INICIAL):
            self.__conseguirCarta(MANO_JUGADOR1)
            self.__conseguirCarta(MANO_JUGADOR2)
            
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
    
    def getTablero(self, jugador):
        #TODO
        return 0
    
    def hacerRecuento(self):
        #TODO
        return True
        
#"""
    #Metodos auxiliares, en el futuno deben ser borrados
    
    def printMazo(self):
        print("Mazo:")
        print(self.__mazoArmas)
        
    def printTablero(self):
        print("Tablero:")
        print(self.__tablero)
          
#"""