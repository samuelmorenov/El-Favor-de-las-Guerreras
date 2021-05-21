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

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

from tensorflow.python.framework.ops import disable_eager_execution

class Entrenamiento:
##Pre procesado de datos
    
    def __init__(self):
        
        #Se deshabilita eager execution para poder usar Adam
        disable_eager_execution()
        #Eliminamos sesiones de keras abiertas
        K.clear_session()
        
        training_entrada, training_salida = self.preProcesadoDeDatos()
        print(training_entrada)
        print(training_salida)
        
        #Crear la red neuronal convolucional
        self.cnn=Sequential() #varias capas secuenciales    
        self.establecerCapas()
        self.creacionRedNeuronal(training_entrada, training_entrada)
        
    def preProcesadoDeDatos(self):
        data_entrenamiento = data.PARTIDAS_GANADAS
        cabecera = ['entrada', 'salida']
        tipos = {'entrada': 'str', 'salida': 'str'}
        
        training_data = pd.read_csv(
            data_entrenamiento,
            sep=data.SEPARADOR,
            names=cabecera,
            dtype=tipos)
        
        training_entrada = training_data.pop('entrada')
        training_entrada = self.transformarDatosEnArray(training_entrada)
        
        training_salida = training_data.pop('salida')
        training_salida = self.transformarDatosEnArray(training_salida)
        
        return training_entrada, training_salida
    
    def transformarDatosEnArray(self, datos):
        datos = np.array(datos)
        
        for i in range(datos.size):
            x = datos[i]
            datos[i] = [int(x) for x in str(x)]
            
        datos = np.array(datos)
        
        return datos
    
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
        
    def creacionRedNeuronal(self, datos_entrenamiento, datos_validacion):

        #parametros para optimizar el algoritmo
        self.cnn.compile(
                loss='categorical_crossentropy', #la funcion de perdida
                optimizer=optimizers.Adam(lr=PNN.lr), #optimizador Adam
                metrics=['accuracy'] #metrica de optimizacion, % de aprendizaje
                )
        
        self.cnn.fit_generator(
                datos_entrenamiento, #imagenes con las que va a entrenar
                steps_per_epoch=PNN.pasos, #numero de pasos por epoca
                epochs=PNN.epocas, #numero de epocas
                validation_data=datos_validacion, #imagenes de validacion
                validation_steps=PNN.pasos_validacion #cuantos pasos va a dar despues de cada epoca
                )
        
        dir='./modelo'
        
        if not os.path.exists(dir):
            os.mkdir(dir)
            
        self.cnn.save(dir+'/modelo.h5') #guardado del modelo
        self.cnn.save_weights(dir+'/pesos.h5') #guardado de los pesos del modelo
