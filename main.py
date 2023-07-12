import pygame
import sys
from clases_y_animaciones.animacion_goku import *
from pygame.locals import *
from modo import *
from clases_y_animaciones.class_personaje import *
from plataformas import *
from clases_y_animaciones.class_plataforma import *
from clases_y_animaciones.animaciones_enemigos import *
from clases_y_animaciones.class_enemigo import *
from clases_y_animaciones.animaciones_consumibles import *
from clases_y_animaciones.class_monedas import *
from clases_y_animaciones.class_nivelUno import NivelUno
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
