# -*- coding: utf-8 -*-
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/interface')

from interface.UI_prompt import UI_prompt

if __name__ == "__main__":
    ui = UI_prompt()