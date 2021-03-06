# -*- coding: utf-8 -*-

import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El Favor de las Guerreras")

BACKGROUND_COLOR = (196, 164, 149)

FPS = 60

def draw_window():
    WIN.fill(BACKGROUND_COLOR)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #Para cerrar el juego, comprobamos si el usuario ha cerrado la ventana
            if( event.type == pygame.QUIT):
                run = False
                
        draw_window()        
        
    pygame.quit()
    
if __name__ == "__main__":
    main()