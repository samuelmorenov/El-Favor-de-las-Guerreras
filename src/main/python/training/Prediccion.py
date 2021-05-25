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
        self.__cargarModelo()
        
    def __cargarModelo(self):
        #cargamos el modelo
        self.__cnn = load_model(data.MODELO_NOMBRE)
        #cargamos los pesos
        self.__cnn.load_weights(data.MODELO_PESOS)
        
    def predecir(self, entrada):
        #Transformación de datos de entrada
        entrada = entrada.flatten()
        entrada = np.array(entrada)
        entrada = np.reshape(entrada, (1, PCNN.altura,PCNN.longitud, 1)) 
        #Prediccion
        salida = self.__cnn.predict(entrada)
        
        #Transformacion de datos de salida
        result = np.zeros(PCNN.salida, dtype=int)
        for i in range(PCNN.salida):
            result[i] = int(salida[0][i])
        
        return result
