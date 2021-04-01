# -*- coding: utf-8 -*-
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')


from controller.PartidaController import PartidaController


if __name__ == "__main__":
    mainController = PartidaController()
    mainController.start()