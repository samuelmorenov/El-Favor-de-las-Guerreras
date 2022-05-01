# -*- coding: utf-8 -*-
import logging

from main.python.interface.GUI_Tkinter import GUI_Tkinter

class JugadorController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.GUI = GUI_Tkinter()
        
    def decidirAccion(self, tablero):
        logging.info(self.miNombre+" : Este es el tablero que me llega:\n"+str(tablero))
        salida = self.__pedirAccion(tablero)
        logging.info(self.miNombre+" : Esta es la accion completa que realizo: "+str(salida))
        logging.info(self.miNombre+" : ___________________________________") #Separador
        return salida
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    def __pedirAccion(self, tablero):
        self.GUI.printTabla(tablero)
        self.GUI.start()
        return self.GUI.obtenerAccion()
    
    def finish(self):
        self.GUI.cerrar()
