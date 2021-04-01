# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED
from PIL import Image, ImageTk

import controller.Constantes as const

static = "static/"
activo = 'azul.png'
inactivo = 'azul_gris.png'

class GUI_Tkinter:
    def __init__(self):
        self.__window = Tk()
        self.__window.title('El Favor de las Guerreras')
        self.__window.geometry(str(const.VENTANA_ANCHO)+"x"+str(const.VENTANA_ALTO))
        #self.__window.iconbitmap('url/ico.ico')
        
        
        self.__printTablaInicial()
        self.__printAceptar()
        
    def printTabla(self, tablero):
        susAcciones = tablero[const.ACCIONES_USADAS_JUGADOR2]
        susArmas = tablero[const.ARMAS_USADAS_JUGADOR2]
        
        misArmas = tablero[const.ARMAS_USADAS_JUGADOR1]
        misAcciones = tablero[const.ACCIONES_USADAS_JUGADOR1]
        miMano = tablero[const.MANO_JUGADOR1]
        
        self.__addSusAcciones(susAcciones, 0)
        self.__addFila(susArmas, 1)
        self.__addGuerreras(2)
        self.__addFila(misArmas, 3)
        self.__addFila(misAcciones, 4)
        self.__addFila(miMano, 5)
    
    '''
    Metodos para añadir filas completas
    '''
    
    def __addFila(self, filaTablero, finaIndice):
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
        
    def __addSusAcciones(self, susAcciones, fila):
        self.__addAccion(susAcciones[const.TIPO_SECRETO], fila, 0)
        self.__addAccion(susAcciones[const.TIPO_RENUNCIA], fila, 1)
        self.__addAccion(susAcciones[const.TIPO_REGALO], fila, 2)
        self.__addAccion(susAcciones[const.TIPO_COMPETICION], fila, 3)
    '''
    Metodos para añadir objetos a las filas
    '''
    def __addAccion(self, valor, fila, columna):
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
        label = Label(self.__window, image = photo, width=ancho, height=alto)
        label.image = photo
        label.grid(row=fila, column=columna)
        
    def __addButtonConFondo(self, fila, columna, color):
        #butn = Button(frm, text="Welcome", fg="pink",activebackground = "green")
        return
    
    def __addHueco(self, fila, columna):
        label = Label(self.__window, text = " ")
        label.grid(row=fila, column=columna)
        
    def __addButton(self, fila, columna, text):
        ButtonToAdd = Button(self.__window, text = text, state=DISABLED)
        ButtonToAdd.grid(row=fila, column=columna)
    
    def __printTablaInicial(self):
        for f in range(const.NFILA):
            for c in range(const.NCOLUMNA):
                ButtonToAdd = Button(self.__window, text = " ", state=DISABLED)
                ButtonToAdd.grid(row=f, column=c)
                
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
