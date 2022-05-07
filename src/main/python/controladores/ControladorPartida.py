# -*- coding: utf-8 -*-
import logging

from main.python.controladores.ControladorTablero import ControladorTablero
from main.python.controladores.ControladorBot import ControladorBot
from main.python.controladores.ControladorJugador import ControladorJugador
from main.python.controladores.ControladorRedNeuronal import ControladorRedNeuronal
from main.python.interfaz.Popup_Tkinter import Popup_Tkinter


import main.python.parametrizacion.ParametrosTablero as const
import main.python.parametrizacion.ParametrosMenu as menu
import main.python.parametrizacion.ParametrosDatos as data
import main.python.parametrizacion.ParametrosGUI as gui


class ControladorPartida:
    def __init__(self):
        self.__controladorTablero = ControladorTablero()
        self.__winnnerNumero = 0
        self.__accionesJ1 = ''
        self.__accionesJ2 = ''
        self.__tableroJ1 = ''
        self.__tableroJ2 = ''
        self.__winner = None
        self.__jugador1 = None
        self.__jugador2 = None
        
    def run(self):
        self.__initJugadores()
        
        try:
            self.__start()
        except:
            newPopup = Popup_Tkinter()
            try:
                self.__jugador1.finish()
                self.__jugador2.finish()
                logging.error("Ha habido un error en el turno")
                newPopup.sendMensaje(gui.TEXTO_POPUP_ERROR)
            except:
                logging.error("Se ha cerrado la ventana de forma inesperada")
                newPopup.sendMensaje(gui.TEXTO_POPUP_CIERRE)
                
    def getAccionesJ1(self):
        return self.__accionesJ1
    
    def getAccionesJ2(self):
        return self.__accionesJ2
    
    def getTablerosJ1(self):
        return self.__tableroJ1
    
    def getTablerosJ2(self):
        return self.__tableroJ2
    
    def getWinner(self):
        return self.__winner
            
    def __initJugadores(self):
        #Elegir opciones para generar datos
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            #Bot tonto en caso de ser facil
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.__jugador1 = ControladorBot("Bot tonto 1", const.JUGADOR1)
                self.__jugador2 = ControladorBot("Bot tonto 2", const.JUGADOR2)
            #Neural Network en caso de ser dificil
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.__jugador1 = ControladorRedNeuronal("Neuronal Network 1", const.JUGADOR1)
                self.__jugador2 = ControladorRedNeuronal("Neuronal Network 2", const.JUGADOR2)
                
        if(menu.MODO == menu.MODO_JUGAR):
            #El jugador 1 siempre sera un jugador
            self.__jugador1 = ControladorJugador("Jugador", const.JUGADOR1)
            #Elegir al jugador 2 dependiendo de la dificultad
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.__jugador2 = ControladorBot("Bot tonto", const.JUGADOR2)
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.__jugador2 = ControladorRedNeuronal("Neuronal Network", const.JUGADOR2)
                
    def __start(self):
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.__winner = None
            self.__accionesJ1 = ''
            self.__accionesJ2 = ''
            self.__tableroJ1 = ''
            self.__tableroJ2 = ''
        contadorRondas = 1
        while (self.__winnnerNumero == 0):
            self.__ronda(contadorRondas)
            self.__winnnerNumero = self.__controladorTablero.finalizarTurno()
            
            if(self.__winnnerNumero == 1):
                self.__winner = self.__jugador1
            elif(self.__winnnerNumero == 2):
                self.__winner = self.__jugador2
            else:
                self.__jugador1, self.__jugador2 = self.__jugador2, self.__jugador1
            contadorRondas = contadorRondas + 1
            
        self.__jugador1.finish()
        self.__jugador2.finish()
        
        logging.info("Ha ganado: "+str(self.__winner.getMiNombre()))
        
        if(menu.MODO == menu.MODO_JUGAR):
            newPopup = Popup_Tkinter()
            if(self.__winner.getMiNumero() == const.JUGADOR1):
                newPopup.sendMensaje(gui.TEXTO_POPUP_GANADO)
            else:
                newPopup.sendMensaje(gui.TEXTO_POPUP_PERDIDO)
        
    def __ronda(self, contadorRondas):
        self.__controladorTablero.initRonda()
        logging.info("Inicio de la ronda "+str(contadorRondas))
        
        for i in range(const.N_ACCIONES):
            logging.info("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.__jugador1, self.__jugador2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.__jugador2, self.__jugador1)
            
    def __accion(self, numeroJugador1, numeroJugador2, jugadorSeleccionadoComo1, jugadorSeleccionadoComo2):
        self.__controladorTablero.jugadorRobaCarta(numeroJugador1)
        tablero = self.__controladorTablero.getVistaTablero(numeroJugador1)
        accion = jugadorSeleccionadoComo1.decidirAccion(tablero)
        self.__guardarAccion(tablero, accion, jugadorSeleccionadoComo1)
        self.__controladorTablero.realizarAccion(numeroJugador1, accion)
        
        if(self.__controladorTablero.hayAccionPendiente()):
            tablero = self.__controladorTablero.getVistaTablero(numeroJugador2)
            accionDeSeleccion = jugadorSeleccionadoComo2.decidirAccionDeSeleccion(tablero)
            self.__guardarAccion(tablero, accionDeSeleccion, jugadorSeleccionadoComo2)
            self.__controladorTablero.realizarAccion(numeroJugador2, accionDeSeleccion)
            
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
                    
                
            if(jugador.getMiNumero()) == const.JUGADOR1:
                self.__tableroJ1 = self.__tableroJ1 + linea1 + "\n"
                self.__accionesJ1 = self.__accionesJ1 + linea2 + "\n"
            else:
                self.__tableroJ2 = self.__tableroJ2 + linea1 + "\n"
                self.__accionesJ2 = self.__accionesJ2 + linea2 + "\n"
