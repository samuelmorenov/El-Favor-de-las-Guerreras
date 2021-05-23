# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from tensorflow.python.keras.models import load_model

import parameterization.ParametrosDatos as data


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
        entrada = entrada.flatten()
        salida = self.__cnn.predict(entrada)
        return salida
