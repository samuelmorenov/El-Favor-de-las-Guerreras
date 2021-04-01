# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED
from PIL import Image, ImageTk

import controller.Constantes as const
import interface.ImagesPath as ip

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
            self.__addBasicButton(finaIndice, c, filaTablero[c])
            
    def __addGuerreras(self, fila):
        self.__addCartaGrande(fila, 0, ip.G1)
        self.__addCartaGrande(fila, 1, ip.G2)
        self.__addCartaGrande(fila, 2, ip.G3)
        self.__addCartaGrande(fila, 3, ip.G4)
        self.__addCartaGrande(fila, 4, ip.G5)
        self.__addCartaGrande(fila, 5, ip.G6)
        self.__addCartaGrande(fila, 6, ip.G7)
        
    def __addSusAcciones(self, fila, acciones):
        self.__addAccion(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addAccion(fila, 1, acciones[const.TIPO_RENUNCIA])
        self.__addAccion(fila, 2, acciones[const.TIPO_REGALO])
        self.__addAccion(fila, 3, acciones[const.TIPO_COMPETICION])
        
    def __addMisAcciones(self, fila, acciones):
        self.__addAccion(fila, 0, acciones[const.TIPO_SECRETO])
        self.__addBasicButton(fila, 1, acciones[const.TIPO_SECRETO])
        
        self.__addAccion(fila, 2, acciones[const.TIPO_RENUNCIA])
        self.__addBasicButton(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addBasicButton(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        self.__addAccion(fila, 5, acciones[const.TIPO_REGALO])
        self.__addAccion(fila, 6, acciones[const.TIPO_COMPETICION])
        
    def __addArmas(self, fila, armas):
        return
    '''
    Metodos para añadir objetos a las filas
    '''
    def __addAccion(self, fila, columna, valor):
        if(valor == 0):
            self.__addLabelConImagen(fila, columna, ip.INACTIVO, const.CARTA_ANCHO, const.CARTA_ANCHO)
        else:
            self.__addLabelConImagen(fila, columna, ip.ACTIVO, const.CARTA_ANCHO, const.CARTA_ANCHO)
            
    def __addCartaGrande(self, fila, columna, path):
        self.__addLabelConImagen(fila, columna, path, const.CARTA_ALTO, const.CARTA_ANCHO)
        
        
        
        
    def __addLabelConImagen(self, fila, columna, image_path, alto, ancho):
        
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=bgcolor)
        label.image = photo
        label.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addBasicButton(self, fila, columna, text):
        self.__addButton(fila, columna, const.BOTON_ALTO, const.BOTON_ANCHO, DISABLED, text)
        
    def __addButton(self, fila, columna, alto, ancho, estado, text):
        boton = Button(
                self.__window,
                text = text,
                state=estado,
                borderwidth=const.BOTON_BORDE, 
                bg=bgcolor)
        boton.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
        
    def __addButtonConFondo(self, fila, columna, color):
        #butn = Button(frm, text="Welcome", fg="pink",activebackground = "green")
        return
    
    def __addHueco(self, fila, columna):
        label = Label(self.__window, bg=bgcolor)
        label.grid(row=fila, column=columna)
        
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
