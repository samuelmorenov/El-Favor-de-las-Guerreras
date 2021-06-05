# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from tkinter import ttk

import tkinter as tk

import parameterization.ParametrosImagenes as ip

def sendMensaje(texto):
    bgcolor = '#c4a495'

    popup = tk.Tk()
    popup.title('El Favor de las Guerreras')
    popup.configure(background=bgcolor)
    popup.iconbitmap(ip.ICO)
    popup.geometry("400x100")
    
    label = ttk.Label(popup,background=bgcolor,text = texto+"\n\n")
    label.pack()
    B1 = ttk.Button(popup, text="Aceptar", command = popup.destroy)
    B1.pack()
    popup.mainloop()