#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from controller.BotTonto import BotTonto
from Utils import Utils

utils = Utils() 

tablero = [[1,2,4,5,5,6,7],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [1,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]


class Test(unittest.TestCase):
    
    def test_bot_accionCorrecta(self):
        bot = BotTonto("test", 0)
        accion = bot.decidirAccion(tablero)
        utils.accionCorrecta(tablero, accion)
        
if __name__ == "__main__":
    unittest.main()
