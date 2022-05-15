# -*- coding: utf-8 -*-
import logging

from main.python.interfaz.GUI_Tkinter import GUI_Tkinter

'''
Clase controladora del jugador controlado por el usuario a traves de la 
interfaz grafica
'''
class ControladorJugador:
    '''
    Metodo constructor de la clase ControladorJugador, recibe el nombre y el numero
    para guardarlo en sus respectivos atributos. Además inicializa el atributo
    GUI que implementa la clase GUI_Tkinter.
    '''
    def __init__(self, miNombre, miNumero):
        '''Atributo miNombre: define el nombre para leerlo en los logs'''
        self.__miNombre = miNombre
        '''Atributo miNumero: define el orden del jugador, puede ser 1 o 2'''
        self.__miNumero = miNumero
        '''Atributo GUI: instancia la clase GUI_Tkinter que corresponde a la 
        interfaz grafica de usuario con la que interactuará el usuario'''
        self.__GUI = GUI_Tkinter()
        
    '''
    Metodo para generar una accion, recibe la matriz del tablero y devuelve un 
    array con una accion correcta que será seleccionada por el usuario a traves 
    del metodo __pedirAccion
    '''
    def decidirAccion(self, tablero):
        logging.info(self.__miNombre+" : Este es el tablero que me llega:\n"+str(tablero))
        salida = self.__pedirAccion(tablero)
        logging.info(self.__miNombre+" : Esta es la accion completa que realizo: "+str(salida))
        logging.info(self.__miNombre+" : ___________________________________") #Separador
        return salida
    
    '''
    Metodo para generar la accion de seleccion pendiente, recibe la matriz del 
    tablero y devuelve un array con la accion correctamente formada con las 
    cartas seleccionadas por el usuarioa traves del metodo __pedirAccion
    '''
    def decidirAccionDeSeleccion(self, tablero):
        return self.__pedirAccion(tablero)
    
    '''
    Metodo que unifica los metodos de decidirAccion y decidirAccionDeSeleccion
    en el que se llama a los metodos de printTabla, start y obtenerAccion para
    pintar el tablero en la interfaz de usuario y esperar a que el usuario 
    seleccione la accion que desee
    '''
    def __pedirAccion(self, tablero):
        self.__GUI.printTabla(tablero)
        self.__GUI.start()
        return self.__GUI.obtenerAccion()
        
    '''
    Metodo que sirve para cerrar el hilo de la interfaz gráfica
    '''
    def finish(self):
        self.__GUI.cerrar()
    
    '''
    Metodo get para el atributo de tipo string: miNombre
    '''
    def getMiNombre(self):
        return self.__miNombre
    
    '''
    Metodo get para el atributo de tipo string: miNumero
    '''
    def getMiNumero(self):
        return self.__miNumero
    
