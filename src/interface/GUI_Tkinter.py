# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from tkinter import Tk, Button, Label, DISABLED, NORMAL
from PIL import Image, ImageTk

import controller.Constantes as const
import interface.ImagesPath as ip
import numpy as np

bgcolor = '#c4a495'

class GUI_Tkinter:
    def __init__(self):
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        self.__cartasRestantes = 0
        self.__accionPendiente = 0
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
        self.__addSusAcciones(const.POSICION_SUS_ACCIONES, tablero[const.ACCIONES_USADAS_JUGADOR2])
        self.__addMarcadores(const.POSICION_SUS_MARCADORES, tablero[const.ARMAS_USADAS_JUGADOR2])
        self.__addGuerreras(const.POSICION_GUERRERAS)
        self.__addMarcadores(const.POSICION_MIS_MARCADORES, tablero[const.ARMAS_USADAS_JUGADOR1])
        self.__addMisAcciones(const.POSICION_MIS_ACCIONES, tablero[const.ACCIONES_USADAS_JUGADOR1])
        self.__addMiMano(const.POSICION_MI_MANO, tablero[const.MANO_JUGADOR1])
        
        #Si hay accion pendiente cambiar el tablero para seleccionarla
        self.__comprobarAccionPendiente(tablero)
            
    
    def __limpiarAccion(self):
        #Borrado de la accion anterior si existiera
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        for label in self.__window.grid_slaves(const.POSICION_ACCION):
           label.grid_forget()
           
    def __comprobarAccionPendiente(self, tablero):
        self.__accionPendiente = tablero[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO]
        if(self.__accionPendiente != 0):
            self.__accionPendiente = 1
            self.__addAccionPendiente(const.POSICION_ACCION, tablero[const.ACCION_PENDIENTE])
            self.__bloquearAccionesNormalesYMano()

    
    def __bloquearAccionesNormalesYMano(self):
        for label in self.__window.grid_slaves(const.POSICION_MIS_ACCIONES):
            label.config(state=DISABLED)
        for label in self.__window.grid_slaves(const.POSICION_MI_MANO):
            label.config(state=DISABLED)
        
        
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
        texto = str(self.__accionGuardada[const.PENDIENTE_TIPO])
        columna = const.PENDIENTE_TIPO
        self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_MARCADA)
        
    def __addAccionPendiente(self, fila, cartas):
        
        if(cartas[const.PENDIENTE_TIPO] == const.TIPO_DECISION_REGALO):
                texto = "Elija una carta entre\nlas siguientes 3"
        if(cartas[const.PENDIENTE_TIPO] == const.TIPO_DECISION_COMPETICION):
                texto = "Elija entre\nlas 2 primeras cartas\no las 2 ultimas"
            
        lado = const.CARTA_ACCION_LADO
        borde = const.BORDE_NULO
        columna = const.POSICION_SUS_ACCIONES
        self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_MARCADA)
        
        for c in range(1, const.NCOLUMNA):
            self.__addCartaPeque(fila, c, cartas[c], 'activo')
            
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
                accion = lambda: self.__seleccionarCarta(valor, fila, columna)
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
    
    def __addLabelConSoloTexto(self, fila, columna, alto, ancho, borde, texto):
        label = Label(self.__window,
                      width=ancho,
                      height=alto,
                      bg=bgcolor,
                      text = texto,
                      compound='center',
                      fg='black',
                      borderwidth=borde)
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
                state=DISABLED,
                borderwidth=borde, 
                bg=bgcolor,
                #activebackground='#00ff00'
                )
        boton.grid(row=fila, column=columna, padx=const.PADDING, pady=const.PADDING)
    '''
    Metodos de accion de botones
    '''
    def __seleccionarAccion(self, accionesLista, tipo):
        #Eliminamos la informacion de la accion seleccionada anteriormente
        self.__limpiarAccion()
        #Borramos el boton de aceptar para que no este disponible hasta 
        #que se seleccionen las cartas
        self.__borrarAceptar()
        #Habilitamos todas las cartas de la mano para poder ser seleccionadas
        for label in self.__window.grid_slaves(const.POSICION_MI_MANO):
            label.config(state=NORMAL)
        
        switcher = {
                0: 1,
                1: 2,
                3: 3,
                4: 4,
            }
        self.__cartasRestantes = switcher.get(tipo)
        
        
        print("Seleccionada accion "+str(tipo))
        self.__accionGuardada[const.PENDIENTE_TIPO] = tipo
        self.__addAccionSeleccionada(const.POSICION_ACCION)
        
        
    def __seleccionarCarta(self, valor, fila, columna):
        print("Seleccionada carta "+str(valor))
        if(self.__cartasRestantes > 0):
            encontrada = 0
            pos = 1
            #Buscamos un hueco libre en la accion a realizar y añadimos la carta
            while (encontrada == 0):
                if(self.__accionGuardada[pos] == 0):
                    encontrada = 1
                    self.__accionGuardada[pos] = valor
                    self.__addCartaPeque(const.POSICION_ACCION, pos, valor, 'inactivo')  
                    
                    self.__cartasRestantes = self.__cartasRestantes - 1
                    if(self.__cartasRestantes == 0):
                        self.__printAceptar()
                else:
                    pos = pos + 1
        
                    
            #Bloqueamos la carta marcada
            for label in self.__window.grid_slaves(fila, columna):
                label.config(state=DISABLED)
                
    def __noAccion(self):
        return
        
        
    '''
    Metodos de control de loop
    '''
    
    def __printAceptar(self):
        ButtonToAdd = Button(self.__window, text = "Aceptar", command = self.__pressAceptar)
        ButtonToAdd.grid(row=const.NFILA-1, column=int(const.NCOLUMNA/2))
        
    def __borrarAceptar(self):
        for label in self.__window.grid_slaves(const.NFILA-1, int(const.NCOLUMNA/2)):
           label.grid_forget()
        
    def start(self):
        self.__window.mainloop()
        
    def __pressAceptar(self):
        self.__window.quit()
        
    def cerrar(self):
        self.__window.destroy()
        
    def obtenerAccion(self):
        return self.__accionGuardada
