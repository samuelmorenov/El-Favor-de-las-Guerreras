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
            tablero1 = self.c.getVistaTablero(const.JUGADOR1)
            self.bot1.realizarAccion(tablero1)
            tablero2 = self.c.getVistaTablero(const.JUGADOR2)
            self.bot2.realizarAccion(tablero2)
        
        self.win = self.c.hacerRecuento()
        
ui = UI_pront()