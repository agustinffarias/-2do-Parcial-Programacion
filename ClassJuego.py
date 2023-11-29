import pygame
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
# icono = pygame.display.set_icon()
fondo = pygame.transform.scale(fondo, (W, H))
pygame.display.set_caption("Terremoto")

nivel = Nivel_uno(pantalla)

bandera = True
while bandera:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            bandera = False
            pygame.quit()

    nivel.update(lista_eventos)

    pygame.display.update()    
pygame.quit()