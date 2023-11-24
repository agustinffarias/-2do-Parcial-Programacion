import pygame

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


vida_llena= pygame.image.load(r"recursos\vida_5.png")
cuatro_vidas =  pygame.image.load(r"recursos\vida_5.png")
tres_vidas= pygame.image.load(r"recursos\vida_3.png")
dos_vidas= pygame.image.load(r"recursos\vida_2.png")
una_vida= pygame.image.load(r"recursos\vida_1.png")

diccionario_vidas = {
    "Cinco": pygame.transform.scale(vida_llena, (100, 20)),
    "Cuatro": pygame.transform.scale(cuatro_vidas, (100, 20)),
    "Tres": pygame.transform.scale(tres_vidas, (100, 20)),
    "Dos": pygame.transform.scale(dos_vidas, (100, 20)),
    "Una": pygame.transform.scale(una_vida, (100, 20)),
}