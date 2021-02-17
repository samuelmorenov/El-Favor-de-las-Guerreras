# -*- coding: utf-8 -*-

import numpy as np

class BotTonto:
    def __init__(self, yo):
        self.__yo = yo
        
        
    def realizarAccion(self, tablero):
        #TODO
        print(self.__yo + " realiza una accion")
        return np.zeros(2, dtype=int)