# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Button, DISABLED, Tk

import controller.Constantes as const

class GUI_Tkinter:
    def __init__(self):
        self.__window = Tk()
        self.__printTablaInicial()
        self.__printAceptar()
        self.start()
        self.__pressAceptar()
        return
    
    def printTabla(self, tablero):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                ButtonToAdd = Button(self.__window, text = tablero[f][c], state=DISABLED)
                ButtonToAdd.grid(row=f, column=c)
    
    def __printTablaInicial(self):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                ButtonToAdd = Button(self.__window, text = " ", state=DISABLED)
                ButtonToAdd.grid(row=f, column=c)

    def __printAceptar(self):
        ButtonToAdd = Button(self.__window, text = "Aceptar", command = self.__pressAceptar)
        ButtonToAdd.grid(row=const.NFILA-1, column=const.NCOLUMNA+1)
    
    def start(self):
        self.__window.mainloop()
        
    def __pressAceptar(self):
        self.__window.quit()
        return
    
    def cerrar(self):
        self.__window.destroy()  
        
if __name__ == "__main__":
    tkinter = GUI_Tkinter()
