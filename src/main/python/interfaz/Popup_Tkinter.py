# -*- coding: utf-8 -*-
from tkinter import ttk

import tkinter as tk

import main.python.parametrizacion.ParametrosImagenes as ip

class Popup_Tkinter:

    def sendMensaje(self, texto):
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