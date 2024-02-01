import pygame
import random
class DisparoJefe:
    def __init__(self,x,y,direccion):
        self.superficie = pygame.image.load(r"imagenes\disparo_jefe.png")
        self.superficie = pygame.transform.scale(self.superficie,(30,30))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = random.randrange(0,1100)
        self.rectangulo.centery = y
        self.direccion = direccion 
        
        
    def actualizar(self,pantalla):
        """
        Actualiza la posición del disparo y lo dibuja en la pantalla.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará el disparo.
        """
        if self.direccion == "Quieto":
            self.rectangulo.y += 2
        pantalla.blit(self.superficie,self.rectangulo)
        
    