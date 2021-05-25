# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import parameterization.ParametrosTablero as const

"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""

#Parametros de la red neuronal

#Numero de veces de iteracion sobre el set de datos completo
epocas=20
#Numero de veces que se va a procesar la informacion en cada epoca
pasos=1000
pasos_validacion=200

#Tamaño de los datos de entrada
altura = const.NFILA
longitud = const.NCOLUMNA

#Tamaño de datos de salida
salida = 5
n_clases = 8

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
