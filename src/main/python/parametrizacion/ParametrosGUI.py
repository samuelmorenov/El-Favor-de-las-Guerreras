# -*- coding: utf-8 -*-

#Constantes de la interfaz
TAMANIO_GUERRERAS = 3

POSICION_SUS_ACCIONES = 0
POSICION_SUS_MARCADORES = 1
POSICION_GUERRERAS = 2

POSICION_GUERRERAS_ENEMIGA = POSICION_GUERRERAS+0
POSICION_GUERRERAS_NEUTRAL = POSICION_GUERRERAS+1
POSICION_GUERRERAS_ALIADA = POSICION_GUERRERAS+2

POSICION_MIS_MARCADORES = 3+TAMANIO_GUERRERAS-1
POSICION_MIS_ACCIONES = 4+TAMANIO_GUERRERAS-1
POSICION_MI_MANO = 5+TAMANIO_GUERRERAS-1
POSICION_ACCION = 6+TAMANIO_GUERRERAS-1
POSICION_ACEPTAR = 7+TAMANIO_GUERRERAS-1

#CARTA_ENORME_ALTO = 220
#CARTA_ENORME_ANCHO = 150

CARTA_GRANDE_ALTO = 145
CARTA_GRANDE_ANCHO = 100

CARTA_PEQUE_ALTO = 110
CARTA_PEQUE_ANCHO = 75

CARTA_ACCION_LADO = 110

MARCADOR_VALOR_LADO = 30

BOTON_ALTO = 1
BOTON_ANCHO = 2

BORDE_NULO = 0
BORDE_CLICKABLE = 1
BORDE_MARCADO = 2

PADDING = 2

VENTANA_ALTO=730
VENTANA_ANCHO= 810

#Textos de las acciones
TEXTO_ACCION_SECRETO = "Secreto"
TEXTO_ACCION_RENUNCIA = "Renuncia"
TEXTO_ACCION_REGALO = "Regalo"
TEXTO_ACCION_COMPETICION = "Competición"
TEXTO_PENDIENTE_REGALO = "Elija una carta entre\nlas siguientes 3"
TEXTO_PENDIENTE_COMPETICION = "Elija entre\nlas 2 primeras cartas\no las 2 ultimas"
TEXTO_POPUP_GANADO_JUGADOR_POR_11_PUNTOS = "Has ganado al conseguir 11 puntos."
TEXTO_POPUP_GANADO_JUGADOR_POR_4_FAVORES= "Has ganado al conseguir el favor de 4 guerreras."
TEXTO_POPUP_PERDIDO_JUGADOR_POR_11_PUNTOS = "Tu oponente ha ganado al conseguir 11 puntos."
TEXTO_POPUP_PERDIDO_JUGADOR_POR_4_FAVORES = "Tu oponente ha ganado al conseguir el favor de 4 guerreras."
TEXTO_POPUP_ERROR = "Se ha producido un error inesperado."
TEXTO_POPUP_CIERRE = "Se ha cerrado la ventana de forma inesperada."
