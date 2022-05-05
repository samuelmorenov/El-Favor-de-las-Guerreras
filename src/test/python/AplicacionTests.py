# -*- coding: utf-8 -*-
import unittest
import logging
import sys, os

base = os.path.dirname(__file__)
sys.path.insert(0, os.path.normpath(base+"/.."))
sys.path.insert(0, os.path.normpath(base+"/../.."))

from main.python.controladores.ControladorBot import ControladorBot
from main.python.controladores.ControladorRedNeuronal import ControladorRedNeuronal
from main.python.controladores.ControladorTablero import ControladorTablero
from auxiliares.ComprobarAcciones import ComprobarAcciones
from auxiliares.ComprobarTablero import ComprobarTablero

import main.python.parametrizacion.ParametrosTablero as const

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
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_2(self):
        acciones.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba del bot, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_3(self):
        acciones.accionException(self.bot, manoVacia, accionesDisponiblesTodas)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_4(self):
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_5(self):
        acciones.accionCorrecta(self.bot, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_6(self):
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_7(self):
        acciones.accionCorrecta(self.bot, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_8(self):
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_9(self):
        acciones.accionCorrecta(self.bot, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_10(self):
        acciones.accionCorrecta(self.bot, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_11(self):
        acciones.accionCorrecta(self.bot, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba del bot, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_12(self):
        acciones.accionException(self.bot, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Bot Seleccionar accion de seleccion-----------------
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_13(self):
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_14(self):
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_15(self):
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_16(self):
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba del bot, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_17(self):
        acciones.accionSeleccionCorrecta(self.bot, cartasAccionSeleccionCompeticionDistintas)
        
    #-----------------------Red neuronal Seleccionar accion-----------------------
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    7 cartas distintas a elegir
    def test_caso_18(self):
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    4 cartas iguales a elegir
    def test_caso_19(self):
        acciones.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesTodas)
         
    #Prueba de la red neuronal, seleccion de accion con:
    #    4 acciones libres
    #    0 cartas a elegir        
    def test_caso_20(self):
        acciones.accionException(self.redNeuronal, manoVacia, accionesDisponiblesTodas)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    7 cartas distintas a elegir        
    def test_caso_21(self):
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesSecreto)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Secreto
    #    1 carta a elegir
    def test_caso_22(self):
        acciones.accionCorrecta(self.redNeuronal, mano1Iguales, accionesDisponiblesSecreto)
  
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    7 cartas distintas a elegir
    def test_caso_23(self):
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRenuncia)
    
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Renuncia
    #    2 de cartas a elegir, todas iguales
    def test_caso_24(self):
        acciones.accionCorrecta(self.redNeuronal, mano2Iguales, accionesDisponiblesRenuncia)
   
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    7 cartas distintas a elegir
    def test_caso_25(self):
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesRegalo)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Regalo
    #    3 de cartas a elegir, todas iguales
    def test_caso_26(self):
        acciones.accionCorrecta(self.redNeuronal, mano3Iguales, accionesDisponiblesRegalo)
 
    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    7 cartas distintas a elegir
    def test_caso_27(self):
        acciones.accionCorrecta(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Accion libre de tipo Competicion
    #    4 de cartas a elegir, todas iguales
    def test_caso_28(self):
        acciones.accionCorrecta(self.redNeuronal, mano4Iguales, accionesDisponiblesCompeticion)

    #Prueba de la red neuronal, seleccion de accion con:
    #    Sin acciones libres
    def test_caso_29(self):
        acciones.accionException(self.redNeuronal, mano7CartasDistintas, accionesDisponiblesNinguna)
        
    #-----------------Red neuronal Seleccionar accion de seleccion-----------------
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas distintas
    def test_caso_30(self):
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo0Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   2 cartas iguales
    def test_caso_31(self):
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo2Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo regalo con:
    #   Todas las cartas iguales
    def test_caso_32(self):
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionRegalo3Iguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones iguales
    def test_caso_33(self):
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionIguales)
        
    #Prueba de la red neuronal, seleccion de accion de seleccion de tipo competicion con:
    #   Las dos opciones distintas
    def test_caso_34(self):
        acciones.accionSeleccionCorrecta(self.redNeuronal, cartasAccionSeleccionCompeticionDistintas)
        
    #-----------------Tablero-----------------
    #Prueba del tablero, creacion del tablero:
    def test_caso_35(self):
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
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararAccionSeleccionJugador1(self.tablero, self.bot, self.bot2, const.TIPO_DECISION_REGALO)
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        
        tableros.accionSeleccionCorrecta(tableroAux[const.ACCION_PENDIENTE], const.TIPO_DECISION_REGALO)
        
    #Prueba del tablero, vista del tablero:
    #   Con accion pendiente de selección
    #   Es de tipo 4
    def test_caso_41(self):
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero = tableros.prepararAccionSeleccionJugador1(self.tablero, self.bot, self.bot2, const.TIPO_DECISION_COMPETICION)
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        
        tableros.accionSeleccionCorrecta(tableroAux[const.ACCION_PENDIENTE], const.TIPO_DECISION_COMPETICION)
        
    #Prueba del tablero, robar carta:
    #   Tiene la mano con un solo hueco
    def test_caso_42(self):
        self.tablero = ControladorTablero()
        self.tablero.jugadorRobaCarta(const.JUGADOR1)
        
    #Prueba del tablero, robar carta:
    #   Tiene la mano llena
    def test_caso_43(self):
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        self.tablero.jugadorRobaCarta(const.JUGADOR1)
        with self.assertRaises(Exception):
            self.tablero.jugadorRobaCarta(const.JUGADOR1)
        
    #Prueba del tablero, robar carta:
    #   El mazo esta vacio
    def test_caso_44(self):
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
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = tableros.seleccionarCartasDeMano(tableroAux, const.TIPO_SECRETO, const.ACCION_1_COUNT)
        
        tableros.comprobarQueSeRealizaLaAccion(self.tablero, accion, cartas, const.JUGADOR1, const.MANO_JUGADOR1)
        
    #Prueba del tablero, realizar una accion:
    #   Tipo secreto
    #   El tipo de accion no esta disponible
    def test_caso_46(self):
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = tableros.seleccionarCartasDeMano(tableroAux, const.TIPO_SECRETO, const.ACCION_1_COUNT)
        tableros.comprobarQueSeRealizaLaAccion(self.tablero, accion, cartas, const.JUGADOR1, const.MANO_JUGADOR1)
        
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = tableros.seleccionarCartasDeMano(tableroAux, const.TIPO_SECRETO, const.ACCION_1_COUNT)
        tableros.comprobarExceptionAlRealizarLaAccion(self.tablero, accion)
    
    #Prueba del tablero, realizar una accion:
    #   Tipo secreto
    #   La accion tiene un numero incorrecto de cartas
    def test_caso_47(self):
        self.tablero = ControladorTablero()
        self.tablero.initRonda()
        tableroAux = self.tablero.getVistaTablero(const.JUGADOR1)
        accion, cartas = tableros.seleccionarCartasDeMano(tableroAux, const.TIPO_SECRETO, const.ACCION_1_COUNT+1)
        
        tableros.comprobarExceptionAlRealizarLaAccion(self.tablero, accion)
        
def initLogger():
    logging.basicConfig(filename='logfile.log',level=logging.INFO)
    
    logger = logging.getLogger()
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])
    
    logging.getLogger().addHandler(logging.StreamHandler())
    
if __name__ == "__main__":
    initLogger()
    unittest.main()
