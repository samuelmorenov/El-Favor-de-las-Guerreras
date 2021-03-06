# -*- coding: utf-8 -*-

import pygame


WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    
    run = True
    
    while run:
        for event in pygame.event.get():
            #Para cerrar el juego, comprobamos si el usuario ha cerrado la ventana
            if( event.type == pygame.QUIT):
                run = False
                
    pygame.quit()
    
if __name__ == "__main__":
    main()