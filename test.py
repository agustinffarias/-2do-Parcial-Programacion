import pygame
import sys
from pygame.locals import *
from GUI_form_prueba import FormPrueba

pygame.init()
WIDTH = 1200
HEIGHT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))


#CREAR FORMULARIO 
form_prueba = FormPrueba(pantalla, 100, 100, 1000, 350, "brown", "white", 5, True)
#fromulario activo es que se muetre en pantalla

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("Black")
    form_prueba.update(eventos)
    
    
    pygame.display.flip()