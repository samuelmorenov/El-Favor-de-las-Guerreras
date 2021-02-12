# -*- coding: utf-8 -*-

import numpy as np
from random import randrange

JUGADOR1 = 0
JUGADOR2 = 6

class Controller:
    def __init__(self):
        self.initMazo()
        self.initTablero()
                    
    #Se inicializa el mazo con todas las cartas menos una
    def initMazo(self):
        self.mazo = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        self.robarCarta()
        
    #Elimina del mazo de cartas una carta random y la devuelve en el return
    def robarCarta(self):
        if(len(self.mazo) < 1):
            raise Exception("Mazo vacio")
        return self.mazo.pop(randrange(len(self.mazo)))
    
    #Se inicializa el tablero y se reparten las cartas
    def initTablero(self):
        self.tablero = np.zeros((7,7), dtype=int)
        self.repartoDeCartas()
        
    #Se reparten 6 cartas del mazo a cada jugador
    def repartoDeCartas(self):
        for i in range(6):
            self.conseguirCarta(JUGADOR1)
            self.conseguirCarta(JUGADOR2)
            
    #Se le asigna una carta del mazo a la mano del jugador
    def conseguirCarta(self, jugador):
        mano = self.tablero[jugador]
        mano = np.delete(mano, [0])
        carta = self.robarCarta()
        mano = np.append(mano, carta)
        self.tablero[jugador] = mano
        
        
#c = Controller()
#print(c.tablero)
#print(c.mazo)