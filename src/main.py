# -*- coding: utf-8 -*-
import sys
import os
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')


from controller.PartidaController import PartidaController
from neuralNetwork.Entrenamiento import Entrenamiento

import parameterization.ParametrosMenu as menu
import parameterization.ParametrosTablero as const

def modo_generar_datos():
    partidasGanadas1 = 0
    partidasGanadas2 = 0
    
    dir='./../data'
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = dir + "/jugadasGanadoras.csv"
    with open(path, 'w') as f:
        f.write('')
    
    for i in range(menu.NUM_SIMULACIONES):
        mainController = PartidaController('generacion')
        mainController.start()
        if(mainController.winner == const.JUGADOR1):
            partidasGanadas1 = partidasGanadas1 + 1
        else:
            partidasGanadas2 = partidasGanadas2 + 1
            
        print("Partidas ganadas por el 1: "+ str(partidasGanadas1))
        print("Partidas ganadas por el 2: "+ str(partidasGanadas2))
        print()


if __name__ == "__main__":
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        modo_generar_datos()
    
    if(menu.MODO == menu.MODO_JUGAR):
        mainController = PartidaController('jugar')
        mainController.start()
        
    if(menu.MODO == menu.MODO_ENTRENAR_RED):
        entrenamiento = Entrenamiento()

