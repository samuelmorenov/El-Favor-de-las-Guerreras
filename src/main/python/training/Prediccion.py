# -*- coding: utf-8 -*-
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
        campo = 0
        
        while(campo == 0):
            campoMayorPonderado = int(np.argmax(copiaResultado))
            if(campoMayorPonderado in posiblesValores):
                campo = campoMayorPonderado
            else:
                copiaResultado[campoMayorPonderado] = 0
        
        return campo
