# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import *

import controller.Constantes as const

class GUI_Tkinter:
    def __init__(self):
        self.window = Tk()
        self.printTabla()
        self.printAceptar()
        self.start()
        return
    
    def printTabla(self):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                text = str(f)+","+str(c)
                ButtonToAdd = Button(self.window, text = " ", state=DISABLED)
                ButtonToAdd.grid(row=f, column=c)
            
        
    def printAceptar(self):
        ButtonToAdd = Button(self.window, text = "Aceptar", command = self.pressAceptar)
        ButtonToAdd.grid(row=const.NFILA-1, column=const.NCOLUMNA+1)
    
    def start(self):
        self.window.mainloop()
        
    def pressAceptar(self):
        self.window.quit()
        return
    
    def cerrar(self):
        self.window.destroy()
        
        
        
if __name__ == "__main__":
    tkinter = GUI_Tkinter()
