# -*- coding: utf-8 -*-
import os

import parametrizacion.ParametrosDatos as data
import parametrizacion.ParametrosCNN as PCNN

import pandas as pd
import numpy as np
import tensorflow as tf

from tensorflow.python.keras.layers import Dropout, Flatten, Dense
from tensorflow.python.keras.layers import  Convolution2D, Reshape
from tensorflow.python.keras import backend as K

from tensorflow.python.framework.ops import disable_eager_execution

class Entrenamiento:
    
    def __init__(self):
        self.__cnn = None
        
    def run(self):
        #Se deshabilita eager execution para poder usar Adam
        disable_eager_execution()
        #Eliminamos sesiones de keras abiertas
        K.clear_session()
        
        entrada, salida = self.__preProcesadoDeDatos()
        
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
        
        training_salida = np.array(training_salida)
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
        
        #Cambio del formato de la salida
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
            
        #guardado del modelo
        self.__cnn.save(data.MODELO_NOMBRE) 
        #guardado de los pesos del modelo
        self.__cnn.save_weights(data.MODELO_PESOS) 
