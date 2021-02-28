# -*- coding: utf-8 -*-

from Controller import Controller
from BotTonto import BotTonto

import Constantes as const


class UI_pront:
    def __init__(self):
        self.c = Controller()
        self.win = False
        self.bot1 = BotTonto("Bot 1")
        self.bot2 = BotTonto("Bot 2")
        while (self.win == False):
            self.__turno()
            
    def __turno(self):
        self.c.initRonda()
        
        for i in range(const.N_ACCIONES):
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.bot1, self.bot2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.bot2, self.bot1)
            
        self.win = self.c.hacerRecuento()
        
    def __accion(self, jugador1, jugador2, bot1, bot2):
        tablero = self.c.getVistaTablero(jugador1)
        accion = bot1.decidirAccion(tablero)
            
        #self.c.realizarAccion(jugador1, accion)
        
        #if(accion[const.ACCION_SIMPLE] == 1):
            #tablero = self.c.getVistaTablero(jugador2)
            #accion = bot2.decidirAccion(tablero)
            
            #self.c.realizarAccion(jugador2, accion)
        
        
ui = UI_pront()