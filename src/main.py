# -*- coding: utf-8 -*-
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')


from controller.PartidaController import PartidaController


if __name__ == "__main__":
    '''
    for i in range(500):
        mainController = PartidaController()
        mainController.start()
    '''
    mainController = PartidaController()
    mainController.start()