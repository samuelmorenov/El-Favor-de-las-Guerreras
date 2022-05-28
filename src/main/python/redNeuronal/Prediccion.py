# -*- coding: utf-8 -*-
import logging

import numpy as np

from tensorflow.python.keras.models import load_model

import main.python.parametrizacion.ParametrosDatos as data
import main.python.parametrizacion.ParametrosCNN as PCNN

'''
Clase encargada de utilizar el modelo entrenado para generar predicciones
'''
class Prediccion:
    '''
    Método constructor de la clase Entrenamiento, se define los atributos e 
    inicializarlos.
    '''
    def __init__(self):
        '''Atributo cnn: Contendrá una instancia de la clase Sequential.
        de tensorflow'''
        self.__cnn = None
        '''Atributo resultado: contendrá el resultado de la ultima prediccion
        realizada'''
        self.__resultado = None
        
        self.__cargarModelo()
        
    '''
    Método encargado de cargar el modelo entrenado de los ficheros .h5
    '''
    def __cargarModelo(self):
        #cargamos el modelo
        self.__cnn = load_model(data.MODELO_NOMBRE)
        #cargamos los pesos
        self.__cnn.load_weights(data.MODELO_PESOS)
        
    '''
    Método que, dado un tablero de entrada, genera una predicción y la guarda
    en el atributo resultado.
    '''
    def predecir(self, entrada):
        entrada = entrada.flatten()
        entrada = np.array(entrada)
        entrada = np.reshape(entrada, (1, PCNN.altura,PCNN.longitud, 1)) 

        self.__resultado = self.__cnn.predict(entrada)
        
    '''
    Método que, dado un el índice del campo del que se desea obtener la 
    predicción realizada y los posibles valores aceptables, devuelve el 
    valor más probable.
    '''
    def obtenerPrediccionCampo(self, numeroCampo, posiblesValores):
        copiaResultado = np.copy(self.__resultado[0][numeroCampo])
        valorSeleccionado = posiblesValores[0]
        valorMayorPonderado = 0
        
        logging.debug("Prediccion() : numeroCampo = "+str(numeroCampo)+", posiblesValores = "+str(posiblesValores))
        logging.debug("Ponderaciones = "+str(copiaResultado))
        
        for i in range(len(copiaResultado)):
            if((i in posiblesValores) and (copiaResultado[i] > copiaResultado[valorSeleccionado])):
                valorSeleccionado = i
            if((copiaResultado[i] > copiaResultado[valorMayorPonderado])):
                valorMayorPonderado = i
                
        logging.debug("Prediccion() : Resultado = " +str(valorSeleccionado)+", Mayor ponderado = "+str(valorMayorPonderado))
        
        return valorSeleccionado
