# -*- coding: utf-8 -*-

from Controller import Controller
from BotTonto import BotTonto

JUGADOR1 = 0
JUGADOR2 = 1
N_ACCIONES = 4

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
        
        for i in range(N_ACCIONES):
            tablero = self.c.getTablero(JUGADOR1)
            self.bot1.realizarAccion(tablero)
            tablero = self.c.getTablero(JUGADOR2)
            self.bot2.realizarAccion(tablero)
        
        self.win = self.c.hacerRecuento()
        
ui = UI_pront()