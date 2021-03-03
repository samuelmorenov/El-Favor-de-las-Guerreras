# -*- coding: utf-8 -*-

import numpy as np

import Constantes as const

LOG = False

class BotTonto:
    def __init__(self, yo):
        self.__yo = yo
        
        
    def decidirAccion(self, tablero):

        if(self.__yo == "Bot 1"):
            print("\033[;33m",end="") #Amarillo
        if(self.__yo == "Bot 2"):
            print("\033[;36m",end="") #Cian
        
        
        print("Soy "+self.__yo)
        
        print("- Este es el tablero que me llega:")
        print(tablero)
    
        listaDeCartasEnMano = []
        
        for i in range(len(tablero[const.MANO_JUGADOR1])):
            if(tablero[const.MANO_JUGADOR1][i] != 0):
                listaDeCartasEnMano.append(tablero[const.MANO_JUGADOR1][i])
        
        if(LOG):
            print("- Estas son las cartas de mi mano:")
            print(listaDeCartasEnMano)
        
        listaAccionesPosibles = []
        accionesRealizadas = tablero[const.ACCIONES_USADAS_JUGADOR1]
        
        if(LOG):
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
           
        if(LOG):
            print("- Estas son las acciones que puedo hacer:")
            print(listaAccionesPosibles)
        
        accionARealizar = listaAccionesPosibles.pop(np.random.randint(len(listaAccionesPosibles)))
        
        if(LOG):
            print("- He decidido realizar la accion: ")
            print(accionARealizar)        
        
        cartasSeleccionadas = []
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
            
        for c in range(accionCount):
            posicion = np.random.randint(len(listaDeCartasEnMano))
            carta = listaDeCartasEnMano.pop(posicion)
            cartasSeleccionadas.append(carta)
            
        if(LOG):
            print("- He seleccionado estas cartas para hacer la accion:")
            print(cartasSeleccionadas)
            print("- Estas son las cartas que quedan en mi mano:")
            print(listaDeCartasEnMano)        

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
            
        else:
            raise Exception("Error al encontrar accion en bot")
            
        print("- Esta es la accion completa que realizo:")
        print(accionCompleta)
        print("\033[0m",end="")
        print("___________________________________") #Separador de bots
        return accionCompleta
    
    def decidirAccionDeSeleccion(self, tablero):
        
        if(self.__yo == "Bot 1"):
            print("\033[;33m",end="") #Amarillo
        if(self.__yo == "Bot 2"):
            print("\033[;36m",end="") #Cian
        
        
        print("Soy "+self.__yo)
        
        print("- Esta es la accion pendiente que me llega:")
        print(tablero[const.ACCION_PENDIENTE])
        
        accionPendienteList = tablero[const.ACCION_PENDIENTE]
        accionPendienteTipo = accionPendienteList[const.PENDIENTE_TIPO]
        
        accionCompleta = np.zeros(const.NCOLUMNA, dtype=int)
        accionCompleta[const.ACCION_REALIZADA] = accionPendienteTipo
        
        if(accionPendienteTipo == const.TIPO_DECISION_REGALO):
            cartasList = []
            cartasList.append(accionPendienteList[const.PENDIENTE_5_1]) 
            cartasList.append(accionPendienteList[const.PENDIENTE_5_2])
            cartasList.append(accionPendienteList[const.PENDIENTE_5_3])
            
            posicion = np.random.randint(len(cartasList))
            carta = cartasList.pop(posicion)
            accionCompleta[const.PENDIENTE_5_ELEGIDA] = carta
            
        elif(accionPendienteTipo == const.TIPO_DECISION_COMPETICION):

            cartasElegidas = np.random.randint(2)
            
            if(cartasElegidas == 1):
                accionCompleta[const.PENDIENTE_6_ELEGIDA_1] = accionPendienteList[const.PENDIENTE_6_1_1]
                accionCompleta[const.PENDIENTE_6_ELEGIDA_2] = accionPendienteList[const.PENDIENTE_6_1_2]
            else:
                accionCompleta[const.PENDIENTE_6_ELEGIDA_1] = accionPendienteList[const.PENDIENTE_6_2_1]
                accionCompleta[const.PENDIENTE_6_ELEGIDA_2] = accionPendienteList[const.PENDIENTE_6_2_2]
                        
        else:
            raise Exception("Error al encontrar accion en bot")
        
        print("- Esta es la accion completa que realizo:")
        print(accionCompleta)
        print("\033[0m",end="")
        print("___________________________________") #Separador de bots
        return accionCompleta
