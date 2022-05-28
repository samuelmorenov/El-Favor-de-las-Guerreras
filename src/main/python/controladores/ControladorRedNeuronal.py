# -*- coding: utf-8 -*-
import logging
import numpy as np

import main.python.parametrizacion.ParametrosTablero as const

from main.python.redNeuronal.Prediccion import Prediccion

'''
Clase controladora del jugador controlado por la red neuronal entrenada
anteriormente.
'''
class ControladorRedNeuronal:
    '''
    Método constructor de la clase ControladorRedNeuronal, recibe el nombre y
    el numero para guardarlo en sus respectivos atributos. Además, inicializa 
    el atributo Prediccion que implementa la clase Prediccion.
    '''
    def __init__(self, miNombre, miNumero):
        '''Atributo miNombre: Define el nombre para leerlo en los logs.'''
        self.__miNombre = miNombre
        '''Atributo miNumero: Define el orden del jugador, puede ser 1 o 2.'''
        self.__miNumero = miNumero
        '''Atributo prediccion: Instancia la clase Prediccion que corresponde 
        a la parte de la red neuronal encargada de generar predicciones.'''
        self.__prediccion = Prediccion()
        
    '''
    Método para generar una acción, recibe la matriz del tablero y devuelve un 
    array con una acción correcta que será seleccionada por la red neuronal y 
    procesada por el Método __procesarAccion.
    '''
    def decidirAccion(self, tablero):
        
        logging.info(self.__miNombre+" : Este es el tablero que me llega:\n"+str(tablero))
            
        self.__prediccion.predecir(tablero)
        salida = self.__procesarAccion(tablero)
        
        logging.info(self.__miNombre+" : Esta es la accion completa que realizo: "+str(salida))
        logging.info(self.__miNombre+" : ___________________________________") #Separador
        return salida
    
    '''
    Método encargado de procesar el resultado emitido por la red neuronal para 
    transformarlo en una acción correctamente formada y válida para el tablero 
    actual. Esto se debe a que la red neuronal devuelve el valor en porcentajes 
    de acierto, que no están exentos de fallos.
    '''
    def __procesarAccion(self, tablero):
        listaDeCartasEnMano, listaAccionesPosibles = self.__obtenerCartasEnManoYAccionesPosibles(tablero)
        
        accionARealizar = self.__prediccion.obtenerPrediccionCampo(const.ACCION_REALIZADA, listaAccionesPosibles)
        
        logging.debug(self.__miNombre+" : He decidido realizar la accion: "+str(accionARealizar))
        
        accionCount = self.__obtenerAccionCount(accionARealizar)
        cartasSeleccionadas = []
        for i in range(accionCount):
            carta = self.__prediccion.obtenerPrediccionCampo(i+1, listaDeCartasEnMano)
            listaDeCartasEnMano = self.__eliminarCarta(carta, listaDeCartasEnMano)
            cartasSeleccionadas.append(carta)
            
        logging.debug(self.__miNombre+" : He seleccionado estas cartas para hacer la accion: "+str(cartasSeleccionadas))
            
        accionCompleta = self.__crearAccionCompleta(accionARealizar, cartasSeleccionadas)
            
        return accionCompleta
        
    '''
    Método encargado de devolver una lista con las cartas que hay en la mano y 
    otra lista con las acciones posibles que puede realizar el jugador para el 
    tablero dado. Este Método es necesario para el Método __procesarAccion.
    '''
    def __obtenerCartasEnManoYAccionesPosibles(self, tablero):
    
        listaDeCartasEnMano = []
        
        for i in range(len(tablero[const.MANO_JUGADOR1])):
            if(tablero[const.MANO_JUGADOR1][i] != 0):
                listaDeCartasEnMano.append(tablero[const.MANO_JUGADOR1][i])
                
        listaDeCartasEnMano = np.array(listaDeCartasEnMano)
        
        listaAccionesPosibles = []
        accionesRealizadas = tablero[const.ACCIONES_USADAS_JUGADOR1]
            
        logging.debug(self.__miNombre+" : Estas son las acciones realizadas: "+str(accionesRealizadas))
         
                
        if(accionesRealizadas[const.TIPO_SECRETO] == 0):
            listaAccionesPosibles.append(const.TIPO_SECRETO)
        if(accionesRealizadas[const.TIPO_RENUNCIA_1] == 0):
            listaAccionesPosibles.append(const.TIPO_RENUNCIA)
        if(accionesRealizadas[const.TIPO_REGALO] == 0):
            listaAccionesPosibles.append(const.TIPO_REGALO)
        if(accionesRealizadas[const.TIPO_COMPETICION] == 0):
            listaAccionesPosibles.append(const.TIPO_COMPETICION)
           
        logging.debug(self.__miNombre+" : Estas son las acciones que puedo hacer: "+str(listaAccionesPosibles))
            
        return listaDeCartasEnMano, listaAccionesPosibles
    
    '''
    Método que devuelve el número de cartas que debe tener la acción a 
    realizar dada por parámetro. Este Método es necesario para el 
    método __procesarAccion.
    '''
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
    
    '''
    Método que devuelve un array con las cartas en mano a la que se le ha 
    retirado la carta seleccionada. Este Método es necesario para el Método 
    __procesarAccion.
    '''
    def __eliminarCarta(self, cartaSeleccionada, listaDeCartasEnMano):
        posiciones = np.where(listaDeCartasEnMano == cartaSeleccionada)
        posicion = posiciones[0][0]
        
        listaDeCartasEnMano_Modificada = np.delete(listaDeCartasEnMano, posicion)
        return listaDeCartasEnMano_Modificada
    
    '''
    Método para generar la acción de selección pendiente, recibe la matriz del 
    tablero y devuelve un array con la acción correctamente formada con las 
    cartas seleccionadas por red neuronal y procesada por el Método 
    __procesarAccionDeSeleccion.
    '''
    def decidirAccionDeSeleccion(self, tablero):
        logging.info(self.__miNombre+" : Esta es la accion pendiente que me llega: "+str(tablero[const.ACCION_PENDIENTE]))
            
        salida =  self.__prediccion.predecir(tablero)
        salida = self.__procesarAccionDeSeleccion(tablero)
        
        logging.info(self.__miNombre+" : Esta es la accion completa que realizo: "+str(salida))
        logging.info(self.__miNombre+" : ___________________________________") #Separador
        return salida
    
    '''
    Método encargado de procesar el resultado emitido por la red neuronal para 
    transformarlo en una acción de selección correctamente formada y válida 
    para el tablero actual. Esto se debe a que la red neuronal devuelve el 
    valor en porcentajes de acierto, que no están exentos de fallos.
    '''
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
            
    '''
    Método encargado de procesar el resultado emitido por la red neuronal para 
    la acción de selección específica de tipo regalo para una acción pendiente 
    dada.
    '''
    def __seleccionarCartasAccionDeSeleccionRegalo(self, accionPendienteList):   
        cartasSeleccionadas = []
        cartasList = []
        cartasList.append(accionPendienteList[const.PENDIENTE_5_1]) 
        cartasList.append(accionPendienteList[const.PENDIENTE_5_2])
        cartasList.append(accionPendienteList[const.PENDIENTE_5_3])

        carta = self.__prediccion.obtenerPrediccionCampo(const.PENDIENTE_5_ELEGIDA, cartasList)
        cartasSeleccionadas.append(carta)
        return cartasSeleccionadas
        
    '''
    Método encargado de procesar el resultado emitido por la red neuronal para 
    la acción de selección específica de tipo competición para una acción 
    pendiente dada.
    '''
    def __seleccionarCartasAccionDeSeleccionCompeticion(self, accionPendienteList):  
        cartasSeleccionadas = []
        cartasList = []
        if(accionPendienteList[const.PENDIENTE_6_1_1] == accionPendienteList[const.PENDIENTE_6_2_1]):
            cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_1])
            
            cartasList.append(accionPendienteList[const.PENDIENTE_6_1_2]) 
            cartasList.append(accionPendienteList[const.PENDIENTE_6_2_2])
            carta = self.__prediccion.obtenerPrediccionCampo(const.PENDIENTE_6_ELEGIDA_2, cartasList)
            
            cartasSeleccionadas.append(carta)
            
        else:
            cartasList.append(accionPendienteList[const.PENDIENTE_6_1_2]) 
            cartasList.append(accionPendienteList[const.PENDIENTE_6_2_2])
            carta = self.__prediccion.obtenerPrediccionCampo(const.PENDIENTE_6_ELEGIDA_1, cartasList)
            
            if(carta == accionPendienteList[const.PENDIENTE_6_1_2]):
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_1])
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_1_2])
            else:
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_2_1])
                cartasSeleccionadas.append(accionPendienteList[const.PENDIENTE_6_2_2])

        return cartasSeleccionadas
    
    '''
    Método que crea un array acción a partir del tipo de acción y las cartas 
    seleccionadas.
    '''
    def __crearAccionCompleta(self, accionARealizar, cartasSeleccionadas):
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
            
        elif(accionARealizar == const.TIPO_DECISION_COMPETICION):
            accionCompleta[const.PENDIENTE_6_ELEGIDA_1] = cartasSeleccionadas.pop(0)
            accionCompleta[const.PENDIENTE_6_ELEGIDA_2] = cartasSeleccionadas.pop(0)
            
        else:
            raise Exception("Error al encontrar accion en red neuronal")
            
        return accionCompleta

    '''
    Método que sirve para cerrar los hilos pendientes de los jugadores, en este
    caso no es necesario cerrar ninguno.
    '''
    def finish(self):
        return
    
    '''
    Método get para el atributo de tipo string: miNombre
    '''
    def getMiNombre(self):
        return self.__miNombre
    
    '''
    Método get para el atributo de tipo string: miNumero
    '''
    def getMiNumero(self):
        return self.__miNumero
    
