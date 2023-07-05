import pygame, sys
from animacion_goku import *
from pygame.locals import *
from modo import *
from class_personaje import *
from plataformas import *
from class_plataforma import *
from animaciones_enemigos import *
from class_enemigo import *
from animaciones_proyectiles import * 
from class_proyectiles import *
pygame.init()

#############################################################################

# #ACTUALIZAR LA PANTALLA
def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, diccionario_plataformas, enemigo_del_nivel_uno : Enemigo):
    pantalla.blit(fondo, (0,0))
    #plataformas
    for clave in diccionario_plataformas:
        pantalla.blit(plataforma_uno.imagen_plataforma,(diccionario_plataformas[clave]["main"].x,diccionario_plataformas[clave]["main"].y))
    
    un_personaje.update(pantalla, diccionario_plataformas)
    enemigo_del_nivel_uno.update(pantalla)

    for disparo in disparos_personaje:
        disparo.dibujar_proyectil(pantalla)

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

#PROYECTILES
# diccionario_proyectiles = {}
# diccionario_proyectiles["proyectil_enemigo_derecha"] = proyectil_enemigo
# diccionario_proyectiles["proyectil_enemigo_izquierda"] = proyectil_enemigo_izquierda
# diccionario_proyectiles["proyectil_personaje_derecha"] = proyectil_personaje
# diccionario_proyectiles["proyectil_personaje_izquierda"] = proyectil_personaje_izquierda

#PERSONAJE
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

mi_personaje = Personaje((150,195), diccionario_animaciones,(0, 690), 10)

#ENEMIGO
diccionario_enemigos = {}
diccionario_enemigos["enemigo_uno_derecha"] = enemigo_uno
diccionario_enemigos["enemigo_uno_izquierda"] = enemigo_uno_izquierda

enemigo_del_nivel_uno = Enemigo((150,195), diccionario_enemigos,(1750,700), "izquierda")

#PISO
piso = pygame.Rect(0,0,WIDTH,20)
piso.top = mi_personaje.lados["main"].bottom

lados_piso = obtener_rectangulos(piso)

#PLATAFORMA
plataforma_uno = Plataforma(imagen_plataforma_uno,(350,60),(950,600))
plataforma_dos = Plataforma(imagen_plataforma_uno,(350,60),(1550,700))

diccionario_plataformas = {}
diccionario_plataformas["piso"] = lados_piso
diccionario_plataformas["plataforma uno"] = plataforma_uno.lados
diccionario_plataformas["plataforma dos"] = plataforma_dos.lados



disparos_personaje = []

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

    for disparo in disparos_personaje:
        if disparo.x<1900 and disparo.x>0:
            disparo.x += disparo.velocidad_proyectil
        else:
            disparos_personaje.pop(disparos_personaje.index(disparo))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]) or (keys[pygame.K_UP] and keys[pygame.K_LEFT]):
        mi_personaje.direccion = "arriba"
    elif keys[pygame.K_RIGHT]: #and rectangulo_personaje.x < WIDTH - velociadad - rectangulo_personaje.width:
        mi_personaje.direccion = "derecha"
        if keys[pygame.K_e]:
            mi_personaje.que_hace = "golpear derecha"
        elif keys[pygame.K_q]:
            mi_personaje.que_hace = "disparar derecha"
            if len(disparos_personaje) < 5:
                disparos_personaje.append(
                    Proyectiles(((mi_personaje.lados["main"].x + mi_personaje.lados["main"].width // 2),mi_personaje.lados["main"].y),1,50,6,(0,0,0)))
        else:
            mi_personaje.que_hace = "caminar derecha"
    elif keys[pygame.K_LEFT]: #and (mi_personaje.lados["main"].x > WIDTH - mi_personaje.velocidad - mi_personaje.ancho):
        mi_personaje.direccion = "izquierda"
        if keys[pygame.K_e]:
            mi_personaje.que_hace = "golpear izquierda"
        elif keys[pygame.K_q]:
            mi_personaje.que_hace = "disparar izquierda"
        else:
            mi_personaje.que_hace = "caminar izquierda"
    else:
        mi_personaje.direccion = "quieto"
    

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, diccionario_plataformas, enemigo_del_nivel_uno)

    if get_modo() == True:
        pygame.draw.rect(PANTALLA, "Blue", piso, 2)
        pygame.draw.rect(PANTALLA, "Green", mi_personaje.lados["main"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma uno"]["top"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma uno"]["main"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma dos"]["top"], 2)
        pygame.draw.rect(PANTALLA, "Orange", diccionario_plataformas["plataforma dos"]["main"], 2)
        pygame.draw.rect(PANTALLA, "Blue", enemigo_del_nivel_uno.lados["main"], 2)
        pygame.draw.rect(PANTALLA, "Pink", mi_personaje.lados["bottom"], 2)


    pygame.display.update()

