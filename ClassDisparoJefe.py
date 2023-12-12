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
        if self.direccion == "Quieto":
            self.rectangulo.y += 5
        pantalla.blit(self.superficie,self.rectangulo)
        
    