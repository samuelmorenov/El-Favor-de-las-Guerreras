# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.TableroController import TableroController
from controller.BotTonto import BotTonto
from controller.JugadorController import JugadorController

import parameterization.ParametrosTablero as const
import parameterization.ParametrosMenu as menu
import parameterization.ParametrosDatos as data


class PartidaController:
    def __init__(self, modo):
        self.c = TableroController()
        self.win = 0
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.j1 = BotTonto("Bot tonto 1", const.JUGADOR1)
        if(menu.MODO == menu.MODO_JUGAR):
            self.j1 = JugadorController("Jugador", const.JUGADOR1)
        self.j2 = BotTonto("Bot tonto 2", const.JUGADOR2)
        
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.winner = False
            self.accionesj1 = ''
            self.accionesj2 = ''
            self.tablerosj1 = ''
            self.tablerosj2 = ''
            #self.tablerosYAccionesj1 = ''
            #self.tablerosYAccionesj2 = ''
        
    def start(self):
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.winner = False
            self.accionesj1 = ''
            self.accionesj2 = ''
            self.tablerosj1 = ''
            self.tablerosj2 = ''
            #self.tablerosYAccionesj1 = ''
            #self.tablerosYAccionesj2 = ''
        contadorRondas = 1
        while (self.win == 0):
            self.__turno(contadorRondas)
            self.win = self.c.finalizarTurno()
            
            if(self.win == 1):
                self.winner = self.j1
            elif(self.win == 2):
                self.winner = self.j2
            else:
                self.j1, self.j2 = self.j2, self.j1
            contadorRondas = contadorRondas + 1
            
        self.j1.finish()
        self.j2.finish()
        
    def __turno(self, contadorRondas):
        self.c.initRonda()

        self.c.printTableroCompleto()
        
        for i in range(const.N_ACCIONES):
            if(menu.PRINT_TRACE):
                print("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.j1, self.j2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.j2, self.j1)
            
    def __accion(self, jugador1, jugador2, botSeleccionadoComo1, botSeleccionadoComo2):
        self.c.jugadorRobaCarta(jugador1)
        tablero = self.c.getVistaTablero(jugador1)
        accion = botSeleccionadoComo1.decidirAccion(tablero)
        self.__guardarAccion(tablero, accion, botSeleccionadoComo1)
        self.c.realizarAccion(jugador1, accion)
        
        if(self.c.hayAccionPendiente()):
            tablero = self.c.getVistaTablero(jugador2)
            accionDeSeleccion = botSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            self.__guardarAccion(tablero, accionDeSeleccion, botSeleccionadoComo2)
            self.c.realizarAccion(jugador2, accionDeSeleccion)
            
    def __guardarAccion(self, tablero, accion, jugador):
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            linea1 = ''
            for f in range(const.NFILA):
                for c in range(const.NCOLUMNA):
                    casilla = tablero[f][c]
                    casilla = str(casilla)
                    linea1 = linea1 + casilla
                    if(f*c != (const.NFILA-1)*(const.NCOLUMNA-1)):
                        linea1 = linea1 + data.SEPARADOR
                    
                    
            linea2 = ''
            camposAccionCorregido = const.NCOLUMNA - 2
            for c2 in range(camposAccionCorregido):
                casilla = accion[c2]
                casilla = str(casilla)
                linea2 = linea2 + casilla
                if(c2 != camposAccionCorregido-1):
                    linea2 = linea2 + data.SEPARADOR
                    
                
            if(jugador.miNumero) == const.JUGADOR1:
                self.tablerosj1 = self.tablerosj1 + linea1 + "\n"
                self.accionesj1 = self.accionesj1 + linea2 + "\n"
                #self.tablerosYAccionesj1 = self.tablerosYAccionesj1 + linea1 + data.SEPARADOR + linea2 + "\n"
            else:
                self.tablerosj2 = self.tablerosj2 + linea1 + "\n"
                self.accionesj2 = self.accionesj2 + linea2 + "\n"
                #self.tablerosYAccionesj2 = self.tablerosYAccionesj2 + linea1 + data.SEPARADOR + linea2 + "\n"
