import pygame
from GUI_form_prueba import FormPrueba
from config import *
from modo import *
from ClassEnemigo import *
from ClassPersonaje import *
from ClassPlataformas import *
from ClassPremio import *
from ClassNivel import *
from ClassNivel_uno import *
from ClassNivel_dos import *
from ClassNivel_tres import *


pygame.init()
RELOJ = pygame.time.Clock() 
pantalla = pygame.display.set_mode((W, H))
pygame.display.set_icon(icono)
fondo = pygame.transform.scale(fondo, (W, H))
pygame.display.set_caption("Foxxie")


form_prueba = FormPrueba(pantalla, 100, 100, 1000, 350, "brown", "white", 5, True)

bandera = True
while bandera:
    pantalla.fill("black")
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            bandera = False
            pygame.quit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #         print(event.pos)
    
    form_prueba.update(lista_eventos)
    
    pygame.display.update()    
pygame.quit()
