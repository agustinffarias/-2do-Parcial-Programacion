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

piso_invisible = Plataformas(False,(1100,20),0,600)

casa = Plataformas(True,(200,200),900,400,r"recursos\house.png")

plataforma_uno = Plataformas(True,(80,25),293,460,r"recursos\plataforma.png")
plataforma_cuatro = Plataformas(True,(80,25),372,460,r"recursos\plataforma.png")

plataforma_dos = Plataformas(True,(80,25),394,340,r"recursos\plataforma.png")
plataforma_ocho = Plataformas(True,(80,25),474,340,r"recursos\plataforma.png")

plataforma_tres = Plataformas(True,(80,25),785,243,r"recursos\plataforma.png")
plataforma_nueve = Plataformas(True,(80,25),864,243,r"recursos\plataforma.png")

plataforma_cinco = Plataformas(True,(80,25),646,189,r"recursos\plataforma.png")
plataforma_seis = Plataformas(True,(80,25),566,189,r"recursos\plataforma.png")

plataforma_siete = Plataformas(True,(80,25),143,185,r"recursos\plataforma.png")
plataforma_diez = Plataformas(True,(80,25),223,185,r"recursos\plataforma.png")

puerta = Plataformas(True,(46,58),956,540,r"recursos\door_opened.png")
craneo_casa = Plataformas(True,(30,20),910,580,r"recursos\skulls.png")
craneo_left = Plataformas(True,(30,20),1004,580,r"recursos\skulls.png")
#PLATAFORMAS:
plataformas =[piso_invisible,casa,plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,
              plataforma_seis,plataforma_siete,plataforma_ocho,plataforma_nueve,plataforma_diez,puerta,craneo_left,
              craneo_casa]