# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from controller.TableroController import TableroController
from controller.BotTonto import BotTonto
from controller.JugadorController import JugadorController

import controller.Constantes as const


class PartidaController:
    def __init__(self, modo):
        self.c = TableroController()
        self.win = 0
        self.winner = False
        if(const.MODO == const.MODO_GENERAR_DATOS):
            self.j1 = BotTonto("Bot tonto 1", const.JUGADOR1)
        if(const.MODO == const.MODO_JUGAR):
            self.j1 = JugadorController("Jugador", const.JUGADOR1)
        self.j2 = BotTonto("Bot tonto 2", const.JUGADOR2)
        self.accionesj1 = ''
        self.accionesj2 = ''
        
    def start(self):
        self.accionesj1 = ''
        self.accionesj2 = ''
        contadorRondas = 1
        while (self.win == 0):
            self.__turno(contadorRondas)
            self.win = self.c.finalizarTurno()
            if(self.win == 1):
                self.__guardarGanador(self.j1)
            elif(self.win == 2):
                self.__guardarGanador(self.j2)
            else:
                self.j1, self.j2 = self.j2, self.j1
            contadorRondas = contadorRondas + 1
            
        self.j1.finish()
        self.j2.finish()
        
    def __turno(self, contadorRondas):
        self.c.initRonda()

        self.c.printTableroCompleto()
        
        for i in range(const.N_ACCIONES):
            if(const.PRINT_TRACE):
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
            self.__guardarAccion(tablero, accion, botSeleccionadoComo2)
            self.c.realizarAccion(jugador2, accionDeSeleccion)
            
    def __guardarAccion(self, tablero, accion, jugador):
        linea = ''
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                casilla = tablero[f][c]
                casilla = str(casilla)
                linea = linea + casilla
            if(f != const.NFILA-1):
                linea = linea + const.SEPARADOR_FILAS
                
        linea = linea + const.SEPARADOR_ENTRADASALIDA
        for c2 in range(const.NCOLUMNA - 2):
            casilla = accion[c2]
            casilla = str(casilla)
            linea = linea + casilla
            
        if(jugador.miNumero) == const.JUGADOR1:
            self.accionesj1 = self.accionesj1 + linea + "\n"
        else:
            self.accionesj2 = self.accionesj2 + linea + "\n"
            
    def __guardarGanador(self, jugador):
        if(const.PRINT_TRACE):
            print("Ha ganado el "+str(jugador.miNombre))
        jugadas = ''
        if(jugador.miNumero == const.JUGADOR1):
            jugadas = self.accionesj1
            self.winner = const.JUGADOR1
        else:
            jugadas = self.accionesj2
            self.winner = const.JUGADOR2
            
        self.__guardarEnArchivo(jugadas)
        
    def __guardarEnArchivo(self, jugadas):
        path = "./../data/jugadasGanadoras.csv"
        with open(path, 'a') as f:
            f.write(jugadas)
