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
    Metodo constructor de la clase Entrenamiento, se define los atributos e 
    inicializarlos
    '''
    def __init__(self):
        '''Atributo cnn: contendrá una instancia de la clase Sequential 
        de tensorflow'''
        self.__cnn = None
        '''Atributo resultado: contendrá el resultado de la ultima prediccion
        realizada'''
        self.__resultado = None
        
        self.__cargarModelo()
        
    '''
    Metodo encargado de cargar el modelo entrenado de los ficheros .h5
    '''
    def __cargarModelo(self):
        #cargamos el modelo
        self.__cnn = load_model(data.MODELO_NOMBRE)
        #cargamos los pesos
        self.__cnn.load_weights(data.MODELO_PESOS)
        
    '''
    Metodo que, dado un tablero de entrada, genera una prediccion y la guarda 
    en el atributo resultado
    '''
    def predecir(self, entrada):
        entrada = entrada.flatten()
        entrada = np.array(entrada)
        entrada = np.reshape(entrada, (1, PCNN.altura,PCNN.longitud, 1)) 

        self.__resultado = self.__cnn.predict(entrada)
        
    '''
    Metodo que, dado un el indice del campo del que se desea obtener la 
    prediccion realizada y los posibles valores aceptables, devuelve el valor 
    mas probable
    '''
    def obtenerPrediccionCampo(self, numeroCampo, posiblesValores):
        copiaResultado = np.copy(self.__resultado[0][numeroCampo])
        campo = -1
        
        logging.debug("Prediccion() : numeroCampo = "+str(numeroCampo)+", posiblesValores = "+str(posiblesValores))
        
        for i in range(PCNN.altura):
            campoMayorPonderado = int(np.argmax(copiaResultado))
            
            if(campoMayorPonderado in posiblesValores):
                campo = campoMayorPonderado
                break
            else:
                copiaResultado[campoMayorPonderado] = 0
            
        if(campo == -1):
            raise Exception("Campo no encontrado")
                
        logging.debug("Prediccion() : Resultado = " +str(campo))
        
        return campo
