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


class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo,lista_enemigos, lista_monedas):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.lista_enemigos = lista_enemigos
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo
        self.monedas = lista_monedas
    
    def update(self, lista_enventos):
        for evento in lista_enventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()


        self.leer_inputs()
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self._slave.blit(self.imagen_fondo, (0, 0))
        # plataformas
        for clave in self.plataformas:
            self._slave.blit(imagen_plataforma_uno, (self.plataformas[clave]["main"].x, self.plataformas[clave]["main"].y))

        for moneda_dict in self.monedas:
            for clave_moneda, moneda_rect in moneda_dict.items():
                if clave_moneda == "main":
                    self._slave.blit(animacion_moneda, (moneda_rect.x, moneda_rect.y))

        self.jugador.update(self._slave, self.plataformas, self.lista_enemigos)

        for clave in self.lista_enemigos:
            self.lista_enemigos[clave].update(self._slave)
        
        for moneda_dict in self.monedas:
            moneda_rect = moneda_dict["top"]
            if self.jugador.lados["main"].colliderect(moneda_rect):
                self.monedas.remove(moneda_dict)
    
    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]) or (keys[pygame.K_UP] and keys[pygame.K_LEFT]):
            self.jugador.direccion = "arriba"
        elif keys[pygame.K_RIGHT]:
            self.jugador.direccion = "derecha"
            if keys[pygame.K_q]:
                self.jugador.que_hace = "disparar derecha"
            else:
                self.jugador.que_hace = "caminar derecha"
        elif keys[pygame.K_LEFT]:
            self.jugador.direccion = "izquierda"
            if keys[pygame.K_q]:
                self.jugador.que_hace = "disparar izquierda"

            else:
                self.jugador.que_hace = "caminar izquierda"
        else:
            self.jugador.direccion = "quieto"

    def dibujar_rectangulos(self):
        if get_modo() == True:
            pygame.draw.rect(self._slave, "Green", self.jugador.lados["main"], 2)
            for clave in self.plataformas:
                pygame.draw.rect(self._slave, "Orange", self.plataformas[clave]["top"], 2)
            for clave in self.plataformas:
                pygame.draw.rect(self._slave, "Orange", self.plataformas[clave]["main"], 2)
            for clave in self.lista_enemigos:
                pygame.draw.rect(self._slave, "Blue", self.lista_enemigos[clave].lados["main"], 2)
            pygame.draw.rect(self._slave, "Pink", self.jugador.lados["bottom"], 2)
