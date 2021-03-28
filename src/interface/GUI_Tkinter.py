# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import *

import controller.Constantes as const

class GUI_Tkinter:
    def __init__(self):
        self.window = Tk()
        self.printTable()
        self.start()
        return
    
    def printTable(self):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                text = str(f)+","+str(c)
                ButtonToAdd = Button(self.window, text = text)
                ButtonToAdd.grid(row=f, column=c)
            
        
        return
    
    def start(self):
        self.window.mainloop()
        
        
        
if __name__ == "__main__":
    tkinter = GUI_Tkinter()
