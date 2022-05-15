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

'''
Clase controladora de la partida, se encarga de los turnos y las rondas además 
de guardar las acciones que han llevado a cabo los jugadores
'''
class ControladorPartida:
    '''
    Metodo constructor de la clase ControladorPartida, se definen todos los 
    atributos privados de la misma.
    '''
    def __init__(self):
        '''Atributo controladorTablero: instancia del controlador del tablero
        en el que se guarda el estado del tablero y se ejecutan las acciones'''
        self.__controladorTablero = ControladorTablero()
        '''Atributo accionesJ1: string en el que se guardan las acciones que
        ha ejecutado el jugador 1 para su futuro guardado'''
        self.__accionesJ1 = ''
        '''Atributo accionesJ2: string en el que se guardan las acciones que
        ha ejecutado el jugador 2 para su futuro guardado'''
        self.__accionesJ2 = ''
        '''Atributo tableroJ1: string en el que se guardan los tableros que le 
        llegaron la jugador 1 y sobre los cuales formo la accion 
        correspondiente'''
        self.__tableroJ1 = ''
        '''Atributo tableroJ2: string en el que se guardan los tableros que le 
        llegaron la jugador 2 y sobre los cuales formo la accion 
        correspondiente'''
        self.__tableroJ2 = ''
        '''Atributo winnnerNumero: guarda el numero del ganador al final de
        cada ronda para poder saber si se ha terminado la partida'''
        self.__winnnerNumero = 0
        '''Atributo winner: copia de la instancia del jugador que ha ganado 
        la partida'''
        self.__winner = None
        '''Atributo jugador1: instancia del jugador correspondiente al orden 1'''
        self.__jugador1 = None
        '''Atributo jugador2: instancia del jugador correspondiente al orden 2'''
        self.__jugador2 = None
        '''Atributo jugador1Inicio: instancia del jugador copia de jugador 1, 
        pero que no cambia a lo largo de la partida dependiendo del turno, 
        se usa para declarar el ganador'''
        self.__jugador1Inicio = None
        '''Atributo jugador2Inicio: instancia del jugador copia de jugador 2, 
        pero que no cambia a lo largo de la partida dependiendo del turno, 
        se usa para declarar el ganador'''
        self.__jugador2Inicio = None
        
    '''
    Metodo ejecutor de la clase ControladorPartida, inicializa los jugadores y
    ejecuta el metodo __start con una captura de posibles errores que se 
    mostraran en un popup
    '''
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
                
    '''
    Metodo que instancia los atributos de jugador1 y jugador2 dependiendo del 
    modo y nivel seleccionados en la parametrizacion 
    '''       
    def __initJugadores(self):
        #Elegir opciones para generar datos
        if(menu.MODO == menu.MODO_GENERAR_DATOS):
            #Bot tonto en caso de ser facil
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.__jugador1 = ControladorBot("Bot 1", const.JUGADOR1)
                self.__jugador2 = ControladorBot("Bot 2", const.JUGADOR2)
            #Neural Network en caso de ser dificil
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.__jugador1 = ControladorRedNeuronal("Red neuronal 1", const.JUGADOR1)
                self.__jugador2 = ControladorRedNeuronal("Red neuronal 2", const.JUGADOR2)
                
        if(menu.MODO == menu.MODO_JUGAR):
            #El jugador 1 siempre sera un jugador
            self.__jugador1 = ControladorJugador("Jugador", const.JUGADOR1)
            #Elegir al jugador 2 dependiendo de la dificultad
            if(menu.MODO_DIFICULTAD == menu.MODO_FACIL):
                self.__jugador2 = ControladorBot("Bot aleatorio", const.JUGADOR2)
            if(menu.MODO_DIFICULTAD == menu.MODO_DIFICIL):
                self.__jugador2 = ControladorRedNeuronal("Neuronal Network", const.JUGADOR2)
                
        self.__jugador1Inicio = self.__jugador1
        self.__jugador2Inicio = self.__jugador2
        
    '''
    Metodo encargado de realizar el bucle de rondas hasta que en una de ellas
    haya un ganador
    ''' 
    def __start(self):
        contadorRondas = 1
        textoFinal = ''
        while (self.__winnnerNumero == const.GANADOR_EMPATE):
            self.__ronda(contadorRondas)
            self.__winnnerNumero = self.__controladorTablero.finalizarTurno()
            
            if(self.__winnnerNumero == const.GANADOR_1_POR_11_PUNTOS):
                self.__winner = self.__jugador1Inicio
                textoFinal = gui.TEXTO_POPUP_GANADO_JUGADOR_POR_11_PUNTOS
                
            elif(self.__winnnerNumero == const.GANADOR_1_POR_4_FAVORES):
                self.__winner = self.__jugador1Inicio
                textoFinal = gui.TEXTO_POPUP_GANADO_JUGADOR_POR_4_FAVORES
                
            elif(self.__winnnerNumero == const.GANADOR_2_POR_11_PUNTOS):
                self.__winner = self.__jugador2Inicio
                textoFinal = gui.TEXTO_POPUP_PERDIDO_JUGADOR_POR_11_PUNTOS
                
            elif(self.__winnnerNumero == const.GANADOR_2_POR_4_FAVORES):
                self.__winner = self.__jugador2Inicio
                textoFinal = gui.TEXTO_POPUP_PERDIDO_JUGADOR_POR_4_FAVORES
                
            else:
                self.__jugador1, self.__jugador2 = self.__jugador2, self.__jugador1
            contadorRondas = contadorRondas + 1
            
        self.__jugador1.finish()
        self.__jugador2.finish()
        
        logging.info("Ha ganado: "+str(self.__winner.getMiNombre()))
        
        if(menu.MODO == menu.MODO_JUGAR):
            newPopup = Popup_Tkinter()
            newPopup.sendMensaje(textoFinal)
                
    '''
    Metodo encargado de inicializar la ronda correspondiente y realizar el 
    bucle de las acciones de los jugadores
    '''
    def __ronda(self, contadorRondas):
        self.__controladorTablero.initRonda()
        logging.info("Inicio de la ronda "+str(contadorRondas))
        
        for i in range(const.N_ACCIONES):
            logging.info("Inicio de turno "+str(i))
            self.__accion(const.JUGADOR1, const.JUGADOR2, self.__jugador1, self.__jugador2)
            self.__accion(const.JUGADOR2, const.JUGADOR1, self.__jugador2, self.__jugador1)
            
    '''
    Metodo encargado de pedir a los jugadores que realicen una accion, si la 
    accion requiere de interaccion por parte del otro jugador tambien se le 
    pedira que haga la seleccion
    '''
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
            
    '''
    Metodo encargado de guardar en formato string la accion y el tablero dados
    en su correspondiente atributo de la clase
    '''
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
                
    '''
    Metodo get para el atributo de tipo string: accionesJ1
    '''
    def getAccionesJ1(self):
        return self.__accionesJ1
    
    '''
    Metodo get para el atributo de tipo string: accionesJ2
    '''
    def getAccionesJ2(self):
        return self.__accionesJ2
    
    '''
    Metodo get para el atributo de tipo string: tablerosJ1
    '''
    def getTablerosJ1(self):
        return self.__tableroJ1
    
    '''
    Metodo get para el atributo de tipo string: tablerosJ2
    '''
    def getTablerosJ2(self):
        return self.__tableroJ2
    
    '''
    Metodo get para el atributo winner que implementa una clase jugador
    '''
    def getWinner(self):
        return self.__winner
    
