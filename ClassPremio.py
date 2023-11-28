import pygame
from config import *


class Premio():
    def __init__(self,animaciones,tamaño,x,y,path=""):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.path = path
        self.rectangulo_principal = self.animaciones["cereza"][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        self.visible = True
        self.obtenido = False
    
    def dibujar(self, pantalla):
        if self.visible:
            pantalla.blit(self.animaciones["cereza"][0], self.rectangulo_principal)
    
    
        
  
cereza_uno = Premio(animaciones,(25,25),187,156,"recursos\cherry-1.png")
cereza_dos = Premio(animaciones,(25,25),678,159,"recursos\cherry-1.png")
cereza_tres = Premio(animaciones,(25,25),902,213,"recursos\cherry-1.png")
cereza_cuatro = Premio(animaciones,(25,25),514,312,"recursos\cherry-1.png")
cereza_cinco = Premio(animaciones,(25,25),411,435,"recursos\cherry-1.png")
cereza_seis = Premio(animaciones,(25,25),987,375,"recursos\cherry-1.png")

premios = [cereza_uno,cereza_dos,cereza_tres,cereza_cuatro,cereza_cinco,cereza_seis]