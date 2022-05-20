# -*- coding: utf-8 -*-
import logging

from tkinter import Tk, Button, Label, DISABLED, NORMAL
from PIL import Image, ImageTk

import main.python.parametrizacion.ParametrosTablero as const
import main.python.parametrizacion.ParametrosImagenes as ip
import main.python.parametrizacion.ParametrosGUI as gui
import numpy as np

'''
Clase encargada de generar la ventana principal de la aplicacion usando la 
libreria tkinter.
'''
class GUI_Tkinter:
    '''
    Método constructor de la clase GUI_Tkinter, se definen e inicializan todos 
    los atributos privados de la misma.
    '''
    def __init__(self):
        '''Atributo accionGuardada: Array en el que se van guardando la 
        información de la acción que se está generando.'''
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        '''Atributo cartasRestantes: El número de cartas que faltan para
        terminar de completar la acción actual.'''
        self.__cartasRestantes = 0
        '''Atributo accionPendiente: Array con la acción pendiente que llega.'''
        self.__accionPendiente = None
        '''Atributo window: Instancia la clase Tk de tkinter.'''
        self.__window = Tk()
        
        self.__window.title(gui.TEXTO_TITULO)
        self.__window.geometry(str(gui.VENTANA_ANCHO)+"x"+str(gui.VENTANA_ALTO))
        self.__window.configure(background=gui.COLOR_FONDO)
        self.__window.iconbitmap(ip.ICO)
        
    '''
    Método encargado de pintar el tablero que nos llega.
    '''
    def printTabla(self, tablero):
        #Limpieza de elementos del tablero
        for label in self.__window.grid_slaves():
           label.grid_forget()
        
        #Creacion de elementos del tablero        
        self.__addSusAcciones(gui.POSICION_SUS_ACCIONES, tablero[const.ACCIONES_USADAS_JUGADOR2])
        self.__addMarcadores(gui.POSICION_SUS_MARCADORES, tablero[const.ARMAS_USADAS_JUGADOR2])
        self.__addGuerreras(gui.POSICION_GUERRERAS, tablero[const.FAVOR_DE_GUERRERA])
        self.__addMarcadores(gui.POSICION_MIS_MARCADORES, tablero[const.ARMAS_USADAS_JUGADOR1])
        self.__addMisAcciones(gui.POSICION_MIS_ACCIONES, tablero[const.ACCIONES_USADAS_JUGADOR1])
        self.__addMiMano(gui.POSICION_MI_MANO, tablero[const.MANO_JUGADOR1])
        
        #Si hay accion pendiente cambiar el tablero para seleccionarla
        self.__comprobarAccionPendiente(tablero)
        
    '''
    Método encargado de vaciar el array de acción guardada y borrar del 
    tablero la acción que se había seleccionado.
    '''
    def __limpiarAccion(self):
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        for label in self.__window.grid_slaves(gui.POSICION_ACCION):
           label.grid_forget()
        
    '''
    Método encargado de comprobar si existe una acción pendiente y modificar 
    el tablero para que se muestre la misma.
    '''
    def __comprobarAccionPendiente(self, tablero):
        self.__accionPendiente = tablero[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO]
        if(self.__accionPendiente != 0):
            self.__accionPendiente = 1
            self.__addAccionPendiente(gui.POSICION_ACCION, tablero[const.ACCION_PENDIENTE])
            self.__bloquearAccionesNormalesYMano()
        
    '''
    Método encargado de deshabilitar todos los botones de las acciones y de
    la mano.
    '''
    def __bloquearAccionesNormalesYMano(self):
        for label in self.__window.grid_slaves(gui.POSICION_MIS_ACCIONES):
            label.config(state=DISABLED)
        for label in self.__window.grid_slaves(gui.POSICION_MI_MANO):
            label.config(state=DISABLED)
            
    
    ##### Métodos para añadir filas completas
        
    '''
    Método encargado de añadir una fila de imágenes de cartas grandes.
    '''
    def __addGuerreras(self, fila, favores):
        self.__addCartaGrande(fila, 0, ip.G1)
        self.__addCartaGrande(fila, 1, ip.G2)
        self.__addCartaGrande(fila, 2, ip.G3)
        self.__addCartaGrande(fila, 3, ip.G4)
        self.__addCartaGrande(fila, 4, ip.G5)
        self.__addCartaGrande(fila, 5, ip.G6)
        self.__addCartaGrande(fila, 6, ip.G7)
        
        switcher = {
                const.FAVOR_NEUTRAL: gui.POSICION_GUERRERAS_NEUTRAL,
                const.FAVOR_JUGADOR_1: gui.POSICION_GUERRERAS_ALIADA,
                const.FAVOR_JUGADOR_2: gui.POSICION_GUERRERAS_ENEMIGA
            }
        
        for c in range(const.NCOLUMNA):
            favor  = switcher.get(favores[c])
            self.__addMarcadorValor(favor, c, ip.MARCADOR_VALOR)
            
    '''
    Método encargado de añadir una fila de marcadores dada una lista de números.
    '''
    def __addMarcadores(self, fila, listaNumeros):
        for c in range(const.NCOLUMNA):
            self.__addMarcador(fila, c, listaNumeros[c])
            
    '''
    Método encargado de añadir una fila con las acciones usadas del adversario.
    '''
    def __addSusAcciones(self, fila, acciones):
        self.__addAccionEnemiga(fila, 0, acciones[const.TIPO_SECRETO], const.TIPO_SECRETO)
        self.__addCartaOculta(fila, 1, acciones[const.TIPO_SECRETO])
        
        self.__addAccionEnemiga(fila, 2, acciones[const.TIPO_RENUNCIA], const.TIPO_RENUNCIA)
        self.__addCartaOculta(fila, 3, acciones[const.TIPO_RENUNCIA_1])
        self.__addCartaOculta(fila, 4, acciones[const.TIPO_RENUNCIA_2])
        
        self.__addAccionEnemiga(fila, 5, acciones[const.TIPO_REGALO], const.TIPO_REGALO)
        self.__addAccionEnemiga(fila, 6, acciones[const.TIPO_COMPETICION], const.TIPO_COMPETICION)
            
    '''
    Método encargado de añadir una fila con las acciones usadas del jugador.
    '''
    def __addMisAcciones(self, fila, acciones):
        self.__addAccionPropia(fila, 0, acciones, const.TIPO_SECRETO)
        self.__addCartaPeque(fila, 1, acciones[const.TIPO_SECRETO], 'inactivo')
        
        self.__addAccionPropia(fila, 2, acciones, const.TIPO_RENUNCIA)
        self.__addCartaPeque(fila, 3, acciones[const.TIPO_RENUNCIA_1], 'inactivo')
        self.__addCartaPeque(fila, 4, acciones[const.TIPO_RENUNCIA_2], 'inactivo')
        
        self.__addAccionPropia(fila, 5, acciones, const.TIPO_REGALO)
        
        self.__addAccionPropia(fila, 6, acciones, const.TIPO_COMPETICION)
            
    '''
    Método encargado de añadir una fila con las cartas de la mano del jugador.
    '''
    def __addMiMano(self, finaIndice, cartas):
        for c in range(const.NCOLUMNA):
            self.__addCartaPeque(finaIndice, c, cartas[c], 'activo')
            
    '''
    Método encargado de añadir el label con la accion seleccionada.
    '''
    def __addAccionSeleccionada(self, fila):
        lado = gui.CARTA_ACCION_LADO
        borde = gui.BORDE_NULO
        texto = self.__getTextoAccion(self.__accionGuardada[const.PENDIENTE_TIPO])
        columna = const.PENDIENTE_TIPO
        self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_MARCADA)
            
    '''
    Método encargado de añadir las cartas de la acción pendiente.
    '''
    def __addAccionPendiente(self, fila, cartas):
        if(cartas[const.PENDIENTE_TIPO] == const.TIPO_DECISION_REGALO):
            self.__addAccionPendiente5(fila, cartas)
        if(cartas[const.PENDIENTE_TIPO] == const.TIPO_DECISION_COMPETICION):
            self.__addAccionPendiente6(fila, cartas)
            
    '''
    Método encargado de añadir las cartas de la accion pendiente para el tipo 5.
    '''
    def __addAccionPendiente5(self, fila, cartas):
        texto = gui.TEXTO_PENDIENTE_REGALO
        self.__addMarcoExplicativo(fila, gui.POSICION_SUS_ACCIONES, texto)
        
        columna1 = const.PENDIENTE_5_1
        accion = lambda: self.__seleccionarCartaPendiente5(fila, columna1, cartas[columna1])
        self.__addCartaAccionPendiente(fila, columna1, cartas[columna1], accion)
        
        columna2 = const.PENDIENTE_5_2
        accion = lambda: self.__seleccionarCartaPendiente5(fila, columna2, cartas[columna2])
        self.__addCartaAccionPendiente(fila, columna2, cartas[columna2], accion)
        
        columna3 = const.PENDIENTE_5_3
        accion = lambda: self.__seleccionarCartaPendiente5(fila, columna3, cartas[columna3])
        self.__addCartaAccionPendiente(fila, columna3, cartas[columna3], accion)
            
    '''
    Método encargado de añadir las cartas de la accion pendiente para el tipo 6.
    '''
    def __addAccionPendiente6(self, fila, cartas):
        texto = gui.TEXTO_PENDIENTE_COMPETICION
        self.__addMarcoExplicativo(fila, gui.POSICION_SUS_ACCIONES, texto)
        
        columna11 = const.PENDIENTE_6_1_1
        columna12 = const.PENDIENTE_6_1_2
        accion = lambda: self.__seleccionarCartaPendiente6(fila, columna11, columna12, cartas[columna11], cartas[columna12])
        self.__addCartaAccionPendiente(fila, columna11, cartas[columna11], accion)
        
        columna21 = const.PENDIENTE_6_1_2
        columna22 = const.PENDIENTE_6_1_1
        accion = lambda: self.__seleccionarCartaPendiente6(fila, columna21, columna22, cartas[columna21], cartas[columna22])
        self.__addCartaAccionPendiente(fila, columna21, cartas[columna21], accion)
        
        columna31 = const.PENDIENTE_6_2_1
        columna32 = const.PENDIENTE_6_2_2
        accion = lambda: self.__seleccionarCartaPendiente6(fila, columna31, columna32, cartas[columna31], cartas[columna32])
        self.__addCartaAccionPendiente(fila, columna31, cartas[columna31], accion)
        
        columna41 = const.PENDIENTE_6_2_2
        columna42 = const.PENDIENTE_6_2_1
        accion = lambda: self.__seleccionarCartaPendiente6(fila, columna41, columna42, cartas[columna41], cartas[columna42])
        self.__addCartaAccionPendiente(fila, columna41, cartas[columna41], accion)
        
    
    ##### Métodos para añadir objetos a las filas
    
    '''
    Método para añadir una imagen de carta grande en la posición dada con 
    la imagen dada.
    '''
    def __addCartaGrande(self, fila, columna, path):
        alto = gui.CARTA_GRANDE_ALTO
        ancho = gui.CARTA_GRANDE_ANCHO
        borde = gui.BORDE_NULO
        nfilas = gui.TAMANIO_GUERRERAS
        self.__addLabelConImagenYTamanioFilas(fila, columna, alto, ancho, nfilas, borde, '', path)
    
    '''
    Método para añadir el marcador del valor en la posición dada con la
    imagen dada.
    '''
    def __addMarcadorValor(self, fila, columna, path):
        alto = gui.MARCADOR_VALOR_LADO
        ancho = gui.MARCADOR_VALOR_LADO
        borde = gui.BORDE_NULO
        self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
    
    '''
    Método para añadir marcadores en la posición dada con el texto dado.
    '''
    def __addMarcador(self, fila, columna, texto):
        borde = gui.BORDE_MARCADO
        self.__addButtonConTexto(fila, columna, borde, texto)
    
    '''
    Método para añadir un botón, en la posición dada, de acción activa/inactiva
    dependiendo del tipo dado.
    '''
    def __addAccionPropia(self, fila, columna, accionesLista, tipo):
        lado = gui.CARTA_ACCION_LADO
        texto = self.__getTextoAccion(tipo)
        if(accionesLista[tipo] != 0):
            borde = gui.BORDE_NULO
            accion = lambda: self.__noAccion()
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_USADA)
        else:
            borde = gui.BORDE_CLICKABLE
            accion = lambda: self.__seleccionarAccion(tipo)
            self.__addBotonConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_PROPIA_NO_USADA, accion)
    
    '''
    Método encargado de añadir una imagen de acción realizada/no realizada en 
    la posición dada.
    '''
    def __addAccionEnemiga(self, fila, columna, valor, tipo):
        lado = gui.CARTA_ACCION_LADO
        borde = gui.BORDE_NULO
        texto = self.__getTextoAccion(tipo)
        if(valor == 0):
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_ENEMIGA_USADA)
        else:
            self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.ACCION_ENEMIGA_NO_USADA)
    
    '''
    Método encargado de seleccionar el texto para un tipo dado.
    '''
    def __getTextoAccion(self, tipo):
        switcher = {
            const.TIPO_SECRETO: gui.TEXTO_ACCION_SECRETO,
            const.TIPO_RENUNCIA: gui.TEXTO_ACCION_RENUNCIA,
            const.TIPO_REGALO: gui.TEXTO_ACCION_REGALO,
            const.TIPO_COMPETICION: gui.TEXTO_ACCION_COMPETICION
        }
        texto = switcher.get(tipo)
        return texto
    
    '''
    Método encargado de añadir un botón con una carta pequeña.
    '''
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
            
            alto = gui.CARTA_PEQUE_ALTO
            ancho = gui.CARTA_PEQUE_ANCHO
            borde = gui.BORDE_CLICKABLE
            if(activo == 'activo'):
                accion = lambda: self.__seleccionarCarta(valor, fila, columna)
                self.__addBotonConImagen(fila, columna, alto, ancho, borde, '', path, accion)
            else:
                self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
    
    '''
    Método encargado de añadir un boton de una carta de accion pendiente.
    '''
    def __addCartaAccionPendiente(self, fila, columna, valor, accion):
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
            
            alto = gui.CARTA_PEQUE_ALTO
            ancho = gui.CARTA_PEQUE_ANCHO
            borde = gui.BORDE_CLICKABLE
            self.__addBotonConImagen(fila, columna, alto, ancho, borde, '', path, accion)
    
    '''
    Método encargado de añadir un botón con una carta oculta.
    '''
    def __addCartaOculta(self, fila, columna, valor):
        if(valor != 0):
            path = ip.CO
            alto = gui.CARTA_PEQUE_ALTO
            ancho = gui.CARTA_PEQUE_ANCHO
            borde = gui.BORDE_NULO
            self.__addLabelConImagen(fila, columna, alto, ancho, borde, '', path)
    
    '''
    Método encargado de añadir un boton con una carta oculta.
    '''
    def __addMarcoExplicativo(self, fila, columna, texto):
        lado = gui.CARTA_ACCION_LADO
        borde = gui.BORDE_NULO
        self.__addLabelConImagen(fila, columna, lado, lado, borde, texto, ip.MARCO_TEXTO_EXPLICATIVO)
        
    
    ##### Métodos de creacion de witgets
    
    '''
    Método encargado de añadir un label con una imagen para una posición, con 
    un tamaño, imagen, texto y borde dados y numero de filas = 1.
    '''
    def __addLabelConImagen(self, fila, columna, alto, ancho, borde, texto, image_path):
        nfilas = 1
        self.__addLabelConImagenYTamanioFilas(fila, columna, alto, ancho, nfilas, borde, texto, image_path)
    
    '''
    Método encargado de añadir un label con una imagen para una posición, con
    un tamaño, imagen, texto, numero de filas y borde dados.
    '''
    def __addLabelConImagenYTamanioFilas(self, fila, columna, alto, ancho, nfilas, borde, texto, image_path):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        label = Label(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=gui.COLOR_FONDO,
                      text = texto,
                      compound='center',
                      fg='black',
                      borderwidth=borde)
        label.image = photo
        label.grid(row=fila, column=columna, padx=gui.PADDING, rowspan = nfilas, pady=gui.PADDING)
    
    '''
    Método encargado de añadir un label in imagen para una posición, con un 
    tamaño, texto y borde dados.
    '''
    def __addLabelConSoloTexto(self, fila, columna, alto, ancho, borde, texto):
        label = Label(self.__window,
                      width=ancho,
                      height=alto,
                      bg=gui.COLOR_FONDO,
                      text = texto,
                      compound='center',
                      fg='black',
                      borderwidth=borde)
        label.grid(row=fila, column=columna, padx=gui.PADDING, pady=gui.PADDING)
    
    '''
    Método encargado de añadir un botón con una imagen para una posición, con 
    un tamaño, imagen, texto, numero de filas y borde dados.
    '''
    def __addBotonConImagen(self, fila, columna, alto, ancho, borde, texto, image_path, accion):
        image = Image.open(image_path)
        image = image.resize((ancho, alto), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        
        boton = Button(self.__window,
                      image = photo,
                      width=ancho,
                      height=alto,
                      bg=gui.COLOR_FONDO,
                      borderwidth=borde,
                      text = texto,
                      compound='center',
                      fg='black',
                      command = accion)
        boton.image = photo
        boton.grid(row=fila, column=columna, padx=gui.PADDING, pady=gui.PADDING)
    
    '''
    Método encargado de añadir un botón con un texto para una posición, con una
    imagen, texto y borde dados.
    '''
    def __addButtonConTexto(self, fila, columna, borde, text):
        boton = Button(
                self.__window,
                text = text,
                state=DISABLED,
                borderwidth=borde, 
                bg=gui.COLOR_FONDO,
                #activebackground='#00ff00'
                )
        boton.grid(row=fila, column=columna, padx=gui.PADDING, pady=gui.PADDING)
        
    
    ##### Métodos de accion de botones
    
    '''
    Método que se ejecuta al dar a un botón de selección de acción. Elimina la
    acción anteriormente seleccionada y pinta la nueva para poder seleccionar
    las cartas correspondientes.
    '''
    def __seleccionarAccion(self, tipo):
        #Eliminamos la informacion de la accion seleccionada anteriormente
        self.__limpiarAccion()
        #Borramos el boton de aceptar para que no este disponible hasta 
        #que se seleccionen las cartas
        self.__borrarAceptar()
        #Habilitamos todas las cartas de la mano para poder ser seleccionadas
        for label in self.__window.grid_slaves(gui.POSICION_MI_MANO):
            label.config(state=NORMAL)
        
        switcher = {
                0: 1,
                1: 2,
                3: 3,
                4: 4,
            }
        self.__cartasRestantes = switcher.get(tipo)
        
        
        logging.info("GUI : Seleccionada accion "+str(tipo))
        self.__accionGuardada[const.PENDIENTE_TIPO] = tipo
        self.__addAccionSeleccionada(gui.POSICION_ACCION)
        
    '''
    Método que se ejecuta al seleccionar una carta, en caso de que la acción 
    admita una nueva carta pinta la carta seleccionada en la sección de la 
    acción seleccionada y bloquea la carta de la mano.
    '''
    def __seleccionarCarta(self, valor, fila, columna):
        logging.info("GUI : Seleccionada carta "+str(valor))
        if(self.__cartasRestantes > 0):
            encontrada = 0
            pos = 1
            #Buscamos un hueco libre en la accion a realizar y añadimos la carta
            while (encontrada == 0):
                if(self.__accionGuardada[pos] == 0):
                    encontrada = 1
                    self.__accionGuardada[pos] = valor
                    self.__addCartaPeque(gui.POSICION_ACCION, pos, valor, 'inactivo')  
                    
                    self.__cartasRestantes = self.__cartasRestantes - 1
                    if(self.__cartasRestantes == 0):
                        self.__printAceptar()
                else:
                    pos = pos + 1
        
                    
            #Bloqueamos la carta marcada
            for label in self.__window.grid_slaves(fila, columna):
                label.config(state=DISABLED)
                
    '''
    Método que se ejecuta al seleccionar una carta cuando esta la acción de 
    selección pendiente de tipo 5.
    '''
    def __seleccionarCartaPendiente5(self, fila, columna, valor):
        logging.info("GUI : Seleccionada carta para accion pendiente "+str(valor))
        #Eliminamos la informacion de la accion seleccionada anteriormente
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        self.__accionGuardada[const.PENDIENTE_TIPO] = const.TIPO_DECISION_REGALO
        self.__accionGuardada[const.PENDIENTE_5_ELEGIDA] = valor
        
        #Desbloqueamos todas las cartas de accion pendiente
        for label in self.__window.grid_slaves(fila):
            label.config(state=NORMAL)
            
        #Bloqueamos la carta seleccionada
        for label in self.__window.grid_slaves(fila, columna):
            label.config(state=DISABLED)
            
        #Volvemos a pintar el boton de aceptar
        self.__borrarAceptar()
        self.__printAceptar()
        
    '''
    Método que se ejecuta al seleccionar una carta cuando esta la acción de 
    selección pendiente de tipo 6.
    '''
    def __seleccionarCartaPendiente6(self, fila, columna1, columna2, valor1, valor2):
        logging.info("GUI : Seleccionada cartas para accion pendiente "+str(valor1)+" y "+str(valor2))
        #Eliminamos la informacion de la accion seleccionada anteriormente
        self.__accionGuardada = np.zeros(const.NCOLUMNA, dtype=int)
        self.__accionGuardada[const.PENDIENTE_TIPO] = const.TIPO_DECISION_COMPETICION
        self.__accionGuardada[const.PENDIENTE_6_ELEGIDA_1] = valor1
        self.__accionGuardada[const.PENDIENTE_6_ELEGIDA_2] = valor2
        
        #Desbloqueamos todas las cartas de accion pendiente
        for label in self.__window.grid_slaves(fila):
            label.config(state=NORMAL)
            
        #Bloqueamos las cartas seleccionadas
        for label in self.__window.grid_slaves(fila, columna1):
            label.config(state=DISABLED)
        for label in self.__window.grid_slaves(fila, columna2):
            label.config(state=DISABLED)
            
        #Volvemos a pintar el boton de aceptar
        self.__borrarAceptar()
        self.__printAceptar()
                
    '''
    Método auxiliar para no hacer nada al pulsar acciones que no están disponibles.
    '''
    def __noAccion(self):
        return
    
    
    ##### Métodos de control de loop
                
    '''
    Método que pinta el boton de aceptar para enviar la accion seleccionada.
    '''
    def __printAceptar(self):
        ButtonToAdd = Button(self.__window, text = "Aceptar", command = self.__pressAceptar)
        ButtonToAdd.grid(row=gui.POSICION_ACEPTAR, column=int(const.NCOLUMNA/2))
        
    '''
    Método que borra el botón de aceptar para que no se envíe una acción a medias.
    '''
    def __borrarAceptar(self):
        for label in self.__window.grid_slaves(gui.POSICION_ACEPTAR, int(const.NCOLUMNA/2)):
           label.grid_forget()
           
    '''
    Método que inicia el bucle de tkinter.
    '''
    def start(self):
        self.__window.mainloop()
        
           
    '''
    Método sale del bucle de tkinter para poder seguir con la ejecucion del 
    programa y aplicar la accion seleccionada.
    '''
    def __pressAceptar(self):
        self.__window.quit()
        
    '''
    Método que destruye la ventana de tkinter cuando se termina la partida.
    '''
    def cerrar(self):
        self.__window.destroy()
        
    '''
    Método que devuelve el atributo de accionGuardada.
    '''
    def obtenerAccion(self):
        return self.__accionGuardada
