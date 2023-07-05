import pygame
# from animacion_goku import reescalar_imagenes, obtener_rectangulos
# from animaciones_proyectiles import *
class Proyectiles:
    def __init__(self, posxposy, direccion, velocidad_proyectil, radio, color):
        self.contador_foto = 0
        self.direccion = direccion
        self.color = color
        # self.quien_lanza = quien_lanza
        # self.animaciones = animaciones
        # self.reescalar_animaciones()
        #Rectanculos proyectil
        # rectangulo_proyectil = self.animaciones["proyectil_enemigo_derecha"][0].get_rect()
        self.x = posxposy[0]
        self.y = posxposy[1]
        self.radio = radio
        # self.lados = obtener_rectangulos(rectangulo_proyectil)
        self.velocidad_proyectil = velocidad_proyectil * direccion
    
    def dibujar_proyectil(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x,self.y), self.radio)

    # def reescalar_animaciones(self):
    #     for clave in self.animaciones:
    #         reescalar_imagenes(self.animaciones[clave], (100,65))

    # def animar(self, pantalla, que_animaciones):
    #     animacion = self.animaciones[que_animaciones]
    #     largo = len(animacion)

    #     if self.contador_foto >= largo:
    #         self.contador_foto = 0
        
    #     pantalla.blit(animacion[self.contador_foto], self.lados["main"])
    #     self.contador_foto += 1

    # def mover_proyectil(self, velocidad_proyectil):
    #     for lado in self.lados:
    #         self.lados[lado].x += velocidad_proyectil
    
    # def update_proyectil(self, pantalla):
    #     match self.direccion:
    #         case "derecha":
    #             match self.quien_lanza:
    #                 case "enemigo":
    #                     self.animar(pantalla,"proyectil_enemigo_derecha")
    #                     self.mover_proyectil(self.velocidad_proyectil)
    #                 case "personaje":
    #                     self.animar(pantalla, "proyectil_personaje_derecha")
    #                     self.mover_proyectil(self.velocidad_proyectil)
    #         case "izquierda":
    #             match self.quien_lanza:
    #                 case "enemigo":
    #                     self.animar(pantalla,"proyectil_enemigo_izquierda")
    #                     self.mover_proyectil(self.velocidad_proyectil)
    #                 case "personaje":
    #                     self.animar(pantalla, "proyectil_personaje_izquierda")
    #                     self.mover_proyectil(self.velocidad_proyectil)
