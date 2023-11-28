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
            if not self.obtenido:
                pantalla.blit(self.animaciones["cereza"][0], self.rectangulo_principal)
            
  
    
