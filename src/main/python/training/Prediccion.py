# -*- coding: utf-8 -*-

import logging
import sys
sys.path.append('../')

import numpy as np

from tensorflow.python.keras.models import load_model

import parameterization.ParametrosDatos as data
import parameterization.ParametrosCNN as PCNN

class Prediccion:
    def __init__(self):
        self.__cnn = None
        self.__resultado = None
        self.__cargarModelo()
        
    def __cargarModelo(self):
        #cargamos el modelo
        self.__cnn = load_model(data.MODELO_NOMBRE)
        #cargamos los pesos
        self.__cnn.load_weights(data.MODELO_PESOS)
        
    def predecir(self, entrada):
        entrada = entrada.flatten()
        entrada = np.array(entrada)
        entrada = np.reshape(entrada, (1, PCNN.altura,PCNN.longitud, 1)) 

        self.__resultado = self.__cnn.predict(entrada)
    
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
