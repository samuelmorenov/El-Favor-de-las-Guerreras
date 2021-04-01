# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED
from PIL import Image, ImageTk

import controller.Constantes as const

static = "static/"
bgcolor = '#c4a495'

class GUI_Tkinter:
    def __init__(self):
        self.__window = Tk()
        self.__window.title('El Favor de las Guerreras')
        self.__window.geometry(str(const.VENTANA_ANCHO)+"x"+str(const.VENTANA_ALTO))
        self.__window.configure(background=bgcolor)
        #self.__window.iconbitmap('url/ico.ico')
        
        self.__printTableroLimpio()
        self.__printAceptar()
        
    def printTabla(self, tablero):
        susAcciones = tablero[const.ACCIONES_USADAS_JUGADOR2]
        susArmas = tablero[const.ARMAS_USADAS_JUGADOR2]
        
        misArmas = tablero[const.ARMAS_USADAS_JUGADOR1]
        misAcciones = tablero[const.ACCIONES_USADAS_JUGADOR1]
        miMano = tablero[const.MANO_JUGADOR1]
        
        self.__addSusAcciones(0, susAcciones)
        self.__addFila(1, susArmas)
        self.__addGuerreras(2)
        self.__addFila(3, misArmas)
        self.__addMisAcciones(4, misAcciones)
        self.__addFila(5, miMano)
        
    def __printTableroLimpio(self):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                self.__addHueco(f, c)
                
    '''
    Metodos para añadir filas completas
    '''
    
    def __addFila(self, finaIndice, filaTablero):
        for c in range(const.NCOLUMNA):
            self.__addButton(finaIndice, c, filaTablero[c])
            
    def __addGuerreras(self, fila):
        self.__addCarta(fila, 0, 'guerrera1.png')
        self.__addCarta(fila, 1, 'guerrera2.png')
        self.__addCarta(fila, 2, 'guerrera3.png')
        self.__addCarta(fila, 3, 'guerrera4.png')
        self.__addCarta(fila, 4, 'guerrera5.png')
        self.__addCarta(fila, 5, 'guerrera6.png')
        self.__addCarta(fila, 6, 'guerrera7.png')
        
    def __addSusAcciones(self, fila, acciones):
        self.__addAccion(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addAccion(fila, 1, acciones[const.TIPO_RENUNCIA])
        self.__addAccion(fila, 2, acciones[const.TIPO_REGALO])
        self.__addAccion(fila, 3, acciones[const.TIPO_COMPETICION])
        
    def __addMisAcciones(self, fila, acciones):
        self.__addAccion(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addButton(fila, 1, acciones[const.TIPO_SECRETO])
        self.__addAccion(fila, 2, acciones[const.TIPO_RENUNCIA])
        self.__addButton(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addButton(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        self.__addAccion(fila, 5, acciones[const.TIPO_REGALO])
        self.__addAccion(fila, 6, acciones[const.TIPO_COMPETICION])
        
    def __addArmas(self, fila, armas):
        return
    '''
    Metodos para añadir objetos a las filas
    '''
    def __addAccion(self, fila, columna, valor):
        activo = 'azul.png'
        inactivo = 'azul_gris.png'
        if(valor == 0):
            self.__addLabelConImagen(fila, columna, inactivo, const.CARTA_ANCHO, const.CARTA_ANCHO)
        else:
            self.__addLabelConImagen(fila, columna, activo, const.CARTA_ANCHO, const.CARTA_ANCHO)
            
    def __addCarta(self, fila, columna, path):
        self.__addLabelConImagen(fila, columna, path, const.CARTA_ALTO, const.CARTA_ANCHO)
        
    def __addLabelConImagen(self, fila, columna, path, alto, ancho):
        image_path = static+path

        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.__window, image = photo, width=ancho, height=alto, borderwidth=0, bg=bgcolor)
        label.image = photo
        label.grid(row=fila, column=columna)
        
    def __addButtonConFondo(self, fila, columna, color):
        #butn = Button(frm, text="Welcome", fg="pink",activebackground = "green")
        return
    
    def __addHueco(self, fila, columna):
        label = Label(self.__window, text = " ", borderwidth=0, bg=bgcolor)
        label.grid(row=fila, column=columna)
        
    def __addButton(self, fila, columna, text):
        ButtonToAdd = Button(self.__window, text = text, state=DISABLED, borderwidth=0, bg=bgcolor)
        ButtonToAdd.grid(row=fila, column=columna)
        
    '''
    Metodos de control de loop
    '''
    
    def __printAceptar(self):
        ButtonToAdd = Button(self.__window, text = "Aceptar", command = self.__pressAceptar)
        ButtonToAdd.grid(row=const.NFILA-1, column=const.NCOLUMNA+1)
        
    def start(self):
        self.__window.mainloop()
        
    def __pressAceptar(self):
        self.__window.quit()
    
    def cerrar(self):
        self.__window.destroy()  
