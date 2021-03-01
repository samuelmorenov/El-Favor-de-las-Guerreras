# -*- coding: utf-8 -*-

N_CARTAS_INICIAL = 6

N_ACCIONES = 4

JUGADOR1 = 0
JUGADOR2 = 1

#Disposicion de las filas del tablero
"""Las 7 cartas del jugador"""
MANO_JUGADOR1 = 0 
MANO_JUGADOR2 = 1

"""Acciones que ha usado cada jugador"""
ACCIONES_USADAS_JUGADOR1 = 2
ACCIONES_USADAS_JUGADOR2 = 3
"""Para cada guerrera guarda la cantidad de armas que le ha dado el jugador"""
ARMAS_USADAS_JUGADOR1 = 4
ARMAS_USADAS_JUGADOR2 = 5
"""
Para cada guerrera guarda quien se ha ganado su favor
0: Nadie
1: Jugador1
2: Jugador2
"""
FAVOR_DE_GUERRERA = 6
"""
Para las acciones 3 y 4, esta fila guarda las cartas que se muestran al adversario
En la posicion 0 el numero de la accion
Si es la accion 3:
    Se guardan las 3 cartas en las posiciones 1, 2 y3
Si es la accion 4:
    Se guarda la opcion 1 en las posiciones 1 y 2
    Se guarda la opcion 2 en las posiciones 3 y 4
"""
ACCION_PENDIENTE = 7

NFILA = 8 #Este numero depende de el numero de filas definidas arriba
NCOLUMNA = 7 #Este numero depende del numero maximo de cartas en la mano

"""
Posicion 0 guarda el secreto
Posicion 1 y 2 guarda la renuncia
Posicion 3 guarda si se ha usado el regalo
Posicion 4 guarda si se ha usado la competicion
"""
TIPO_SECRETO = 0
TIPO_RENUNCIA = 1
TIPO_RENUNCIA_1 = 1
TIPO_RENUNCIA_2 = 2
TIPO_REGALO = 3
TIPO_COMPETICION = 4

#Posicion de las acciones:
ACCION_REALIZADA = 0

ACCION_1 = 1
ACCION_1_COUNT = 1

ACCION_2_1 = 1
ACCION_2_2 = 2
ACCION_2_COUNT = 2

ACCION_3_1 = 1
ACCION_3_2 = 2
ACCION_3_3 = 3
ACCION_3_COUNT = 3

ACCION_4_1_1 = 1
ACCION_4_1_2 = 2
ACCION_4_2_1 = 3
ACCION_4_2_2 = 4
ACCION_4_COUNT = 4

ACCION_SIMPLE = 1
