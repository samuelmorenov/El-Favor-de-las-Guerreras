# -*- coding: utf-8 -*-

import logging
import sys
sys.path.append('../')

from controller.TableroController import TableroController
from controller.BotTonto import BotTonto
from controller.JugadorController import JugadorController
from controller.NeuralNetworkController import NeuralNetworkController
from interface.Popup_Tkinter import sendMensaje


import parameterization.ParametrosTablero as const
import parameterization.ParametrosMenu as menu
import parameterization.ParametrosDatos as data


class PartidaController:
    def __init__(self):
        self.c = TableroController()
        self.win = 0
        
        self.__initJugadores()

        #Si esta en modo generacion de datos hay que guardar esos datos
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            self.winner = False
            self.accionesj1 = ''
            self.accionesj2 = ''
            self.tablerosj1 = ''
            self.tablerosj2 = ''
            #self.tablerosYAccionesj1 = ''
            #self.tablerosYAccionesj2 = ''
        
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
                self.j1 = BotTonto("Bot tonto 1", const.JUGADOR1)
                self.j2 = BotTonto("Bot tonto 2", const.JUGADOR2)
            #Neural Network en caso de ser dificil
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.j1 = NeuralNetworkController("Neuronal Network 1", const.JUGADOR1)
                self.j2 = NeuralNetworkController("Neuronal Network 2", const.JUGADOR2)
                
        if(menu.MODO == menu.MODO_JUGAR):
            #El jugador 1 siempre sera un jugador
            self.j1 = JugadorController("Jugador", const.JUGADOR1)
            #Elegir al jugador 2 dependiendo de la dificultad
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.j2 = BotTonto("Bot tonto", const.JUGADOR2)
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.j2 = NeuralNetworkController("Neuronal Network", const.JUGADOR2)
                
    def __start(self):
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
        
        logging.info("Ha ganado: "+str(self.winner.miNombre))
        
        if(menu.MODO == menu.MODO_JUGAR):
            if(self.winner.miNumero == const.JUGADOR1):
                sendMensaje("Has ganado :)")
            else:
                sendMensaje("Has perdido :(")
        
    def __turno(self, contadorRondas):
        self.c.initRonda()
        
        for i in range(const.N_ACCIONES):
            logging.info("Inicio de turno "+str(i))
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
