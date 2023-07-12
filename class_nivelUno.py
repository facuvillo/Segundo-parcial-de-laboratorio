import pygame
from animacion_goku import *
from pygame.locals import *
from class_personaje import *
from plataformas import *
from class_plataforma import Plataforma
from animaciones_enemigos import *
from class_enemigo import *
from animaciones_consumibles import *
from class_monedas import Moneda
from class_niveles import Nivel

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.surface):

        WIDTH = pantalla.get_width()
        HEIGHT = pantalla.get_height()

        # FONDO
        fondo = pygame.image.load("Efectos e imagenes\mapa\mapa_fondo.png")
        fondo = pygame.transform.scale(fondo, (WIDTH,HEIGHT))

        # PERSONAJE
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

        mi_personaje = Personaje((150, 195), diccionario_animaciones, (0, 690), 10)

        # PISO
        piso = pygame.Rect(0, 0, WIDTH, 20)
        piso.top = mi_personaje.lados["main"].bottom

        lados_piso = obtener_rectangulos(piso)

        # PLATAFORMA
        plataforma_uno = Plataforma(imagen_plataforma_uno, (950, 700))
        plataforma_dos = Plataforma(imagen_plataforma_uno, (400, 550))
        plataforma_tres = Plataforma(imagen_plataforma_uno, (950, 400))
        plataforma_cuatro = Plataforma(imagen_plataforma_uno, (10, 350))
        plataforma_cinco = Plataforma(imagen_plataforma_uno, (1550, 350))

        diccionario_plataformas = {}
        diccionario_plataformas["piso"] = lados_piso
        diccionario_plataformas["plataforma uno"] = plataforma_uno.lados
        diccionario_plataformas["plataforma dos"] = plataforma_dos.lados
        diccionario_plataformas["plataforma tres"] = plataforma_tres.lados
        diccionario_plataformas["plataforma cuatro"] = plataforma_cuatro.lados
        diccionario_plataformas["plataforma cinco"] = plataforma_cinco.lados

        # ENEMIGO
        diccionario_animaciones_enemigos = {}
        diccionario_animaciones_enemigos["enemigo_uno_derecha"] = enemigo_uno
        diccionario_animaciones_enemigos["enemigo_uno_izquierda"] = enemigo_uno_izquierda

        enemigo_uno_del_nivel_uno = Enemigo((125, 165), diccionario_animaciones_enemigos,(1750, piso.y - 165), "izquierda")
        enemigo_dos_del_nivel_uno = Enemigo((125, 165), diccionario_animaciones_enemigos,(plataforma_cinco.lados["main"].x, plataforma_cuatro.lados["main"].y - 165),"izquierda")
        enemigo_tres_del_nivel_uno = Enemigo((125, 165), diccionario_animaciones_enemigos,(plataforma_cuatro.lados["main"].x + plataforma_cuatro.lados["main"].width - 125,plataforma_cuatro.lados["main"].y - 165), "derecha")

        diccionario_enemigos = {}
        diccionario_enemigos["enemigo_uno"] = enemigo_uno_del_nivel_uno
        diccionario_enemigos["enemigo_dos"] = enemigo_dos_del_nivel_uno
        diccionario_enemigos["enemigo_tres"] = enemigo_tres_del_nivel_uno

        # MONEDAS
        moneda_uno = Moneda(animacion_moneda,(plataforma_uno.lados["main"].x + plataforma_uno.lados["main"].width // 2 - 30,plataforma_uno.lados["main"].y - 90))
        moneda_dos = Moneda(animacion_moneda,(plataforma_dos.lados["main"].x + plataforma_dos.lados["main"].width // 2 - 30,plataforma_dos.lados["main"].y - 90))
        moneda_tres = Moneda(animacion_moneda,(plataforma_tres.lados["main"].x + plataforma_tres.lados["main"].width // 2 - 30,plataforma_tres.lados["main"].y - 90))
        moneda_cuatro = Moneda(animacion_moneda,(plataforma_cuatro.lados["main"].x + plataforma_cuatro.lados["main"].width // 2 - 30,plataforma_cuatro.lados["main"].y - 90))
        moneda_cinco = Moneda(animacion_moneda,(plataforma_cinco.lados["main"].x + plataforma_cinco.lados["main"].width // 2 - 30,plataforma_cinco.lados["main"].y - 90))

        lista_monedas = []
        lista_monedas.append(moneda_uno.lados)
        lista_monedas.append(moneda_dos.lados)
        lista_monedas.append(moneda_tres.lados)
        lista_monedas.append(moneda_cuatro.lados)
        lista_monedas.append(moneda_cinco.lados)

        super().__init__(pantalla, mi_personaje, diccionario_plataformas,fondo, diccionario_enemigos, lista_monedas)