# -*- coding: utf-8 -*-
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/interface')

#from interface.UI_prompt import UI_prompt
from interface.GUI_pygame import GUI_pygame


if __name__ == "__main__":
    #prompt = UI_prompt()
    pygame = GUI_pygame()