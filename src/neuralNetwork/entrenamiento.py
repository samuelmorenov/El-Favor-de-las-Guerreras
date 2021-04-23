# -*- coding: utf-8 -*-

import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution() #Se deshabilita eager execution para poder usar Adam

#Eliminamos sesiones de keras abiertas
K.clear_session()

#path de imagenes de entrenamiento
data_entrenamiento = './data/entrenamiento'
#path de imagenes de validacion
data_validacion = './data/validacion'

#Parametros de la red neuronal

#Numero de veces de iteracion sobre el set de datos completo
epocas=20
#Tamaño de las imagenes
altura, longitud = 100, 100
#Numero de imagenes a procesar en cada paso
batch_size=32
#Numero de veces que se va a procesar la informacion en cada epoca
pasos=1000
pasos_validacion=200

#Numero de filtros que se van a aplicar en cada convolucion 
#(profundidad de la imagen al aplicar el filtro)
filtrosConv1=32
filtrosConv2=64

#Altura y longitud de los filtros que se van a aplicar
tamanio_filtro1=(3,3)
tamanio_filtro2=(2,2)
#Tamaño del filtro para el max pooling
tamanio_pool=(2,2)

#Numero de clases (gato, perro y gorila)
clases = 3

#Learning Rate 
lr=0.0005

##Pre procesado de imagenes

entrenamiento_datagen = ImageDataGenerator(
        rescale=1./255, #para pasar de un rango de 0-255 a 0-1
        shear_range=0.3, #inclinacion de las imagenes
        zoom_range=0.3, #zoom de las imagenes
        horizontal_flip=True #inversion horizontal
        )

validation_datagen = ImageDataGenerator(
        rescale=1./255, #para pasar de un rango de 0-255 a 0-1
        )

imagen_entrenamiento = entrenamiento_datagen.flow_from_directory( #Imagenes de entrenamiento ya cargadas
        data_entrenamiento, #directorio
        target_size = (altura, longitud), #reescalado
        batch_size = batch_size, #numero de imagenes
        class_mode='categorical' #perro, gato y gorila
        )


imagen_validacion = validation_datagen.flow_from_directory( #Imagenes de validacion ya cargadas
        data_validacion, #directorio
        target_size = (altura, longitud), #reescalado
        batch_size = batch_size, #numero de imagenes
        class_mode='categorical' #perro, gato y gorila
        )

#Crear la red neuronal convolucional

cnn=Sequential() #varias capas secuenciales

#Primera capa de convolucion
cnn.add(Convolution2D( 
        filtrosConv1, 
        tamanio_filtro1, 
        padding='same', #lo que va a hacer el filtro en las esquinas
        input_shape=(altura, longitud, 3), #altura, longitud y rgb
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
        clases, #numero de neuronas
        activation='softmax' #% de cada opcion
        ))

#parametros para optimizar el algoritmo
cnn.compile(
        loss='categorical_crossentropy', #la funcion de perdida
        optimizer=optimizers.Adam(lr=lr), #optimizador Adam
        metrics=['accuracy'] #metrica de optimizacion, % de aprendizaje
        )

cnn.fit_generator(
        imagen_entrenamiento, #imagenes con las que va a entrenar
        steps_per_epoch=pasos, #numero de pasos por epoca
        epochs=epocas, #numero de epocas
        validation_data=imagen_validacion, #imagenes de validacion
        validation_steps=pasos_validacion #cuantos pasos va a dar despues de cada epoca
        )

dir='./modelo'

if not os.path.exists(dir):
    os.mkdir(dir)
    
cnn.save(dir+'/modelo.h5') #guardado del modelo
cnn.save_weights(dir+'/pesos.h5') #guardado de los pesos del modelo
