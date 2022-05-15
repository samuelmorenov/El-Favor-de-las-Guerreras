# -*- coding: utf-8 -*-
from tkinter import ttk

import tkinter as tk

import main.python.parametrizacion.ParametrosImagenes as ip
import main.python.parametrizacion.ParametrosGUI as gui

class Popup_Tkinter:

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
        
