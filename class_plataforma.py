import pygame
from animacion_goku import obtener_rectangulos

class Plataforma:
    def __init__(self, plataforma, posicion:tuple):
        self.imagen_plataforma = plataforma
        rectangulos_plataforma = self.imagen_plataforma.get_rect()
        rectangulos_plataforma.x = posicion[0]
        rectangulos_plataforma.y = posicion[1]
        self.lados = obtener_rectangulos(rectangulos_plataforma)
