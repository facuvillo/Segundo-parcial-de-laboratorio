from animacion_goku import reescalar_imagenes, obtener_rectangulos
import pygame

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # #VARIABLES SALTO
        self.gravedad = 1.25
        self.potencia_salto = -22
        self.limite_velocidad_caida = 100
        self.esta_saltando = False
        self.desplazamiento_y = 0
        #ANIMACIONES
        self.contador_pasos = 0
        self.direccion = "derecha"
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOs
        rectangulo = self.animaciones["quieto"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, diccionario_plataformas):
        match self.direccion:
            case "derecha":
                match self.que_hace:
                    case "caminar derecha":
                        if not self.esta_saltando:
                            self.animar(pantalla,"caminar_derecha")
                        self.mover(self.velocidad)
                    case "golpear derecha":
                        if not self.esta_saltando: 
                            self.animar(pantalla,"golpeando_derecha")
                        self.mover(self.velocidad)
                    case "disparar derecha":
                        if not self.esta_saltando:
                            self.animar(pantalla,"disparar_ki_derecha")
                        self.mover(self.velocidad)
            case "izquierda":
                match self.que_hace:
                    case "caminar izquierda":
                        if not self.esta_saltando:
                            self.animar(pantalla,"caminar_izquierda")
                        self.mover(self.velocidad * -1)
                    case "golpear izquierda":
                        if not self.esta_saltando: 
                            self.animar(pantalla,"golpeando_izquierda")
                        self.mover(self.velocidad * -1)
                    case "disparar izquierda":
                        if not self.esta_saltando:
                            self.animar(pantalla,"disparar_ki_izquierda")
                        self.mover(self.velocidad * -1)
            case "arriba":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")

        self.aplicar_gravedad(pantalla, diccionario_plataformas)

    def aplicar_gravedad(self, pantalla, diccionario_plataformas):
        if self.esta_saltando:
            self.animar(pantalla,"saltar_derecha")
            
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for plataforma in diccionario_plataformas: 
            if self.lados["bottom"].colliderect(diccionario_plataformas[plataforma]["top"]):
                self.esta_saltando = False
                self.lados["main"].bottom = diccionario_plataformas[plataforma]["top"].top
                self.desplazamiento_y = 0
                break
            else:
                self.esta_saltando = True