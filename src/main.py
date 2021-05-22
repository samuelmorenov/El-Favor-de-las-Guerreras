# -*- coding: utf-8 -*-

from controller.PartidaController import PartidaController
from neuralNetwork.entrenamiento import Entrenamiento
from controller.DataGeneratorController import DataGeneratorController

import parameterization.ParametrosMenu as menu

if __name__ == "__main__":
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        DataGeneratorController()
    
    if(menu.MODO == menu.MODO_JUGAR):
        mainController = PartidaController('jugar')
        mainController.start()
        
    if(menu.MODO == menu.MODO_ENTRENAR_RED):
        entrenamiento = Entrenamiento()

