import pygame

class Disparo:
    def __init__(self,x,y,direccion):
        self.superficie = pygame.image.load(r"imagenes\disparo_10.png")
        self.superficie = pygame.transform.scale(self.superficie,(30,30))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion 
        
        
    def actualizar(self,pantalla):
        if self.direccion == "Derecha" or self.direccion == "Quieto" or self.direccion == "Salta_derecha":
            self.rectangulo.x += 10 #VELOCIDAD DEL DISPARO
        elif self.direccion == "Izquierda" or self.direccion == "Quieto_izquierda" or self.direccion == "Salta_izquierda":
            self.rectangulo.x -= 10
        pantalla.blit(self.superficie,self.rectangulo)
        
    