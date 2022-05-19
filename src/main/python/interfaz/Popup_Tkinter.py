# -*- coding: utf-8 -*-
from tkinter import ttk

import tkinter as tk

import main.python.parametrizacion.ParametrosImagenes as ip
import main.python.parametrizacion.ParametrosGUI as gui

'''
Clase encargada de generar la ventana pequeña de informacion (o popup)
'''
class Popup_Tkinter:
    '''
    Metodo que construye el popup con el texto dado y un boton de aceptar 
    para cerrarlo
    '''
    def sendMensaje(self, texto):
        popup = tk.Tk()
        popup.title(gui.TEXTO_TITULO)
        popup.configure(background=gui.COLOR_FONDO)
        popup.iconbitmap(ip.ICO)
        popup.geometry("420x100")
        
        label = ttk.Label(popup,background=gui.COLOR_FONDO,text = texto+"\n\n")
        label.pack()
        B1 = ttk.Button(popup, text="Aceptar", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        
