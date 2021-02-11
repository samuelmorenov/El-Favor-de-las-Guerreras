# -*- coding: utf-8 -*-

PLAYER = 1
COMPUTER = 2
LOG = True

class Controller:
    def __init__(self):
        self.tablero = {}
        self.mazo = [1,1,
                     2,2,
                     3,3,
                     4,4,4,
                     5,5,5,
                     6,6,6,6,
                     7,7,7,7,7]
        
        for i in range(1,7):
            for j in range(1,7):
                self.tablero[(i,j)] = 0
                if(i == j):
                    self.tablero[(i,j)] = 1
        
    def getTablero(self):
        return self.tablero
    
    def getMazo(self):
        return self.mazo
    
