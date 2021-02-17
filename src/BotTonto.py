# -*- coding: utf-8 -*-

import numpy as np

class BotTonto:
    def __init__(self, yo):
        self.__yo = yo
        
        
    def realizarAccion(self, tablero):
        print("Soy "+self.__yo+", me llega este tablero:")
        print(tablero)
        #print("Soy "+self.__yo+", realizando accion...")
        return np.zeros(2, dtype=int)