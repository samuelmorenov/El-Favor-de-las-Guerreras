# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from tensorflow.python.keras.models import load_model

import parameterization.ParametrosDatos as data


class PartidaController:
    def __init__(self):
        self.cnn = None
        
    def cargarModelo(self):
        #cargamos el modelo
        self.cnn = load_model(data.MODELO_NOMBRE)
        #cargamos los pesos
        self.cnn.load_weights(data.MODELO_PESOS)
