import pygame
import sys
from animacion_goku import *
from pygame.locals import *
from modo import *
from class_personaje import *
from plataformas import *
from class_plataforma import *
from animaciones_enemigos import *
from class_enemigo import *
from animaciones_consumibles import *
from class_monedas import *
from class_nivelUno import NivelUno
from form_prueba import FormPrueba

WIDTH = 1900
HEIGHT = 900
TAMAÑO_PANTALLA = (WIDTH, HEIGHT)
FPS = 15

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Dragon ball GT")
formulario_principal = FormPrueba(PANTALLA,0,0,1900,900,"Gold", "Magenta", 5, True)

# nivel_actual = NivelUno(PANTALLA)

############################       BUCLE      ################################################

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    formulario_principal.update(eventos)


    pygame.display.update()
