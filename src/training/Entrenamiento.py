# -*- coding: utf-8 -*-
import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')

import parameterization.ParametrosDatos as data
import parameterization.ParametrosCNN as PNN


import pandas as pd
import numpy as np
import tensorflow as tf

#from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
#from tensorflow.python.keras import optimizers
#from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense
#from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from tensorflow.keras import layers
#from tensorflow.keras.layers.experimental import preprocessing

from tensorflow.python.framework.ops import disable_eager_execution

class Entrenamiento:
##Pre procesado de datos
    
    def __init__(self):
        
        #Se deshabilita eager execution para poder usar Adam
        disable_eager_execution()
        #Eliminamos sesiones de keras abiertas
        K.clear_session()
        
        entrada, salida = self.preProcesadoDeDatos()
        #print(entrada)
        #print(salida)
        
        self.cnn = None
        self.creacionModelo()
        self.complileAndFit(entrada, salida)
        self.guardarModelo()
        
    def preProcesadoDeDatos(self):
        tipos = int
        cabecera = None
        separador = data.SEPARADOR
        
        data_entrenamiento = data.PARTIDAS_GANADAS_TABLERO
        training_entrada = pd.read_csv(
            data_entrenamiento,
            sep=separador,
            header=cabecera,
            dtype=tipos)
        
        data_entrenamiento = data.PARTIDAS_GANADAS_JUGADAS
        training_salida = pd.read_csv(
            data_entrenamiento,
            sep=separador,
            header=cabecera,
            dtype=tipos)
        
        training_entrada = np.array(training_entrada)
        training_salida = np.array(training_salida)
        
        return training_entrada, training_salida
    
    def establecerCapas(self):
        #Primera capa de convolucion
        self.cnn.add(Convolution2D( 
                PNN.filtrosConv1, 
                PNN.tamanio_filtro1, 
                padding='same', #lo que va a hacer el filtro en las esquinas
                input_shape=(PNN.altura, PNN.longitud, 1), #altura, longitud y rgb
                activation='relu'
                ))
        
        #Primera capa de pooling
        self.cnn.add(MaxPooling2D(
                pool_size=PNN.tamanio_pool
                ))
        
        #Siguiente capa de convolucion
        self.cnn.add(Convolution2D( 
                PNN.filtrosConv2, 
                PNN.tamanio_filtro2, 
                padding='same', #lo que va a hacer el filtro en las esquinas
                activation='relu'
                ))
        
        #Siguiente capa de pooling
        self.cnn.add(MaxPooling2D(
                pool_size=PNN.tamanio_pool
                ))
        
        #Transformacion de la red en una dimension
        self.cnn.add(Flatten())
        
        #Capa densa
        self.cnn.add(Dense(
                256, #numero de neuronas
                activation='relu'
                ))
        
        #Se apagaran el 50% de las neuronas para no atrofiar caminos
        self.cnn.add(Dropout(0.5)) 
        
        #Ultima capa
        self.cnn.add(Dense(
                5, #numero de neuronas de salida
                activation='softmax' #% de cada opcion
                ))
    
    
    def creacionModelo(self):
        self.cnn = tf.keras.Sequential([layers.Dense(64), layers.Dense(1)])
        
        
    def complileAndFit(self, entrada, salida):
        self.cnn.compile(loss = tf.losses.MeanSquaredError(),optimizer = tf.optimizers.Adam())
        self.cnn.fit(entrada, salida, epochs=10)
        
    def guardarModelo(self):
        dir=data.MODELO_DIR

        if not os.path.exists(dir):
            os.mkdir(dir)
            
        self.cnn.save(data.MODELO_NOMBRE) #guardado del modelo
        self.cnn.save_weights(data.MODELO_PESOS) #guardado de los pesos del modelo
