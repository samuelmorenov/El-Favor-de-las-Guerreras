# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.BotTonto import BotTonto
from interface.GUI_Tkinter import GUI_Tkinter


LOG = False

class JugadorController:
    def __init__(self):
        self.bot = BotTonto("Jugador automatico")
        self.yo = "Jugador automatico"
        self.GUI = GUI_Tkinter()
        
        
    def decidirAccion(self, tablero):
        #accion = self.bot.decidirAccion(tablero)
        

        
        self.GUI.printTabla(tablero)
        self.GUI.start()
        
        accion = self.GUI.obtenerAccion()
        
        #self.GUI.getAccion()
        
        return accion
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.bot.decidirAccionDeSeleccion(tablero)
    
    def finish(self):
        self.GUI.cerrar()
