# -*- coding: utf-8 -*-

from Controller import Controller

class UI_pront:
    def __init__(self):
        self.c = Controller()
        
    def printTablero(self):
        print("Tablero:")
        for i in range(1,7):
            for j in range(1,7):
                print(str(self.c.tablero[(i,j)]), end=' ')
            print()

            
    def printMazo(self):
        print("Mazo:")
        print(self.c.mazo)
        
    def robarTodoElMazo(self):
        print("Robando todo el mazo:")
        while (len(self.c.mazo)>0):
            print(ui.c.robarCarta(), end=' ')
        print()
        
        
        
        
        
ui = UI_pront()
ui.printTablero()
ui.printMazo()
ui.robarTodoElMazo()
ui.printMazo()

    