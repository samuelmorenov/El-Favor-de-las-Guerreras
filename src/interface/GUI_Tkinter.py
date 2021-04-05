# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED, NORMAL
from PIL import Image, ImageTk

import controller.Constantes as const
import interface.ImagesPath as ip
import numpy as np

bgcolor = '#c4a495'
desactivado = DISABLED
activado = NORMAL

class GUI_Tkinter:
    def __init__(self):
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        self.__window = Tk()
        self.__window.title('El Favor de las Guerreras')
        self.__window.geometry(str(const.VENTANA_ANCHO)+"x"+str(const.VENTANA_ALTO))
        self.__window.configure(background=bgcolor)
        self.__window.iconbitmap(ip.ICO)
        
    def printTabla(self, tablero):
        
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
    
    def __limpiarAccion(self):
        #Borrado de la accion anterior si existiera
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        
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
        self.__addAccionEnemiga(fila, 0, acciones[const.TIPO_SECRETO], const.TIPO_SECRETO)
        self.__addCartaOculta(fila, 1, acciones[const.TIPO_SECRETO])
        
        self.__addAccionEnemiga(fila, 2, acciones[const.TIPO_RENUNCIA], const.TIPO_RENUNCIA)
        self.__addCartaOculta(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addCartaOculta(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        
        self.__addAccionEnemiga(fila, 5, acciones[const.TIPO_REGALO], const.TIPO_REGALO)
        self.__addAccionEnemiga(fila, 6, acciones[const.TIPO_COMPETICION], const.TIPO_COMPETICION)
        
    def __addMisAcciones(self, fila, acciones):
        self.__addAccionPropia(fila, 0, acciones, const.TIPO_SECRETO)
        self.__addCartaPeque(fila, 1, acciones[const.TIPO_SECRETO], 'inactivo')
        
        self.__addAccionPropia(fila, 2, acciones, const.TIPO_RENUNCIA)
        self.__addCartaPeque(fila, 3, acciones[const.TIPO_RENUNCIA_1], 'inactivo')
        self.__addCartaPeque(fila, 4, acciones[const.TIPO_RENUNCIA_2], 'inactivo')
        
        self.__addAccionPropia(fila, 5, acciones, const.TIPO_REGALO)
        
        self.__addAccionPropia(fila, 6, acciones, const.TIPO_COMPETICION)
        
    def __addMiMano(self, finaIndice, cartas):
        for c in range(const.NCOLUMNA):
            self.__addCartaPeque(finaIndice, c, cartas[c], 'activo')
            
    def __addAccionSeleccionada(self, fila):
        lado = const.CARTA_ACCION_LADO
        borde = const.BORDE_NULO
        texto = str(self.__accionGuardada[0]) #TODO: Cambiar
        columna = 0
        self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_MARCADA)
            
    '''
    Metodos para añadir objetos a las filas
    '''
    #Metodo para añadir una imagen de carta grande
    def __addCartaGrande(self, fila, columna, path):
        alto = const.CARTA_GRANDE_ALTO
        ancho = const.CARTA_GRANDE_ANCHO
        borde = const.BORDE_NULO
        self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
        
    #Metodo para añadir marcadores
    def __addMarcador(self, fila, columna, texto):
        borde = const.BORDE_MARCADO
        self.__addButtonConTexto(fila, columna, borde, texto)
        
    #Metodo para añadir un boton de accion activa/inactiva dependiendo del valor
    def __addAccionPropia(self, fila, columna, accionesLista, tipo):
        lado = const.CARTA_ACCION_LADO
        texto = str(tipo) #TODO: Cambiar
        if(accionesLista[tipo] != 0):
            borde = const.BORDE_NULO
            accion = lambda: self.__noAccion()
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_USADA)
        else:
            borde = const.BORDE_CLICKABLE
            accion = lambda: self.__seleccionarAccion(accionesLista, tipo)
            self.__addBotonConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_NO_USADA, accion)
            
    #Metodo para añadir una imagen de accion realizada/norealizada
    def __addAccionEnemiga(self, fila, columna, valor, tipo):
        lado = const.CARTA_ACCION_LADO
        borde = const.BORDE_NULO
        texto = str(tipo) #TODO: Cambiar
        if(valor == 0):
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_ENEMIGA_USADA)
        else:
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_ENEMIGA_NO_USADA)
            
    #Metodo para añadir un boton con una carta pequeña
    def __addCartaPeque(self, fila, columna, valor, activo):
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
            if(activo == 'activo'):
                accion = lambda: self.__seleccionarCarta(valor)
                self.__addBotonConImagen(fila, columna, alto, ancho, borde, '', path, accion)
            else:
                self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
            
    #Metodo para añadir un boton con una carta pequeña oculta
    def __addCartaOculta(self, fila, columna, valor):
        if(valor != 0):
            path = ip.CO
            alto = const.CARTA_PEQUE_ALTO
            ancho = const.CARTA_PEQUE_ANCHO
            borde = const.BORDE_NULO
            self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
            
    '''
    Metodos de creacion de witgets (self, fila, columna, alto, ancho, borde, activo, texto/path)
    '''
    def __addLabelConImagen(self, fila, columna, alto, ancho, borde, texto, image_path):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        label = Label(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=bgcolor,
                      text = texto,
                      compound='center',
                      fg='black',
                      borderwidth=borde)
        label.image = photo
        label.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addBotonConImagen(self, fila, columna, alto, ancho, borde, texto, image_path, accion):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        boton = Button(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=bgcolor,
                      borderwidth=borde,
                      text = texto,
                      compound='center',
                      fg='black',
                      command = accion)
        boton.image = photo
        boton.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addButtonConTexto(self, fila, columna, borde, text):
        boton = Button(
                self.__window,
                text = text,
                state=desactivado,
                borderwidth=borde, 
                bg=bgcolor,
                #activebackground='#00ff00'
                )
        boton.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
    '''
    Metodos de accion de botones
    '''
    def __seleccionarAccion(self, accionesLista, tipo):
        self.__limpiarAccion()
        
        print("Seleccionada accion "+str(tipo))
        self.__accionGuardada[0] = str(tipo)
        self.__addAccionSeleccionada(6)
        
        
    def __seleccionarCarta(self, valor):
        print("Seleccionada carta "+str(valor))
        
    def __noAccion(self):
        return
        
        
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
