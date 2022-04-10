# -*- coding: utf-8 -*-

import sys
sys.path.append('../../../')

from interface.GUI_Tkinter import GUI_Tkinter

class JugadorController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.GUI = GUI_Tkinter()
        
    def decidirAccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def __pedirAccion(self, tablero):
        self.GUI.printTabla(tablero)
        self.GUI.start()
        return self.GUI.obtenerAccion()
    
    def finish(self):
        self.GUI.cerrar()
