# -*- coding: utf-8 -*-

from Controller import Controller
from BotTonto import BotTonto

import Constantes as const


class UI_pront:
    def __init__(self):
        self.c = Controller()
        self.win = 0
        self.bot1 = BotTonto("Bot 1")
        self.bot2 = BotTonto("Bot 2")
        self.__jugarPartida()
        
    def __jugarPartida(self):
        contadorRondas = 1
        while (self.win == 0):
            self.__turno(contadorRondas)
            self.win = self.c.finalizarTurno()
            if(self.win != 0):
                print("Ha ganado el jugador: "+str(self.win))
            contadorRondas = contadorRondas + 1
            
    def __turno(self, contadorRondas):
        self.c.initRonda()
        print("Inicio de ronda "+str(contadorRondas))
        self.c.printTableroCompleto()
        
        for i in range(const.N_ACCIONES):
            print("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.bot1, self.bot2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.bot2, self.bot1)
        
        self.c.printTableroCompleto()
        print("Fin de ronda " +str(contadorRondas))
            


        
    def __accion(self, jugador1, jugador2, botSeleccionadoComo1, botSeleccionadoComo2):
        self.c.jugadorRobaCarta(jugador1)
        tablero = self.c.getVistaTablero(jugador1)
        accion = botSeleccionadoComo1.decidirAccion(tablero)
        self.c.realizarAccion(jugador1, accion)
        
        if(self.c.hayAccionPendiente()):
            tablero = self.c.getVistaTablero(jugador2)
            accionDeSeleccion = botSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            self.c.realizarAccion(jugador2, accionDeSeleccion)

ui = UI_pront()
