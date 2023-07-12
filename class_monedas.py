import pygame
from animacion_goku import obtener_rectangulos

class Moneda:
    def __init__(self, moneda, posicion:tuple):
        self.imagen_moneda = moneda
        rectangulos_moneda = self.imagen_moneda.get_rect()
        rectangulos_moneda.x = posicion[0]
        rectangulos_moneda.y = posicion[1]
        self.lados = obtener_rectangulos(rectangulos_moneda)
