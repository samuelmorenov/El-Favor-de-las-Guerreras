# -*- coding: utf-8 -*-

import pygame
import os

WIDTH, HEIGHT = 900, 700
CARTAS_SIZE =(80, 120)

BACKGROUND_COLOR = (196, 164, 149)

GUERRERA1_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera1.png'))
GUERRERA2_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera2.png'))
GUERRERA3_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera3.png'))
GUERRERA4_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera4.png'))
GUERRERA5_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera5.png'))
GUERRERA6_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera6.png'))
GUERRERA7_IMAGEN = pygame.image.load(os.path.join('static', 'guerrera7.png'))

GUERRERA1 = pygame.transform.scale(GUERRERA1_IMAGEN, CARTAS_SIZE)
GUERRERA2 = pygame.transform.scale(GUERRERA2_IMAGEN, CARTAS_SIZE)
GUERRERA3 = pygame.transform.scale(GUERRERA3_IMAGEN, CARTAS_SIZE)
GUERRERA4 = pygame.transform.scale(GUERRERA4_IMAGEN, CARTAS_SIZE)
GUERRERA5 = pygame.transform.scale(GUERRERA5_IMAGEN, CARTAS_SIZE)
GUERRERA6 = pygame.transform.scale(GUERRERA6_IMAGEN, CARTAS_SIZE)
GUERRERA7 = pygame.transform.scale(GUERRERA7_IMAGEN, CARTAS_SIZE)

FPS = 60

class GUI_pygame:
    def __init__(self):
        self.Window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("El Favor de las Guerreras")
        return

    def draw_window(self):
        self.Window.fill(BACKGROUND_COLOR)
        self.Window.blit(GUERRERA1, (100, 250))
        self.Window.blit(GUERRERA2, (200, 250))
        self.Window.blit(GUERRERA3, (300, 250))
        self.Window.blit(GUERRERA4, (400, 250))
        self.Window.blit(GUERRERA5, (500, 250))
        self.Window.blit(GUERRERA6, (600, 250))
        self.Window.blit(GUERRERA7, (700, 250))
        pygame.display.update()
    
    def start(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                #Para cerrar el juego, comprobamos si el usuario ha cerrado la ventana
                if( event.type == pygame.QUIT):
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    print("clicked x= "+str(x)+", y = "+str(y))
                    
            self.draw_window()        
            
        pygame.quit()
