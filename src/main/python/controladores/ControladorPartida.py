# -*- coding: utf-8 -*-
import logging

from main.python.controladores.ControladorTablero import ControladorTablero
from main.python.controladores.ControladorBot import ControladorBot
from main.python.controladores.ControladorJugador import ControladorJugador
from main.python.controladores.ControladorRedNeuronal import ControladorRedNeuronal
from main.python.interfaz.Popup_Tkinter import sendMensaje


import main.python.parametrizacion.ParametrosTablero as const
import main.python.parametrizacion.ParametrosMenu as menu
import main.python.parametrizacion.ParametrosDatos as data


class ControladorPartida:
    def __init__(self):
        self.tablero = ControladorTablero()
        self.win = 0
        
    def run(self):
        self.__initJugadores()

        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.winner = False
            self.accionesj1 = ''
            self.accionesj2 = ''
            self.tablerosj1 = ''
            self.tablerosj2 = ''
        
        try:
            self.__start()
        except:
            try:
                self.j1.finish()
                self.j2.finish()
                logging.error("Ha habido un error en el turno")
                sendMensaje("Se ha producido un error")
            except:
                logging.error("Ha habido un error en la interfaz o se ha cerrado la ventana")
            
    def __initJugadores(self):
        #Elegir opciones para generar datos
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            #Bot tonto en caso de ser facil
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.j1 = ControladorBot("Bot tonto 1", const.JUGADOR1)
                self.j2 = ControladorBot("Bot tonto 2", const.JUGADOR2)
            #Neural Network en caso de ser dificil
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.j1 = ControladorRedNeuronal("Neuronal Network 1", const.JUGADOR1)
                self.j2 = ControladorRedNeuronal("Neuronal Network 2", const.JUGADOR2)
                
        if(menu.MODO == menu.MODO_JUGAR):
            #El jugador 1 siempre sera un jugador
            self.j1 = ControladorJugador("Jugador", const.JUGADOR1)
            #Elegir al jugador 2 dependiendo de la dificultad
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.j2 = ControladorBot("Bot tonto", const.JUGADOR2)
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.j2 = ControladorRedNeuronal("Neuronal Network", const.JUGADOR2)
                
    def __start(self):
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.winner = False
            self.accionesj1 = ''
            self.accionesj2 = ''
            self.tablerosj1 = ''
            self.tablerosj2 = ''
        contadorRondas = 1
        while (self.win == 0):
            self.__ronda(contadorRondas)
            self.win = self.tablero.finalizarTurno()
            
            if(self.win == 1):
                self.winner = self.j1
            elif(self.win == 2):
                self.winner = self.j2
            else:
                self.j1, self.j2 = self.j2, self.j1
            contadorRondas = contadorRondas + 1
            
        self.j1.finish()
        self.j2.finish()
        
        logging.info("Ha ganado: "+str(self.winner.miNombre))
        
        if(menu.MODO == menu.MODO_JUGAR):
            if(self.winner.miNumero == const.JUGADOR1):
                sendMensaje("Has ganado :)")
            else:
                sendMensaje("Has perdido :(")
        
    def __ronda(self, contadorRondas):
        self.tablero.initRonda()
        logging.info("Inicio de la ronda "+str(contadorRondas))
        
        for i in range(const.N_ACCIONES):
            logging.info("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.j1, self.j2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.j2, self.j1)
            
    def __accion(self, numeroJugador1, numeroJugador2, jugadorSeleccionadoComo1, jugadorSeleccionadoComo2):
        self.tablero.jugadorRobaCarta(numeroJugador1)
        tablero = self.tablero.getVistaTablero(numeroJugador1)
        accion = jugadorSeleccionadoComo1.decidirAccion(tablero)
        self.__guardarAccion(tablero, accion, jugadorSeleccionadoComo1)
        self.tablero.realizarAccion(numeroJugador1, accion)
        
        if(self.tablero.hayAccionPendiente()):
            tablero = self.tablero.getVistaTablero(numeroJugador2)
            accionDeSeleccion = jugadorSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            self.__guardarAccion(tablero, accionDeSeleccion, jugadorSeleccionadoComo2)
            self.tablero.realizarAccion(numeroJugador2, accionDeSeleccion)
            
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
            else:
                self.tablerosj2 = self.tablerosj2 + linea1 + "\n"
                self.accionesj2 = self.accionesj2 + linea2 + "\n"
