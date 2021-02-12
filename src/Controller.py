# -*- coding: utf-8 -*-

import numpy as np
from random import randrange

PLAYER = 1
COMPUTER = 2

class Controller:
    def __init__(self):
        self.initMazo()
        self.tablero = np.zeros((7,7), dtype=int)
                    
    def initMazo(self):
        self.mazo = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        self.robarCarta()
        
    def robarCarta(self):
        if(len(self.mazo) < 1):
            raise Exception("Mazo vacio")
        return self.mazo.pop(randrange(len(self.mazo)))
                