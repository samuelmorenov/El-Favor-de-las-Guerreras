# -*- coding: utf-8 -*-
import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')

import parameterization.ParametrosDatos as data
import parameterization.ParametrosCNN as PCNN


import pandas as pd
import numpy as np
import tensorflow as tf

#from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
#from tensorflow.python.keras import optimizers
#from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense
#from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D, Reshape
from tensorflow.python.keras import backend as K
#from tensorflow.keras import layers
#from tensorflow.keras.layers.experimental import preprocessing

from tensorflow.python.framework.ops import disable_eager_execution

class Entrenamiento:
##Pre procesado de datos
    
    def __init__(self):
        
        #Se deshabilita eager execution para poder usar Adam
        disable_eager_execution()
        #Eliminamos sesiones de keras abiertas
        K.clear_session()
        
        entrada, salida = self.__preProcesadoDeDatos()
        #print(entrada)
        #print(salida)
        
        self.__cnn = None
        self.__creacionModelo()
        self.__establecerCapas()
        self.__complileAndFit(entrada, salida)
        self.__guardarModelo()
        
    def __preProcesadoDeDatos(self):
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
        
        #Transformación de array en matriz
        training_entrada = np.array(training_entrada)
        lenth = int((training_entrada.size) / (PCNN.altura * PCNN.longitud) )
        training_entrada = np.reshape(training_entrada, (lenth,PCNN.altura,PCNN.longitud, 1))
        
        training_salida = np.array(training_salida)#.reshape(PCNN.altura,PCNN.longitud)
        training_salida = np.reshape(training_salida, (lenth,PCNN.salida, 1))
        
        return training_entrada, training_salida
    
    def __creacionModelo(self):
        self.__cnn = tf.keras.Sequential()
        
    def __establecerCapas(self):
        #Primera capa de convolucion
        filtrosConv1=56
        tamanio_filtro1=(1,7)
        self.__cnn.add(Convolution2D( 
                filtrosConv1, 
                tamanio_filtro1, 
                padding='valid',
                #lo que va a hacer el filtro en las esquinas 
                #valid(no hacer padding)/same(añadir 0 a las esquinas)
                input_shape=(PCNN.altura, PCNN.longitud, 1), #altura, longitud y profundidad
                activation='relu'
                ))
        '''
        #Primera capa de pooling
        tamanio_pool=(2,2)
        self.__cnn.add(MaxPooling2D(
                pool_size=tamanio_pool
                ))
        
        
        #Siguiente capa de convolucion
        filtrosConv2=64
        tamanio_filtro2=(2,2)
        self.__cnn.add(Convolution2D( 
                filtrosConv2, 
                tamanio_filtro2, 
                padding='same', #lo que va a hacer el filtro en las esquinas
                activation='relu'
                ))
        
        #Siguiente capa de pooling
        tamanio_pool=(2,2)
        self.__cnn.add(MaxPooling2D(
                pool_size=tamanio_pool
                ))
        '''
        
        #Transformacion de la red en una dimension
        self.__cnn.add(Flatten())
        
        #Capa densa
        self.__cnn.add(Dense(
                448*4, #numero de neuronas
                activation='relu'
                ))
        
        #Se apagaran el 50% de las neuronas para no atrofiar caminos
        self.__cnn.add(Dropout(0.5)) 
        
        #Ultima capa
        self.__cnn.add(Dense(
                PCNN.salida*PCNN.n_clases, #numero de neuronas de salida
                activation='softmax' #% de cada opcion
                ))
        
        
        self.__cnn.add(Reshape((PCNN.salida, PCNN.n_clases)))
        
    def __complileAndFit(self, entrada, salida):
        self.__cnn.compile(
                loss='sparse_categorical_crossentropy',
                optimizer=tf.optimizers.Adam(lr=PCNN.lr), #optimizador Adam
                metrics=['accuracy'] #metrica de optimizacion, % de aprendizaje
                )
        
        self.__cnn.fit(entrada, salida, epochs=PCNN.epocas)
        
    def __guardarModelo(self):
        dir=data.MODELO_DIR

        if not os.path.exists(dir):
            os.mkdir(dir)
            
        self.__cnn.save(data.MODELO_NOMBRE) #guardado del modelo
        self.__cnn.save_weights(data.MODELO_PESOS) #guardado de los pesos del modelo
        
        #print(self.__cnn.summary())
