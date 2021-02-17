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