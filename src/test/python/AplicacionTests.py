# -*- coding: utf-8 -*-
import unittest
import logging
import sys, os

base = os.path.dirname(__file__)
sys.path.insert(0, os.path.normpath(base+"/../.."))

from main.python.controladores.ControladorBot import ControladorBot
from main.python.controladores.ControladorRedNeuronal import ControladorRedNeuronal
from main.python.controladores.ControladorTablero import ControladorTablero
from auxiliares.ComprobarAcciones import ComprobarAcciones
from auxiliares.ComprobarTablero import ComprobarTablero

import main.python.parametrizacion.ParametrosTablero as const
import main.python.LoggerConfig as loggerConfig

acciones = ComprobarAcciones()
tableros = ComprobarTablero()

accionesDisponiblesTodas            = [0,0,0,0,0,0,0]
accionesDisponiblesSecreto          = [0,2,3,1,1,0,0]
accionesDisponiblesRenuncia         = [2,0,0,1,1,0,0]
accionesDisponiblesRegalo           = [2,3,4,0,1,0,0]
accionesDisponiblesCompeticion      = [2,3,4,1,0,0,0]
accionesDisponiblesNinguna          = [2,3,4,1,1,1,0]

mano7CartasDistintas = [1,2,3,4,5,6,7]
mano4Iguales = [7,7,7,7,0,0,0]
mano3Iguales = [7,7,7,0,0,0,0]
mano2Iguales = [7,7,0,0,0,0,0]
mano1Iguales = [7,0,0,0,0,0,0]
manoVacia = [0,0,0,0,0,0,0]

cartasAccionSeleccionRegalo0Iguales = [5,1,2,3,0,0,0]
cartasAccionSeleccionRegalo2Iguales = [5,1,1,2,0,0,0]
cartasAccionSeleccionRegalo3Iguales = [5,4,4,4,0,0,0]

cartasAccionSeleccionCompeticionIguales = [6,7,7,7,7,0,0]
cartasAccionSeleccionCompeticionDistintas = [6,7,7,6,6,0,0]

