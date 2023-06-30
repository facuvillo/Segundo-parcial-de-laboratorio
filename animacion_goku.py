import pygame

def reescalar_imagenes(lista_imagenes,tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i]= pygame.transform.scale(lista_imagenes[i],tamaño)

def girar_imganes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left + 30, principal.bottom - 50, principal.width -60, 10)
    diccionario["right"] = pygame.Rect(principal.right-2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario
goku_quieto = [pygame.image.load("Efectos e imagenes\imagenes goku\goku quieto\quieto 0.png")]

goku_caminar = [pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 0.png"),
                pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 1.png"),
                pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 2.png"),
                pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 3.png"),
                pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 4.png"),
                pygame.image.load("Efectos e imagenes\imagenes goku\goku caminar\caminar 5.png")]

goku_disparar_ki = [pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 0.png"),
                    pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 1.png"),
                    pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 2.png"),
                    pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 3.png"),
                    pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 4.png"),
                    pygame.image.load("Efectos e imagenes\imagenes goku\goku disparando ki\disparando ki 5.png")]

goku_saltar = [pygame.image.load("Efectos e imagenes\imagenes goku\goku saltar\saltar 1.png")]

goku_golpeando = [pygame.image.load("Efectos e imagenes\imagenes goku\goku golpeando\golpeando 0.png"),
                  pygame.image.load("Efectos e imagenes\imagenes goku\goku golpeando\golpeando 1.png"),
                  pygame.image.load("Efectos e imagenes\imagenes goku\goku golpeando\golpeando 2.png")]

goku_quieto_izquierda = girar_imganes(goku_quieto, True, False)

goku_caminar_izquierda = girar_imganes(goku_caminar, True, False)

goku_saltar_izquierda = girar_imganes(goku_saltar, True, False)

goku_disparar_ki_izquierda = girar_imganes(goku_disparar_ki, True, False)

goku_golpeando_izquierda = girar_imganes(goku_golpeando, True, False)
