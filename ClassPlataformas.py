from config import *
from ClassPersonaje import Personaje
from constantes import *

class Plataformas:
    def __init__(self,visible,tamaño,x,y,path=""):

        self.visible = visible
        self.tamaño = tamaño
        self.plataforma =self.crear_plataformas(visible,tamaño,x,y,path)
        self.path = path
        self.x = x
        self.y = y
        self.rectangulos = obtener_rectangulos(self.plataforma["rectangulo"],tamaño[0],tamaño[1])
        
    def crear_plataformas(self,visible:bool,tamaño,x,y,path=""):
        plataforma = {}
        if visible:
            plataforma["superficie"] = pygame.image.load(path)
            plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"],tamaño)
        else:
            plataforma["superficie"] = pygame.Surface(tamaño)
        
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = x
        plataforma["rectangulo"].y = y

        return plataforma