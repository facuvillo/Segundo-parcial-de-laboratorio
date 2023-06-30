import pygame, sys
from animacion_goku import *
from pygame.locals import *
from modo import *
from class_personaje import *
from plataformas import *
from class_plataforma import *
pygame.init()

#############################################################################

# #ACTUALIZAR LA PANTALLA
def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, diccionario_plataformas):
    pantalla.blit(fondo, (0,0))
    #plataformas
    for clave in diccionario_plataformas:
        pantalla.blit(plataforma_uno.imagen_plataforma,(diccionario_plataformas[clave]["main"].x,diccionario_plataformas[clave]["main"].y))
    
    un_personaje.update(pantalla, diccionario_plataformas)

#############################################################################

WIDTH = 1900
HEIGHT = 900 
TAMAÑO_PANTALLA = (WIDTH, HEIGHT)
FPS = 15

PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Dragon ball GT")

RELOJ = pygame.time.Clock()

#FONDO
fondo =pygame.image.load("Efectos e imagenes\mapa\mapa_fondo.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#PERSONAJE
pos_inicial = (0, 690)
tamaño = (150,195)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = goku_quieto
diccionario_animaciones["quieto_izquierda"] = goku_quieto_izquierda
diccionario_animaciones["caminar_derecha"] = goku_caminar
diccionario_animaciones["caminar_izquierda"] = goku_caminar_izquierda
diccionario_animaciones["saltar_derecha"] = goku_saltar
diccionario_animaciones["saltar_izquierda"] = goku_saltar_izquierda
diccionario_animaciones["golpeando_derecha"] = goku_golpeando
diccionario_animaciones["golpeando_izquierda"] = goku_golpeando_izquierda
diccionario_animaciones["disparar_ki_derecha"] = goku_disparar_ki
diccionario_animaciones["disparar_ki_izquierda"] = goku_disparar_ki_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones,pos_inicial, 10)

# #PISO
piso = pygame.Rect(0,0,WIDTH,20)
piso.top = mi_personaje.lados["main"].bottom

lados_piso = obtener_rectangulos(piso)

#PLATAFORMA
plataforma_uno = Plataforma(imagen_plataforma_uno,(350,60),(700,600))
plataforma_dos = Plataforma(imagen_plataforma_uno,(350,60),(300,700))

diccionario_plataformas = {}
diccionario_plataformas["piso"] = lados_piso
diccionario_plataformas["plataforma uno"] = plataforma_uno.lados
diccionario_plataformas["plataforma dos"] = plataforma_dos.lados

############################       BUCLE      ################################################

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key   == pygame.K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_RIGHT]: #and rectangulo_personaje.x < WIDTH - velociadad - rectangulo_personaje.width:
        mi_personaje.direccion = "derecha"
        if keys[pygame.K_e]:
            mi_personaje.que_hace = "golpear derecha"
        elif keys[pygame.K_q]:
            mi_personaje.que_hace = "disparar derecha"
        else:
            mi_personaje.que_hace = "caminar derecha"
    elif keys[pygame.K_LEFT]: #and rectangulo_personaje.x > WIDTH + velociadad + rectangulo_personaje.width:
        mi_personaje.direccion = "izquierda"
        if keys[pygame.K_e]:
            mi_personaje.que_hace = "golpear izquierda"
        elif keys[pygame.K_q]:
            mi_personaje.que_hace = "disparar izquierda"
        else:
            mi_personaje.que_hace = "caminar izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.direccion = "arriba"
    else:
        mi_personaje.direccion = "quieto"
    

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, diccionario_plataformas)

    if get_modo() == True:
        pygame.draw.rect(PANTALLA, "Blue", piso, 2)
        pygame.draw.rect(PANTALLA, "Green", mi_personaje.lados["main"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma uno"]["top"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma uno"]["main"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma dos"]["top"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma dos"]["main"], 2)

        pygame.draw.rect(PANTALLA, "Pink", mi_personaje.lados["bottom"], 2)


    pygame.display.update()

