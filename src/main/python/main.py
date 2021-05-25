# -*- coding: utf-8 -*-

from controller.PartidaController import PartidaController
from training.Entrenamiento import Entrenamiento
from controller.DataGeneratorController import DataGeneratorController

import parameterization.ParametrosMenu as menu

if __name__ == "__main__":
    if(menu.MODO == menu.MODO_GENERAR_DATOS):
        main = DataGeneratorController()
    
    if(menu.MODO == menu.MODO_JUGAR):
        main = PartidaController()
        
    if(menu.MODO == menu.MODO_ENTRENAR_RED):
        main = Entrenamiento()
