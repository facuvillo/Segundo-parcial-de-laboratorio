import pygame
import sys
from pygame.locals import *
from form_prueba import FormPrueba

WIDTH = 1900
HEIGHT = 900
TAMAÑO_PANTALLA = (WIDTH, HEIGHT)
FPS = 15

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA) 

form_prueba = FormPrueba(PANTALLA, 200, 100, 900, 600, "Orange", "Blue", 5, True)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    PANTALLA.fill("black")

    form_prueba.update(eventos)

    pygame.display.update()