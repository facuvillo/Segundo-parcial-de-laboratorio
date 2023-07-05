import pygame
from animacion_goku import girar_imganes

proyectil_enemigo = [pygame.image.load("Efectos e imagenes\proyectiles\proyectil enemigo 0.png"),
                     pygame.image.load("Efectos e imagenes\proyectiles\proyectil enemigo 1.png"),
                     pygame.image.load("Efectos e imagenes\proyectiles\proyectil enemigo 2.png")]

proyectil_personaje = [pygame.image.load("Efectos e imagenes\proyectiles\proyectil goku 0.png"),
                       pygame.image.load("Efectos e imagenes\proyectiles\proyectil goku 1.png"),
                       pygame.image.load("Efectos e imagenes\proyectiles\proyectil goku 2.png"),]

proyectil_enemigo_izquierda = girar_imganes(proyectil_enemigo, True, True)

proyectil_personaje_izquierda = girar_imganes(proyectil_personaje, True, True)

diccionario_proyectiles = {}
diccionario_proyectiles["proyectil_enemigo_derecha"] = proyectil_enemigo
diccionario_proyectiles["proyectil_enemigo_izquierda"] = proyectil_enemigo_izquierda
diccionario_proyectiles["proyectil_personaje_derecha"] = proyectil_personaje
diccionario_proyectiles["proyectil_personaje_izquierda"] = proyectil_personaje_izquierda