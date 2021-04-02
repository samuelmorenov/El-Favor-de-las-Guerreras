# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED
from PIL import Image, ImageTk

import controller.Constantes as const
import interface.ImagesPath as ip
import numpy as np

bgcolor = '#c4a495'
desactivado = "disabled"
activado = "normal"

class GUI_Tkinter:
    def __init__(self):
        self.__accionARealizar = np.zeros(const.NCOLUMNA, dtype=int)
        self.__window = Tk()
        self.__window.title('El Favor de las Guerreras')
        self.__window.geometry(str(const.VENTANA_ANCHO)+"x"+str(const.VENTANA_ALTO))
        self.__window.configure(background=bgcolor)
        self.__window.iconbitmap(ip.ICO)
        
    def printTabla(self, tablero):
        #Borrado de la accion anterior si existiera
        self.__accionARealizar = np.zeros(const.NCOLUMNA, dtype=int)
        
        #Limpieza de elementos del tablero
        for label in self.__window.grid_slaves():
           label.grid_forget()
        
        #Creacion de elementos del tablero        
        self.__addSusAcciones(0, tablero[const.ACCIONES_USADAS_JUGADOR2])
        self.__addMarcadores(1, tablero[const.ARMAS_USADAS_JUGADOR2])
        self.__addGuerreras(2)
        self.__addMarcadores(3, tablero[const.ARMAS_USADAS_JUGADOR1])
        self.__addMisAcciones(4, tablero[const.ACCIONES_USADAS_JUGADOR1])
        self.__addMiMano(5, tablero[const.MANO_JUGADOR1])
        self.__printAceptar()
        
    '''
    Metodos para añadir filas completas
    '''
    
    #Añade una fila de imagenes de cartas grandes
    def __addGuerreras(self, fila):
        self.__addCartaGrande(fila, 0, ip.G1)
        self.__addCartaGrande(fila, 1, ip.G2)
        self.__addCartaGrande(fila, 2, ip.G3)
        self.__addCartaGrande(fila, 3, ip.G4)
        self.__addCartaGrande(fila, 4, ip.G5)
        self.__addCartaGrande(fila, 5, ip.G6)
        self.__addCartaGrande(fila, 6, ip.G7)
        
    #Añade una fila de marcadores dada una lista de numeros
    def __addMarcadores(self, fila, listaNumeros):
        for c in range(const.NCOLUMNA):
            self.__addMarcador(fila, c, listaNumeros[c])
            
    def __addSusAcciones(self, fila, acciones):
        self.__addAccionEnemiga(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addCartaOculta(fila, 1, acciones[const.TIPO_SECRETO])
        
        self.__addAccionEnemiga(fila, 2, acciones[const.TIPO_RENUNCIA])
        self.__addCartaOculta(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addCartaOculta(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        
        self.__addAccionEnemiga(fila, 5, acciones[const.TIPO_REGALO])
        self.__addAccionEnemiga(fila, 6, acciones[const.TIPO_COMPETICION])
        
    def __addMisAcciones(self, fila, acciones):
        self.__addAccion(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addCartaPeque(fila, 1, acciones[const.TIPO_SECRETO])
        
        self.__addAccion(fila, 2, acciones[const.TIPO_RENUNCIA])
        self.__addCartaPeque(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addCartaPeque(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        
        self.__addAccion(fila, 5, acciones[const.TIPO_REGALO])
        
        self.__addAccion(fila, 6, acciones[const.TIPO_COMPETICION])
        
    def __addMiMano(self, finaIndice, cartas):
        for c in range(const.NCOLUMNA):
            self.__addCartaPeque(finaIndice, c, cartas[c])
            
    '''
    Metodos para añadir objetos a las filas
    '''
    #Metodo para añadir una imagen de carta grande
    def __addCartaGrande(self, fila, columna, path):
        alto = const.CARTA_GRANDE_ALTO
        ancho = const.CARTA_GRANDE_ANCHO
        borde = const.BORDE_NULO
        self.__addLabelConImagen(fila, columna, alto, ancho, borde, desactivado, path)
        
    #Metodo para añadir marcadores
    def __addMarcador(self, fila, columna, texto):
        alto = const.BOTON_ALTO
        ancho = const.BOTON_ANCHO
        borde = const.BORDE_MARCADO
        self.__addButtonConTexto(fila, columna, alto, ancho, borde, desactivado, texto)
        
    #Metodo para añadir un boton de accion activa/inactiva dependiendo del valor
    def __addAccion(self, fila, columna, valor):
        lado = const.CARTA_ACCION_LADO
        if(valor == 0):
            borde = const.BORDE_NULO
            self.__addBotonConImagen(fila, columna, lado, lado, borde, desactivado, ip.INACTIVO)
        else:
            borde = const.BORDE_CLICKABLE
            self.__addBotonConImagen(fila, columna, lado, lado, borde, activado, ip.ACTIVO)
            
    #Metodo para añadir una imagen de accion realizada/norealizada
    def __addAccionEnemiga(self, fila, columna, valor):
        lado = const.CARTA_ACCION_LADO
        borde = const.BORDE_NULO
        if(valor == 0):
            self.__addLabelConImagen(fila, columna, lado, lado, borde, desactivado, ip.INACTIVO)
        else:
            self.__addLabelConImagen(fila, columna, lado, lado, borde, desactivado, ip.ACTIVO)
            
    #Metodo para añadir un boton con una carta pequeña
    def __addCartaPeque(self, fila, columna, valor):
        if(valor != 0):
            switcher = {
                1: ip.C1,
                2: ip.C2,
                3: ip.C3,
                4: ip.C4,
                5: ip.C5,
                6: ip.C6,
                7: ip.C7,
            }
            path = switcher.get(valor)
            
            alto = const.CARTA_PEQUE_ALTO
            ancho = const.CARTA_PEQUE_ANCHO
            borde = const.BORDE_CLICKABLE
            self.__addBotonConImagen(fila, columna, alto, ancho, borde, desactivado, path)
            
    #Metodo para añadir un boton con una carta pequeña oculta
    def __addCartaOculta(self, fila, columna, valor):
        if(valor != 0):
            path = ip.CO
            alto = const.CARTA_PEQUE_ALTO
            ancho = const.CARTA_PEQUE_ANCHO
            borde = const.BORDE_NULO
            self.__addBotonConImagen(fila, columna, alto, ancho, borde, desactivado, path)
            
    '''
    Metodos de creacion de witgets (self, fila, columna, alto, ancho, borde, activo, texto/path)
    '''
    def __addLabelConImagen(self, fila, columna, alto, ancho, borde, activo, image_path):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        label = Label(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=bgcolor,
                      borderwidth=borde)
        label.image = photo
        label.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addBotonConImagen(self, fila, columna, alto, ancho, borde, activo, image_path):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        label = Button(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=bgcolor,
                      borderwidth=borde)
        label.image = photo
        label.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addButtonConTexto(self, fila, columna, alto, ancho, borde, activo, text):
        boton = Button(
                self.__window,
                text = text,
                state=activo,
                borderwidth=borde, 
                bg=bgcolor,
                #activebackground='#00ff00'
                )
        boton.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    '''
    Metodos de control de loop
    '''
    
    def __printAceptar(self):
        ButtonToAdd = Button(self.__window, text = "Aceptar", command = self.__pressAceptar)
        ButtonToAdd.grid(row=const.NFILA-1, column=int(const.NCOLUMNA/2))
        
    def start(self):
        self.__window.mainloop()
        
    def __pressAceptar(self):
        self.__window.quit()
        
    def cerrar(self):
        self.__window.destroy()
