# -*- coding: utf-8 -*-

from random import randrange

PLAYER = 1
COMPUTER = 2

class Controller:
    def __init__(self):
        self.mazo = []
        self.initMazo()
        
        self.tablero = {}
        self.initTablero()
                    
    def initMazo(self):
        self.mazo = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        self.robarCarta()
        
    def robarCarta(self):
        if(len(self.mazo) < 1):
            raise Exception("Mazo vacio")
        numeroGenerado = randrange(len(self.mazo))
        carta = self.mazo.pop(numeroGenerado)
        return carta
    
    def initTablero(self):
        for i in range(1,7):
            for j in range(1,7):
                self.tablero[(i,j)] = 0
                
    