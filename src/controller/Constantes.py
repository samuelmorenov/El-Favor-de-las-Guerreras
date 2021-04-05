# -*- coding: utf-8 -*-

N_CARTAS_INICIAL = 6

N_ACCIONES = 4

NFILA = 8 #Este numero depende de el numero de filas definidas arriba
NCOLUMNA = 7 #Este numero depende del numero maximo de cartas en la mano

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
TIPO_DECISION_REGALO = 5
TIPO_DECISION_COMPETICION = 6

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

#Posicion de accion pendiente
PENDIENTE_TIPO = 0

PENDIENTE_5_1 = 1
PENDIENTE_5_2 = 2
PENDIENTE_5_3 = 3
PENDIENTE_5_COUNT = 3

PENDIENTE_6_1_1 = 1
PENDIENTE_6_1_2 = 2
PENDIENTE_6_2_1 = 3
PENDIENTE_6_2_2 = 4
PENDIENTE_6_COUNT = 4

PENDIENTE_5_ELEGIDA = 1

PENDIENTE_6_ELEGIDA_1 = 1
PENDIENTE_6_ELEGIDA_2 = 2

"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
#Constantes de la interfaz

#CARTA_ENORME_ALTO = 220
#CARTA_ENORME_ANCHO = 150

CARTA_GRANDE_ALTO = 145
CARTA_GRANDE_ANCHO = 100

CARTA_PEQUE_ALTO = 110
CARTA_PEQUE_ANCHO = 75

CARTA_ACCION_LADO = 110

BOTON_ALTO = 1
BOTON_ANCHO = 2

BORDE_NULO = 0
BORDE_CLICKABLE = 1
BORDE_MARCADO = 2

PADDING = 2

VENTANA_ALTO=660
VENTANA_ANCHO= 810
