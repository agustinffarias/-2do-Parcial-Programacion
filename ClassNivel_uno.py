from ClassNivel import * 
from config import *
from constantes import *
import re


class Nivel_uno(Nivel):
    def __init__(self,pantalla: pygame.Surface):
        self.pantalla = pantalla
        fondo = pygame.image.load(r"imagenes\fondo1.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))
        self.fuente = pygame.font.Font("fuente\PressStart2P-Regular.ttf", 12)

        #Musica:
        pygame.mixer.music.load("sonidos\musica_fondo.mp3")  # COPIAR RUTA RELATIVA
        pygame.mixer.music.play(-1) # El uno significa que se va a repetir en bucle
        pygame.mixer.music.set_volume(1) #Seteamos el volumen que va a tener la musica de fondo
        
        #PLATAFORMAS:
        piso_invisible = Plataformas(False,(1100,20),0,600)
        casa = Plataformas(True,(200,200),900,400,r"imagenes\house.png")
        plataforma_uno = Plataformas(True,(80,25),293,460,r"imagenes\plataforma.png")
        plataforma_cuatro = Plataformas(True,(80,25),372,460,r"imagenes\plataforma.png")
        plataforma_dos = Plataformas(True,(80,25),394,340,r"imagenes\plataforma.png")
        plataforma_ocho = Plataformas(True,(80,25),474,340,r"imagenes\plataforma.png")
        plataforma_tres = Plataformas(True,(80,25),785,243,r"imagenes\plataforma.png")
        plataforma_nueve = Plataformas(True,(80,25),864,243,r"imagenes\plataforma.png")
        plataforma_cinco = Plataformas(True,(80,25),646,210,r"imagenes\plataforma.png")
        plataforma_seis = Plataformas(True,(80,25),566,210,r"imagenes\plataforma.png")
        plataforma_siete = Plataformas(True,(80,25),143,210,r"imagenes\plataforma.png")
        plataforma_diez = Plataformas(True,(80,25),223,210,r"imagenes\plataforma.png")
        puerta = Plataformas(True,(46,58),956,540,r"imagenes\door_opened.png")
        craneo_casa = Plataformas(True,(30,20),910,580,r"imagenes\skulls.png")
        craneo_left = Plataformas(True,(30,20),1004,580,r"imagenes\skulls.png")
        plataformas =[piso_invisible,casa,plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,
                    plataforma_seis,plataforma_siete,plataforma_ocho,plataforma_nueve,plataforma_diez,puerta,craneo_left,
                    craneo_casa]
        
        # ENEMIGOS:
        AGUILA = Enemigo(acciones_enemigo,(50,50),175,80,que_hace="Volando")
        AGUILA_dos = Enemigo(acciones_enemigo,(50,50),660,30,que_hace="Volando")
        DOG = Enemigo(dog_acciones,(80,50),800,555,que_hace="Caminando")
        DOG_uno = Enemigo(dog_acciones,(80,50),50,555,que_hace="Caminando")
        

        enemigos = [DOG,DOG_uno,AGUILA,AGUILA_dos]
        
        # PREMIOS:
        cereza_uno = Premio(animaciones_premio,(25,25),187,156)
        cereza_dos = Premio(animaciones_premio,(25,25),678,159)
        cereza_tres = Premio(animaciones_premio,(25,25),902,213)
        cereza_cuatro = Premio(animaciones_premio,(25,25),514,312)
        cereza_cinco = Premio(animaciones_premio,(25,25),411,435)
        premios = [cereza_uno,cereza_dos,cereza_tres,cereza_cuatro,cereza_cinco]
        
        super().__init__(pantalla,KURAMA,plataformas,fondo,enemigos,premios)
