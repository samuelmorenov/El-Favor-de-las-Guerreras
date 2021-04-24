# -*- coding: utf-8 -*-

import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')

import controller.Constantes as const

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
        #disable_eager_execution()
        #Eliminamos sesiones de keras abiertas
        #K.clear_session()
        
        
        training_entrada, training_salida = self.preProcesadoDeDatos()
        
        print(training_entrada)
        print(training_salida)
        
    def preProcesadoDeDatos(self):
        data_entrenamiento = './../../data/jugadasGanadoras.csv'
        separador = const.SEPARADOR
        cabecera = ['entrada', 'salida']
        tipos = {'entrada': 'str', 'salida': 'str'}
        
        training_data = pd.read_csv(
            data_entrenamiento,
            sep=separador,
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
    
    def creacionRedNeuronal(self, datos_entrenamiento, datos_validacion):
        #Parametros de la red neuronal

        #Numero de veces de iteracion sobre el set de datos completo
        epocas=20
        #Numero de veces que se va a procesar la informacion en cada epoca
        pasos=1000
        pasos_validacion=200
        
        #Tamaño de los datos
        altura, longitud = const.NFILA, const.NCOLUMNA
        
        #Numero de filtros que se van a aplicar en cada convolucion 
        #(profundidad de los datos al aplicar el filtro)
        filtrosConv1=32
        filtrosConv2=64
        
        #Altura y longitud de los filtros que se van a aplicar
        tamanio_filtro1=(3,3)
        tamanio_filtro2=(2,2)
        #Tamaño del filtro para el max pooling
        tamanio_pool=(2,2)
        
        #Learning Rate 
        lr=0.0005
        
        
        #Crear la red neuronal convolucional
        cnn=Sequential() #varias capas secuenciales
        
        #Primera capa de convolucion
        cnn.add(Convolution2D( 
                filtrosConv1, 
                tamanio_filtro1, 
                padding='same', #lo que va a hacer el filtro en las esquinas
                input_shape=(altura, longitud, 1), #altura, longitud y rgb
                activation='relu'
                ))
        
        #Primera capa de pooling
        cnn.add(MaxPooling2D(
                pool_size=tamanio_pool
                ))
        
        #Siguiente capa de convolucion
        cnn.add(Convolution2D( 
                filtrosConv2, 
                tamanio_filtro2, 
                padding='same', #lo que va a hacer el filtro en las esquinas
                activation='relu'
                ))
        
        #Siguiente capa de pooling
        cnn.add(MaxPooling2D(
                pool_size=tamanio_pool
                ))
        
        #Transformacion de la red en una dimension
        cnn.add(Flatten())
        
        #Capa densa
        cnn.add(Dense(
                256, #numero de neuronas
                activation='relu'
                ))
        
        #Se apagaran el 50% de las neuronas para no atrofiar caminos
        cnn.add(Dropout(0.5)) 
        
        #Ultima capa
        cnn.add(Dense(
                5, #numero de neuronas de salida
                activation='softmax' #% de cada opcion
                ))
        
        #parametros para optimizar el algoritmo
        cnn.compile(
                loss='categorical_crossentropy', #la funcion de perdida
                optimizer=optimizers.Adam(lr=lr), #optimizador Adam
                metrics=['accuracy'] #metrica de optimizacion, % de aprendizaje
                )
        
        cnn.fit_generator(
                datos_entrenamiento, #imagenes con las que va a entrenar
                steps_per_epoch=pasos, #numero de pasos por epoca
                epochs=epocas, #numero de epocas
                validation_data=datos_validacion, #imagenes de validacion
                validation_steps=pasos_validacion #cuantos pasos va a dar despues de cada epoca
                )
        
        dir='./modelo'
        
        if not os.path.exists(dir):
            os.mkdir(dir)
            
        cnn.save(dir+'/modelo.h5') #guardado del modelo
        cnn.save_weights(dir+'/pesos.h5') #guardado de los pesos del modelo




entrenamiento = Entrenamiento()