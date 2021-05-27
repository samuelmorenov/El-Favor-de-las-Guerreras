# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import numpy as np

import parameterization.ParametrosTablero as const
import parameterization.ParametrosMenu as menu

from training.Prediccion import Prediccion

class NeuralNetworkController:
    def __init__(self, miNombre, miNumero):
        self.miNombre = miNombre
        self.miNumero = miNumero
        self.Prediccion = Prediccion()
        
    def decidirAccion(self, tablero):
        if(menu.PRINT_TRACE):
            if(self.miNumero == const.JUGADOR1):
                print("\033[;33m",end="") #Amarillo
            if(self.miNumero == const.JUGADOR2):
                print("\033[;36m",end="") #Cian
            
            print("Soy "+self.miNombre)
            
            print("- Este es el tablero que me llega:")
            print(tablero)
            
        self.Prediccion.predecir(tablero)
        salida = self.__procesarAccion(tablero)
        
        if(menu.PRINT_TRACE):
            print("- Esta es la accion completa que realizo:")
            print(salida)
            print("\033[0m",end="")
            print("___________________________________") #Separador
        return salida
    
    def __procesarAccion(self, tablero):
        listaDeCartasEnMano, listaAccionesPosibles = self.__obtenerCartasEnManoYAccionesPosibles(tablero)
        
        accionARealizar = self.Prediccion.obtenerPrediccionCampo(const.ACCION_REALIZADA, listaDeCartasEnMano)
        
        accionCount = self.__obtenerAccionCount(accionARealizar)
        cartasSeleccionadas = []
        for i in range(accionCount):
            carta = self.Prediccion.obtenerPrediccionCampo(i+1, listaDeCartasEnMano)
            listaDeCartasEnMano = self.__eliminarCarta(carta, listaDeCartasEnMano)
            cartasSeleccionadas.append(carta)
            
        accionCompleta = self.__crearAccionCompleta(accionARealizar, cartasSeleccionadas)
            
        return accionCompleta
        
    
    def __obtenerCartasEnManoYAccionesPosibles(self, tablero):
        if(menu.PRINT_PREDICCION):        
            print("- Este es el tablero que me llega:")
            print(tablero)
    
        listaDeCartasEnMano = []
        
        for i in range(len(tablero[const.MANO_JUGADOR1])):
            if(tablero[const.MANO_JUGADOR1][i] != 0):
                listaDeCartasEnMano.append(tablero[const.MANO_JUGADOR1][i])
                
        listaDeCartasEnMano = np.array(listaDeCartasEnMano)
        
        if(menu.PRINT_PREDICCION):
            print("- Estas son las cartas de mi mano:")
            print(listaDeCartasEnMano)
        
        listaAccionesPosibles = []
        accionesRealizadas = tablero[const.ACCIONES_USADAS_JUGADOR1]
        
        if(menu.PRINT_PREDICCION):
            print("- Estas son las acciones realizadas:")
            print(accionesRealizadas)
        
        if(accionesRealizadas[const.TIPO_SECRETO] == 0):
            listaAccionesPosibles.append(const.TIPO_SECRETO)
        if(accionesRealizadas[const.TIPO_RENUNCIA_1] == 0):
            listaAccionesPosibles.append(const.TIPO_RENUNCIA)
        if(accionesRealizadas[const.TIPO_REGALO] == 0):
            listaAccionesPosibles.append(const.TIPO_REGALO)
        if(accionesRealizadas[const.TIPO_COMPETICION] == 0):
            listaAccionesPosibles.append(const.TIPO_COMPETICION)
           
        if(menu.PRINT_PREDICCION):
            print("- Estas son las acciones que puedo hacer:")
            print(listaAccionesPosibles)
            
        return listaDeCartasEnMano, listaAccionesPosibles
    
    def __obtenerAccionCount(self, accionARealizar):
        accionCount = 0
        
        if(accionARealizar == const.TIPO_SECRETO):
            accionCount = const.ACCION_1_COUNT
        elif(accionARealizar == const.TIPO_RENUNCIA):
            accionCount = const.ACCION_2_COUNT
        elif(accionARealizar == const.TIPO_REGALO):
            accionCount = const.ACCION_3_COUNT
        elif(accionARealizar == const.TIPO_COMPETICION):
            accionCount = const.ACCION_4_COUNT
        else:
            raise Exception("Accion erronea")
        
        return accionCount
    
    def __eliminarCarta(self, cartaSeleccionada, listaDeCartasEnMano):
        posiciones = np.where(listaDeCartasEnMano == cartaSeleccionada)
        posicion = posiciones[0][0]
        
        listaDeCartasEnMano_Modificada = np.delete(listaDeCartasEnMano, posicion)
        return listaDeCartasEnMano_Modificada
    
    def decidirAccionDeSeleccion(self, tablero):
        if(menu.PRINT_TRACE):
            if(self.miNumero == const.JUGADOR1):
                print("\033[;33m",end="") #Amarillo
            if(self.miNumero == const.JUGADOR2):
                print("\033[;36m",end="") #Cian
            
            
            print("Soy "+self.miNombre)
            
            print("- Esta es la accion pendiente que me llega:")
            print(tablero[const.ACCION_PENDIENTE])
            
        salida =  self.Prediccion.predecir(tablero)
        salida = self.__procesarAccionDeSeleccion(tablero, salida)
        
        if(menu.PRINT_TRACE):
            print("- Esta es la accion completa que realizo:")
            print(salida)
            print("\033[0m",end="")
            print("___________________________________") #Separador
        return salida
    
    def __procesarAccionDeSeleccion(self, tablero):        
        accionPendienteList = tablero[const.ACCION_PENDIENTE]
        accionPendienteTipo = accionPendienteList[const.PENDIENTE_TIPO]
        
        if(accionPendienteTipo == const.TIPO_DECISION_REGALO):
            cartasSeleccionadas = self.__seleccionarCartasAccionDeSeleccionRegalo(accionPendienteList)
            
        elif(accionPendienteTipo == const.TIPO_DECISION_COMPETICION):
            cartasSeleccionadas = self.__seleccionarCartasAccionDeSeleccionCompeticion(accionPendienteList)
            
        else:
            raise Exception("Error al encontrar accion en red neuronal")
            
        accionCompleta = self.__crearAccionCompleta(accionPendienteTipo, cartasSeleccionadas)
        
        return accionCompleta
            
    def __seleccionarCartasAccionDeSeleccionRegalo(self, accionPendienteList):   
        cartasSeleccionadas = []
        cartasList = []
        cartasList.append(accionPendienteList[const.PENDIENTE_5_1]) 
        cartasList.append(accionPendienteList[const.PENDIENTE_5_2])
        cartasList.append(accionPendienteList[const.PENDIENTE_5_3])

        carta = self.Prediccion.obtenerPrediccionCampo(const.ACCION_REALIZADA, cartasList)
        cartasSeleccionadas.append(carta)
        return cartasSeleccionadas
        
    def __seleccionarCartasAccionDeSeleccionCompeticion(self, accionPendienteList):  
        cartasSeleccionadas = []
        cartasList = []
        if(accionPendienteList[const.PENDIENTE_6_1_1] == accionPendienteList[const.PENDIENTE_6_2_1]):
            cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_1])
            
            cartasList.append(accionPendienteList[const.PENDIENTE_6_1_2]) 
            cartasList.append(accionPendienteList[const.PENDIENTE_6_2_2])
            carta = self.Prediccion.obtenerPrediccionCampo(const.ACCION_REALIZADA, cartasList)
            
            cartasSeleccionadas.append(carta)
            
        else:
            cartasList.append(accionPendienteList[const.PENDIENTE_6_1_2]) 
            cartasList.append(accionPendienteList[const.PENDIENTE_6_2_2])
            carta = self.Prediccion.obtenerPrediccionCampo(const.ACCION_REALIZADA, cartasList)
            
            if(carta == accionPendienteList[const.PENDIENTE_6_1_2]):
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_1])
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_2])
            else:
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_2_1])
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_2_2])

        return cartasSeleccionadas
    
    def __crearAccionCompleta(accionARealizar, cartasSeleccionadas):
        accionCompleta = np.zeros(const.NCOLUMNA, dtype=int)
        
        accionCompleta[const.ACCION_REALIZADA] = accionARealizar
        
        if(accionARealizar == const.TIPO_SECRETO):
            accionCompleta[const.ACCION_1] = cartasSeleccionadas.pop(0)
            
        elif(accionARealizar == const.TIPO_RENUNCIA):
            accionCompleta[const.ACCION_2_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_2_2] = cartasSeleccionadas.pop(0)
            
        elif(accionARealizar == const.TIPO_REGALO):
            accionCompleta[const.ACCION_3_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_3_2] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_3_3] = cartasSeleccionadas.pop(0)
            
        elif(accionARealizar == const.TIPO_COMPETICION):
            accionCompleta[const.ACCION_4_1_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_4_1_2] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_4_2_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.ACCION_4_2_2] = cartasSeleccionadas.pop(0)
            
        elif(accionARealizar == const.TIPO_DECISION_REGALO):
            accionCompleta[const.PENDIENTE_5_ELEGIDA] = cartasSeleccionadas.pop(0)
            
        elif(accionARealizar == const.TIPO_DECISION_REGALO):
            accionCompleta[const.PENDIENTE_6_ELEGIDA_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.PENDIENTE_6_ELEGIDA_2] = cartasSeleccionadas.pop(0)
            
        else:
            raise Exception("Error al encontrar accion en red neuronal")
            
        return accionCompleta

    def finish(self):
        return
