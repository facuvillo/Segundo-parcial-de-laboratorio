import pygame
from clases_y_animaciones.animacion_goku import girar_imganes

enemigo_uno = [pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 0.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 1.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 2.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 3.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 4.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_uno 5.png")]

enemigo_dos = [pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 0.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 1.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 2.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 3.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 4.png"),
               pygame.image.load("Efectos e imagenes\imagenes enemigos\enemigo_dos 5.png")]

enemigo_uno_izquierda = girar_imganes(enemigo_uno, True, False)
enemigo_dos_izquierda = girar_imganes(enemigo_dos, True, False)