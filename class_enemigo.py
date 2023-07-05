import pygame
from animacion_goku import reescalar_imagenes, obtener_rectangulos
class Enemigo:
    def __init__(self,tamaño, animaciones, posicion,direccion):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.contador_foto = 0
        self.direccion = direccion
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo_enemigo = self.animaciones["enemigo_uno_derecha"][0].get_rect()
        rectangulo_enemigo.x = posicion[0]
        rectangulo_enemigo.y = posicion[1]
        self.lados = obtener_rectangulos(rectangulo_enemigo)

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))
    
    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_foto >= largo:
            self.contador_foto = 0
        
        pantalla.blit(animacion[self.contador_foto], self.lados["main"])
        self.contador_foto += 1
    
    def update(self, pantalla):
        match self.direccion:
            case "derecha":
                self.animar(pantalla, "enemigo_uno_derecha")
            case "izquierda":
                self.animar(pantalla, "enemigo_uno_izquierda")