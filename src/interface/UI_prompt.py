# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.TableroController import TableroController
from controller.BotTonto import BotTonto

import controller.Constantes as const


class UI_prompt:
    def __init__(self):
        self.c = TableroController()
        self.win = 0
        self.bot1 = BotTonto("Bot 1")
        self.bot2 = BotTonto("Bot 2")
        
    def start(self):
        contadorRondas = 1
        while (self.win == 0):
            self.__turno(contadorRondas)
            self.win = self.c.finalizarTurno()
            if(self.win == 1):
                print("Ha ganado el "+str(self.bot1.yo))
            elif(self.win == 2):
                print("Ha ganado el "+str(self.bot2.yo))
            else:
                self.bot1, self.bot2 = self.bot2, self.bot1
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
