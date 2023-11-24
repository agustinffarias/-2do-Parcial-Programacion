import pygame
from constantes import *
# Función para reescalar imágenes en un diccionario de animaciones

def obtener_rectangulos(rectangulo:pygame.Rect, width:int, height:int):
        diccionario = {}
        if len(rectangulo) > 0 and isinstance(rectangulo, pygame.Rect):

            diccionario["principal"] = rectangulo
            diccionario["bottom"] = pygame.Rect(rectangulo.left, rectangulo.bottom - 12, rectangulo.width, height * 0.20)
            diccionario["right"] = pygame.Rect(rectangulo.right - 10, rectangulo.top, 10, rectangulo.height)
            diccionario["left"] = pygame.Rect(rectangulo.left, rectangulo.top, 10, rectangulo.height)
            diccionario["top"] = pygame.Rect(rectangulo.left, rectangulo.top , rectangulo.width, 12)
        return diccionario
    
def reescalar_imagenes(diccionario_animaciones, ancho, alto):

    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            # Obtener la imagen en el índice actual
            img = diccionario_animaciones[clave][i]
            # Reescalar la imagen al tamaño especificado
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

def obtener_rectangulos(rectangulo:pygame.Rect, width:int, height:int):
        diccionario = {}
        if len(rectangulo) > 0 and isinstance(rectangulo, pygame.Rect):

            diccionario["principal"] = rectangulo
            diccionario["bottom"] = pygame.Rect(rectangulo.left, rectangulo.bottom - 12, rectangulo.width, height * 0.20)
            diccionario["right"] = pygame.Rect(rectangulo.right - 10, rectangulo.top, 10, rectangulo.height)
            diccionario["left"] = pygame.Rect(rectangulo.left, rectangulo.top, 10, rectangulo.height)
            diccionario["top"] = pygame.Rect(rectangulo.left, rectangulo.top , rectangulo.width, 12)

        return diccionario

# Función para invertir horizontalmente una lista de imágenes
def invertir_imagen(lista: list) -> list:
    lista_transformada = []
    for i in range(len(lista)):
        # Obtener la imagen en el índice actual
        img = lista[i]
        # Invertir horizontalmente la imagen y agregarla a la lista transformada
        lista_transformada.append(pygame.transform.flip(img, True, False))
    return lista_transformada

def cambiar_estado_musica(PANTALLA):
    global musica_pausada
    pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()
    nueva_pausa = not pygame.mixer.music.get_busy()
    if nueva_pausa != musica_pausada:
        musica_pausada = nueva_pausa
        actualizar_icono_musica(PANTALLA)

def actualizar_icono_musica(PANTALLA):
        if musica_pausada:
            PANTALLA.blit(sonido_off, (10, 10))
        else:
            PANTALLA.blit(sonido_on, (10, 10))

personaje_quieto = [pygame.image.load(r"recursos\quieto.png")]

personaje_quieto_izquierda = invertir_imagen(personaje_quieto)

personaje_camina_derecha = [pygame.image.load(r"recursos\run1.png"),
                            pygame.image.load(r"recursos\run2.png"),
                            pygame.image.load(r"recursos\run3.png"),
                            pygame.image.load(r"recursos\run4.png"),
                            pygame.image.load(r"recursos\run5.png"),
                            pygame.image.load(r"recursos\run6.png")]

personaje_camina_izquierda = invertir_imagen(personaje_camina_derecha)

personaje_salta_derecha = [pygame.image.load(r"recursos\fox_jump_1.png"),
                           pygame.image.load(r"recursos\fox_jump_2.png")]

personaje_salta_izquierda = invertir_imagen(personaje_salta_derecha)

personaje_golpeado = [pygame.image.load(r"recursos\fox_hurt_1.png"),
                      pygame.image.load(r"recursos\fox_hurt_2.png")]

dog_caminando = [pygame.image.load(r"recursos\dog_1.png"),
                pygame.image.load(r"recursos\dog_2.png"),
                pygame.image.load(r"recursos\dog_3.png"),
                pygame.image.load(r"recursos\dog_4.png"),
                pygame.image.load(r"recursos\dog_5.png"),
                pygame.image.load(r"recursos\dog_6.png")]
