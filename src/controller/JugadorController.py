# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.BotTonto import BotTonto


LOG = False

class JugadorController:
    def __init__(self):
        self.bot = BotTonto("Jugador automatico")
        self.yo = "Jugador automatico"
        
        
    def decidirAccion(self, tablero):
        return self.bot.decidirAccion(tablero)
    
    def decidirAccionDeSeleccion(self, tablero):
        return self.bot.decidirAccionDeSeleccion(tablero)
