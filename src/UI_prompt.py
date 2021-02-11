# -*- coding: utf-8 -*-

from Controller import Controller

class UI_pront:
    def __init__(self):
        self.c = Controller()
        
    def printTablero(self):
        tablero = self.c.getTablero()
        print("Tablero:")
        for i in range(1,7):
            for j in range(1,7):
                print(str(tablero[(i,j)]), end=' ')
            print()
            
            
    def printMazo(self):
        mazo = self.c.getMazo()
        print("Mazo:")
        print(mazo)
        
        
        
        
ui = UI_pront()
ui.printTablero()
ui.printMazo()
    