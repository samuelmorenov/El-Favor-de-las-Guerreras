# -*- coding: utf-8 -*-
import os

import parametrizacion.ParametrosDatos as data
import parametrizacion.ParametrosCNN as PCNN

import pandas as pd
import numpy as np
import tensorflow as tf

from tensorflow.python.keras.layers import Dropout, Flatten, Dense
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D, Reshape, Input
from tensorflow.python.keras import backend as K

from tensorflow.python.framework.ops import disable_eager_execution

'''
Clase encargada de utilizar los datos de entrenamiento para guardar el 
modelo entrenado.
'''
class Entrenamiento:
    '''
    Método constructor de la clase Entrenamiento, se define el atributo cnn.
    '''
    def __init__(self):
        '''Atributo cnn: Contendrá una instancia de la clase Sequential de 
        tensorflow.'''
        self.__cnn = None
        
    '''
    Método ejecutor de la clase Entrenamiento, se realiza el preprocesado de 
    datos, la creación del modelo y el entrenamiento.
    '''
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
        
    '''
    Método encargado de cargar los datos de entrenamiento desde los ficheros 
    y transformarlos en matrices y arrays que reconoce la red neuronal.
    '''
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
    
    '''
    Método encargado de instanciar el atributo cnn con la clase Sequential.
    '''
    def __creacionModelo(self):
        self.__cnn = tf.keras.Sequential()
        
    '''
    Método encargado de definir las capas y filtros que va a tener la red 
    neuronal.
    '''
    def __establecerCapas(self):
        '''Definicion de los parametros de las capas'''
        #Filtros de las capas de convolucion
        numeroFiltrosConv=56
        tamanioFiltro=(1,7)
        #Tamaño del pool
        tamanioPool=(2,2)
        
        #numero de neuronas de ampliacion
        numeroNeuronasAmpliacion = 448*4
        #numero de neuronas de salida
        numeroNeuronasCapaFinal = PCNN.salida*PCNN.n_clases
        #numero de neuronas inicial
        numeroNeuronasCapaInicial = PCNN.altura*PCNN.longitud
        
        #tamaño inicial (altura, longitud y profundidad)
        tamanioInicial = (PCNN.altura, PCNN.longitud, 1)
        #tamaño final (número de salidas, posibilidades de salidas)
        tamanioFinal = (PCNN.salida, PCNN.n_clases)
        
        #porcentaje de desactivacion
        porcentajeDeDesactivacion = 0.5
        
        '''Definicion de los tipos de capas'''
        capa_entrada = Input(shape=tamanioInicial)
        #Capa de convolucion
        capa_convolucion = Convolution2D(numeroFiltrosConv, tamanioFiltro, padding='valid', activation='relu')
        #Capa de pooling
        capa_pooling = MaxPooling2D(tamanioPool,padding='same')
        #Capa de transformacion
        capa_transformacion = Flatten()
        
        #Capa de desactivacion
        capa_desactivacion = Dropout(porcentajeDeDesactivacion)
        
        #Capa densa de empliacion
        capa_densa_ampliacion = Dense(numeroNeuronasAmpliacion, activation='relu')
        #Capa densa reinicio
        capa_densa_reinicio = Dense(numeroNeuronasCapaInicial, activation='softmax')
        #Capa densa final
        capa_densa_final = Dense(numeroNeuronasCapaFinal, activation='softmax')
        
        #Capa de reescalado reinicio
        capa_reescalado_reinicio = Reshape(tamanioInicial)
        #Capa de reescalado final
        capa_reescalado_final = Reshape(tamanioFinal)
        
        
        '''Definicion del orden de las capas'''
        #Capa 1
        self.__cnn.add(capa_entrada)
        #Capa 2
        self.__cnn.add(capa_convolucion)
        #Capa 3
        self.__cnn.add(capa_pooling)
        #Capa 4
        self.__cnn.add(capa_transformacion)
        #Capa 5
        self.__cnn.add(capa_densa_ampliacion)
        #Capa 6
        self.__cnn.add(capa_desactivacion)
        #Capa 7
        self.__cnn.add(capa_densa_reinicio)
        #Capa 8
        self.__cnn.add(capa_reescalado_reinicio)
        #Capa 9
        self.__cnn.add(capa_convolucion)
        #Capa 10
        self.__cnn.add(capa_pooling)
        #Capa 11
        self.__cnn.add(capa_transformacion)
        #Capa 12
        self.__cnn.add(capa_densa_final)
        #Capa 13
        self.__cnn.add(capa_reescalado_final)
        
    '''
    Método encargado de compilar el modelo para su entrenamiento.
    '''
    def __complileAndFit(self, entrada, salida):
        self.__cnn.compile(
                loss='sparse_categorical_crossentropy',
                optimizer=tf.optimizers.Adam(lr=PCNN.lr), #optimizador Adam
                metrics=['accuracy'] #metrica de optimizacion, % de aprendizaje
                )
        
        self.__cnn.fit(entrada, salida, epochs=PCNN.epocas)
        
    '''
    Método encargado de guardar el modelo generado con los pesos de este en 
    los archivos .h5 para su posterior carga por parte de la clase Prediccion.
    '''
    def __guardarModelo(self):
        dir=data.MODELO_DIR

        if not os.path.exists(dir):
            os.mkdir(dir)
            
        #guardado del modelo
        self.__cnn.save(data.MODELO_NOMBRE) 
        #guardado de los pesos del modelo
        self.__cnn.save_weights(data.MODELO_PESOS) 