dog_caminando = invertir_imagen(dog_caminando)


aguila_vuela = [pygame.image.load(r"recursos\eagle_attack_1.png"),
                pygame.image.load(r"recursos\eagle_attack_2.png"),
                pygame.image.load(r"recursos\eagle_attack_3.png"),
                pygame.image.load(r"recursos\eagle_attack_4.png")]

gema = [pygame.image.load(r"recursos\gem_1.png"),
        pygame.image.load(r"recursos\gem_2.png"),
        pygame.image.load(r"recursos\gem_3.png"),
        pygame.image.load(r"recursos\gem_4.png"),
        pygame.image.load(r"recursos\gem_5.png")]

cherry = [pygame.image.load(r"recursos\cherry-1.png"),
          pygame.image.load(r"recursos\cherry-2.png"),
          pygame.image.load(r"recursos\cherry-3.png"),
          pygame.image.load(r"recursos\cherry-4.png"),
          pygame.image.load(r"recursos\cherry-5.png"),
          pygame.image.load(r"recursos\cherry-6.png"),
          pygame.image.load(r"recursos\cherry-7.png")]

agarrar_premio = [pygame.image.load(r"recursos\agarrar_gema_1.png"),
                pygame.image.load(r"recursos\agarrar_gema_2.png"),
                pygame.image.load(r"recursos\agarrar_gema_3.png"),
                pygame.image.load(r"recursos\agarrar_gema_4.png")]

sapo_saltando = [pygame.image.load(r"recursos\frog_jump_1.png"),
                 pygame.image.load(r"recursos\frog_jump_2.png")]

enemigo_muriendo = [pygame.image.load(r"recursos\enemy_death_1.png"),
                    pygame.image.load(r"recursos\enemy_death_2.png"),
                    pygame.image.load(r"recursos\enemy_death_3.png"),
                    pygame.image.load(r"recursos\enemy_death_4.png"),
                    pygame.image.load(r"recursos\enemy_death_5.png"),
                    pygame.image.load(r"recursos\enemy_death_6.png")]
plataforma_larga = pygame.image.load(r"recursos\plataforma.png")

oso_quieto = [pygame.image.load(r"recursos\jefe_1.png")]

oso_derecha = [pygame.image.load(r"recursos\jefe_1.png"),
               pygame.image.load(r"recursos\jefe_2.png"),
               pygame.image.load(r"recursos\jefe_3.png"),
               pygame.image.load(r"recursos\jefe_4.png")]

oso_izquierda = invertir_imagen(oso_derecha)

puerta_abierta = pygame.image.load(r"recursos\door_opened.png")
icono = pygame.image.load(r"recursos\quieto.png") 
fondo = pygame.image.load(r"recursos\fondo1.jpg")
house = pygame.image.load(r"recursos\house.png")
sonido_on = pygame.image.load(r"recursos\sonido on.png")
sonido_off = pygame.image.load(r"recursos\sonido off.png")
sonido_on = pygame.transform.scale(sonido_on,(30,30))
sonido_off = pygame.transform.scale(sonido_off,(30,30))
#ACCIONES PERSONAJE:
acciones = {}
acciones["Quieto"] = personaje_quieto
acciones["Quieto_izquierda"] = personaje_quieto_izquierda
acciones["Derecha"] = personaje_camina_derecha
acciones["Izquierda"] = personaje_camina_izquierda
acciones["Golpeado"] = personaje_golpeado
acciones["Salta_derecha"] = personaje_salta_derecha
acciones["Salta_izquierda"] = personaje_salta_izquierda
# ACCIONES ENEMIGO: 
acciones_enemigo = {}
acciones_enemigo["Volando"] = aguila_vuela
acciones_enemigo["Muriendo"] = enemigo_muriendo
# DOG:
dog_acciones = {}
dog_acciones["Caminando"] = dog_caminando
dog_acciones["Muriendo"] = enemigo_muriendo