import pygame
from config import *


class Premio():
    def __init__(self,animaciones,tamaño,x,y,que_hace="cereza"):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.que_hace = que_hace
        self.rectangulo_principal = self.animaciones[self.que_hace][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        self.visible = True
        self.obtenido = False
        self.indice_animacion = 0
        self.animacion_actual = self.animaciones[self.que_hace]

        
    
    def dibujar(self, pantalla):
        if self.visible and not self.obtenido:
            # Obtener la animación actual
            animacion_actual = self.animacion_actual[self.indice_animacion]
            pantalla.blit(animacion_actual, self.rectangulo_principal)

            # Incrementar el índice de animación para el siguiente fotograma
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion_actual)
        if self.obtenido:
            animacion_actual = self.animacion_actual[self.indice_animacion]
            pantalla.blit(animacion_actual["obtenido"], self.rectangulo_principal)

            # Incrementar el índice de animación para el siguiente fotograma
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion_actual)
                
        
                
            
  
    