class Test(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.bot = ControladorBot("Bot de testing", 0)
        self.bot2 = ControladorBot("Bot de testing jugador 2", 0)
        self.redNeuronal = ControladorRedNeuronal("Red neuronal de testing", 0)
        self.tablero = ControladorTablero()
        
    #-----------------------Bot Seleccionar accion-----------------------
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    7 cartas distintas a elegir
    def test_caso_1(self):
        logging.info("Test del caso 1")
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_2(self):
        logging.info("Test del caso 2")
        acciones.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_3(self):
        logging.info("Test del caso 3")
        acciones.accionException(self.bot, manoVacia, accionesDisponiblesTodas)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_4(self):
        logging.info("Test del caso 4")
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_5(self):
        logging.info("Test del caso 5")
        acciones.accionCorrecta(self.bot, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_6(self):
        logging.info("Test del caso 6")
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_7(self):
        logging.info("Test del caso 7")
        acciones.accionCorrecta(self.bot, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_8(self):
        logging.info("Test del caso 8")
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_9(self):
        logging.info("Test del caso 9")
        acciones.accionCorrecta(self.bot, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_10(self):
        logging.info("Test del caso 10")
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_11(self):
        logging.info("Test del caso 11")
        acciones.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_12(self):
        logging.info("Test del caso 12")
        acciones.accionException(self.bot, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Bot Seleccionar accion de seleccion-----------------
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_13(self):
        logging.info("Test del caso 13")
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_14(self):
        logging.info("Test del caso 14")
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_15(self):
        logging.info("Test del caso 15")
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_16(self):
        logging.info("Test del caso 16")
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_17(self):
        logging.info("Test del caso 17")
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionDistintas)
        
    #-----------------------Red neuronal Seleccionar accion-----------------------
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    7 cartas distintas a elegir
    def test_caso_18(self):
        logging.info("Test del caso 18")
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_19(self):
        logging.info("Test del caso 19")
        acciones.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_20(self):
        logging.info("Test del caso 20")
        acciones.accionException(self.redNeuronal, manoVacia, accionesDisponiblesTodas)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_21(self):
        logging.info("Test del caso 21")
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_22(self):
        logging.info("Test del caso 22")
        acciones.accionCorrecta(self.redNeuronal, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_23(self):
        logging.info("Test del caso 23")
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_24(self):
        logging.info("Test del caso 24")
        acciones.accionCorrecta(self.redNeuronal, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_25(self):
        logging.info("Test del caso 25")
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_26(self):
        logging.info("Test del caso 26")
        acciones.accionCorrecta(self.redNeuronal, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_27(self):
        logging.info("Test del caso 27")
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_28(self):
        logging.info("Test del caso 28")
        acciones.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_29(self):
        logging.info("Test del caso 29")
        acciones.accionException(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Red neuronal Seleccionar accion de seleccion-----------------
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_30(self):
        logging.info("Test del caso 30")
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_31(self):
        logging.info("Test del caso 31")
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_32(self):
        logging.info("Test del caso 32")
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_33(self):
        logging.info("Test del caso 33")
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_34(self):
        logging.info("Test del caso 34")
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionDistintas)
        
    #-----------------Tablero-----------------
    #Prueba del tablero, creacion del tablero:
    def test_caso_35(self):
        logging.info("Test del caso 35")
        self.tablero = ControladorTablero()
        
        tableroAux1 = self.tablero.getVistaTablero(const.JUGADOR1)
        tableroAux2 = self.tablero.getVistaTablero(const.JUGADOR2)
        
        tableros.tableroCreacion(tableroAux1)
        tableros.tableroCreacion(tableroAux2)
        
    #Prueba del tablero, iniciar ronda y vista del tablero:
    #   Primera ronda
    #   Todo vacío excepto las manos de los jugadores
    #   Se ve la mano del jugador
    #   No se ve la mano del adversario
    #   Todo lo demas esta vacio
    def test_caso_36(self):
        logging.info("Test del caso 36")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        
        tableroAux1 = self.tablero.getVistaTablero(const.JUGADOR1)
        tableroAux2 = self.tablero.getVistaTablero(const.JUGADOR2)
        
        tableros.tableroInicioPrimeraRonda(tableroAux1)
        tableros.tableroInicioPrimeraRonda(tableroAux2)
        tableros.manoConNCartas(tableroAux1, const.N_CARTAS_INICIAL)
        tableros.manoConNCartas(tableroAux2, const.N_CARTAS_INICIAL)
        
    #Prueba del tablero, iniciar ronda y vista del tablero:
    #   No primera ronda
    #   Todo vacío excepto las manos de los jugadores y el favor
    def test_caso_37(self):
        logging.info("Test del caso 37")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(const.N_ACCIONES, self.tablero, self.bot, self.bot2)
        self.tablero.finalizarTurno()
        self.tablero.initRonda()
        
        tableroAux1 = self.tablero.getVistaTablero(const.JUGADOR1)
        tableroAux2 = self.tablero.getVistaTablero(const.JUGADOR2)
        
        tableros.tableroInicioSegundaRonda(tableroAux1)
        tableros.tableroInicioSegundaRonda(tableroAux2)
        tableros.manoConNCartas(tableroAux1, const.N_CARTAS_INICIAL)
        tableros.manoConNCartas(tableroAux2, const.N_CARTAS_INICIAL)
        
    #Prueba del tablero, vista del tablero:
    #   Mitad de la segunda ronda
    #   Se ve la mano del jugador
    #   No se ve la mano del adversario
    #   Hay acciones realizadas por ambos jugadores
    #   Se ven las armas en las guerreras
    #   Se ve el favor de las guerreras
    def test_caso_38(self):
        logging.info("Test del caso 38")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(const.N_ACCIONES, self.tablero, self.bot, self.bot2)
        self.tablero.finalizarTurno()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(int(const.N_ACCIONES/2), self.tablero, self.bot, self.bot2)
        
        tableroAux1 = self.tablero.getVistaTablero(const.JUGADOR1)
        tableroAux2 = self.tablero.getVistaTablero(const.JUGADOR2)
        
        tableros.tableroMitadSegundaRonda(tableroAux1)
        tableros.tableroMitadSegundaRonda(tableroAux2)
        
    #Prueba del tablero, vista del tablero:
    #   Fin de la segunda ronda
    #   Mano del jugador vacia
    #   No se ve la mano del adversario
    #   Se ven las cartas de las acciones del jugador
    #   Se ven las acciones del adbersario pero no las cartas
    #   Se ven las armas en las guerreras
    #   Se ve el favor de las guerreras
    def test_caso_39(self):
        logging.info("Test del caso 39")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(const.N_ACCIONES, self.tablero, self.bot, self.bot2)
        self.tablero.finalizarTurno()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(const.N_ACCIONES, self.tablero, self.bot, self.bot2)
        
        tableroAux1 = self.tablero.getVistaTablero(const.JUGADOR1)
        tableroAux2 = self.tablero.getVistaTablero(const.JUGADOR2)
        
        tableros.tableroFinSegundaRonda(tableroAux1)
        tableros.tableroFinSegundaRonda(tableroAux2)

        tableros.seVenLasCartasDeLasAcciones(tableroAux1[const.ACCIONES_USADAS_JUGADOR1])
        tableros.noSeVenLasCartasDeLasAcciones(tableroAux1[const.ACCIONES_USADAS_JUGADOR2])
        
        tableros.seVenLasCartasDeLasAcciones(tableroAux2[const.ACCIONES_USADAS_JUGADOR1])
        tableros.noSeVenLasCartasDeLasAcciones(tableroAux2[const.ACCIONES_USADAS_JUGADOR2])
        
    #Prueba del tablero, vista del tablero:
    #   Con accion pendiente de selección
    #   Es de tipo 3
    def test_caso_40(self):
        logging.info("Test del caso 40")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararAccionSeleccionJugador1(self.tablero, self.bot, self.bot2, const.TIPO_DECISION_REGALO)
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        
        tableros.accionSeleccionCorrecta(tableroAux[const.ACCION_PENDIENTE], const.TIPO_DECISION_REGALO)
        
    #Prueba del tablero, vista del tablero:
    #   Con accion pendiente de selección
    #   Es de tipo 4
    def test_caso_41(self):
        logging.info("Test del caso 41")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararAccionSeleccionJugador1(self.tablero, self.bot, self.bot2, const.TIPO_DECISION_COMPETICION)
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        
        tableros.accionSeleccionCorrecta(tableroAux[const.ACCION_PENDIENTE], const.TIPO_DECISION_COMPETICION)
        
    #Prueba del tablero, robar carta:
    #   Tiene la mano con un solo hueco
    def test_caso_42(self):
        logging.info("Test del caso 42")
        self.tablero = ControladorTablero()
        self.tablero.jugadorRobaCarta(const.JUGADOR1)
        
    #Prueba del tablero, robar carta:
    #   Tiene la mano llena
    def test_caso_43(self):
        logging.info("Test del caso 43")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero.jugadorRobaCarta(const.JUGADOR1)
        with self.assertRaises(Exception):
            self.tablero.jugadorRobaCarta(const.JUGADOR1)
        
    #Prueba del tablero, robar carta:
    #   El mazo esta vacio
    def test_caso_44(self):
        logging.info("Test del caso 44")
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararTableroJugador1(const.N_ACCIONES, self.tablero, self.bot, self.bot2)
        with self.assertRaises(Exception):
            self.tablero.jugadorRobaCarta(const.JUGADOR1)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo secreto
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_45(self):
        logging.info("Test del caso 45")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDisponibleYBienFormada(self.tablero, const.TIPO_SECRETO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo secreto
    #   El tipo de accion no esta disponible
    def test_caso_46(self):
        logging.info("Test del caso 46")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionNoDisponible(self.tablero, const.TIPO_SECRETO)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo secreto
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_47(self):
        logging.info("Test del caso 47")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionMalFormada(self.tablero, const.TIPO_SECRETO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo renuncia
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_48(self):
        logging.info("Test del caso 48")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDisponibleYBienFormada(self.tablero, const.TIPO_RENUNCIA)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo renuncia
    #   El tipo de accion no esta disponible
    def test_caso_49(self):
        logging.info("Test del caso 49")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionNoDisponible(self.tablero, const.TIPO_RENUNCIA)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo renuncia
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_50(self):
        logging.info("Test del caso 50")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionMalFormada(self.tablero, const.TIPO_RENUNCIA)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo regalo
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_51(self):
        logging.info("Test del caso 51")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDisponibleYBienFormada(self.tablero, const.TIPO_REGALO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo regalo
    #   El tipo de accion no esta disponible
    def test_caso_52(self):
        logging.info("Test del caso 52")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionNoDisponible(self.tablero, const.TIPO_REGALO)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo regalo
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_53(self):
        logging.info("Test del caso 53")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionMalFormada(self.tablero, const.TIPO_REGALO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo competicion
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_54(self):
        logging.info("Test del caso 54")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDisponibleYBienFormada(self.tablero, const.TIPO_COMPETICION)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo competicion
    #   El tipo de accion no esta disponible
    def test_caso_55(self):
        logging.info("Test del caso 55")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionNoDisponible(self.tablero, const.TIPO_COMPETICION)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo competicion
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_56(self):
        logging.info("Test del caso 56")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionMalFormada(self.tablero, const.TIPO_COMPETICION)
      
    #Prueba del tablero, realizar una accion:
    #   Tipo decision regalo
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_57(self):
        logging.info("Test del caso 57")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionDisponibleYBienFormada(self.tablero, const.TIPO_DECISION_REGALO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo decision regalo
    #   El tipo de accion no esta disponible
    def test_caso_58(self):
        logging.info("Test del caso 58")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionNoDisponible(self.tablero, const.TIPO_DECISION_REGALO)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo decision regalo
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_59(self):
        logging.info("Test del caso 59")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionMalFormada(self.tablero, const.TIPO_DECISION_REGALO)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo decision competicion
    #   El tipo de accion esta disponible
    #   La accion esta bien formada
    def test_caso_60(self):
        logging.info("Test del caso 60")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionDisponibleYBienFormada(self.tablero, const.TIPO_DECISION_COMPETICION)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo decision competicion
    #   El tipo de accion no esta disponible
    def test_caso_61(self):
        logging.info("Test del caso 61")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionNoDisponible(self.tablero, const.TIPO_DECISION_COMPETICION)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo decision competicion
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_62(self):
        logging.info("Test del caso 62")
        self.tablero = ControladorTablero()
        tableros.comprobarAccionDeSeleccionMalFormada(self.tablero, const.TIPO_DECISION_COMPETICION)
    
if __name__ == "__main__":
    loggerConfig.initLogger(logging.DEBUG)
    unittest.main()
