# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.TableroController import TableroController
from controller.BotTonto import BotTonto
from controller.JugadorController import JugadorController

import controller.Constantes as const


class PartidaController:
    def __init__(self):
        self.c = TableroController()
        self.win = 0
        self.j1 = BotTonto("Bot 1")
        self.j2 = JugadorController()
        
    def start(self):
        contadorRondas = 1
        while (self.win == 0):
            self.__turno(contadorRondas)
            self.win = self.c.finalizarTurno()
            if(self.win == 1):
                print("Ha ganado el "+str(self.j1.yo))
            elif(self.win == 2):
                print("Ha ganado el "+str(self.j2.yo))
            else:
                self.j1, self.j2 = self.j2, self.j1
            contadorRondas = contadorRondas + 1
            
    def __turno(self, contadorRondas):
        self.c.initRonda()

        self.c.printTableroCompleto()
        
        for i in range(const.N_ACCIONES):
            print("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.j1, self.j2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.j2, self.j1)
              


        
    def __accion(self, jugador1, jugador2, botSeleccionadoComo1, botSeleccionadoComo2):
        self.c.jugadorRobaCarta(jugador1)
        tablero = self.c.getVistaTablero(jugador1)
        accion = botSeleccionadoComo1.decidirAccion(tablero)
        self.c.realizarAccion(jugador1, accion)
        
        if(self.c.hayAccionPendiente()):
            tablero = self.c.getVistaTablero(jugador2)
            accionDeSeleccion = botSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            self.c.realizarAccion(jugador2, accionDeSeleccion)

if __name__ == "__main__":
    prompt = UI_prompt()
    prompt.start()