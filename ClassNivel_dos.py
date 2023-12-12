from ClassNivel import *
from config import *


from constantes import *

class Nivel_dos(Nivel):
    def __init__(self,pantalla: pygame.Surface):
        self.pantalla = pantalla
        fondo = pygame.image.load(r"imagenes\fondo.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))
        self.fuente = pygame.font.Font("fuente\PressStart2P-Regular.ttf", 12)

        #Musica:
        pygame.mixer.music.load(r"sonidos\fondo_nivel_2.mp3")  # COPIAR RUTA RELATIVA
        pygame.mixer.music.play(-1) # El uno significa que se va a repetir en bucle
        pygame.mixer.music.set_volume(1) #Seteamos el volumen que va a tener la musica de fondo
        
        #PLATAFORMAS:      
        piso_invisible = Plataformas(False,(1100,20),0,600)
        
        casa = Plataformas(True,(200,200),900,400,r"imagenes\house.png")
        
        plataforma_uno = Plataformas(True,(80,25),293,460,r"imagenes\plataforma.png")#
        plataforma_cuatro = Plataformas(True,(80,25),372,460,r"imagenes\plataforma.png")#
        plataforma_dos = Plataformas(True,(80,25),451,460,r"imagenes\plataforma.png")#
        
        plataforma_nueve = Plataformas(True,(80,25),446,322,r"imagenes\plataforma.png")
        plataforma_cinco = Plataformas(True,(80,25),597,236,r"imagenes\plataforma.png")#
        plataforma_seis = Plataformas(True,(80,25),676,236,r"imagenes\plataforma.png")#
        plataforma_siete = Plataformas(True,(80,25),143,231,r"imagenes\plataforma.png")
        plataforma_diez = Plataformas(True,(80,25),223,231,r"imagenes\plataforma.png")
        
        puerta = Plataformas(True,(46,58),956,540,r"imagenes\door_opened.png")
        
        craneo_casa = Plataformas(True,(30,20),910,580,r"imagenes\skulls.png")
        craneo_left = Plataformas(True,(30,20),1004,580,r"imagenes\skulls.png")
        plataformas =[piso_invisible,casa,plataforma_uno,plataforma_dos,plataforma_cuatro,plataforma_cinco,
                    plataforma_seis,plataforma_siete,plataforma_nueve,plataforma_diez,puerta,craneo_left,
                    craneo_casa]
        
        enemigos = []
        # ENEMIGOS:
        for x in range(random.randrange(6)+3):
            AGUILA = Enemigo(acciones_enemigo,(50,50),(random.randrange(W)),80,que_hace="Volando")
            enemigos.append(AGUILA)
            
        for x in range(random.randrange(6)+3):
            dog = Enemigo(dog_acciones,(80,50),(random.randrange(H)),555,que_hace="Caminando")
            enemigos.append(dog)
        # PREMIOS:
        KURAMA = Personaje(acciones,(35,50),404,411,4)
        cereza = Premio(animaciones_premio,(25,25),70,521)
        cereza_2 = Premio(animaciones_premio,(25,25),481,298)
        cereza_3 = Premio(animaciones_premio,(25,25),175,201)
        cereza_4 = Premio(animaciones_premio,(25,25),646,104)
        cereza_5 = Premio(animaciones_premio,(25,25),688,104)
        cereza_6 = Premio(animaciones_premio,(25,25),732,104)
        cereza_7 = Premio(animaciones_premio,(25,25),848,521)
        cereza_8 = Premio(animaciones_premio,(25,25),798,521)
        cereza_9 = Premio(animaciones_premio,(25,25),748,521)
        
        premios = [cereza,cereza_2,cereza_3,cereza_4,cereza_5,cereza_6,cereza_7,cereza_8,cereza_9]

        super().__init__(pantalla,KURAMA,plataformas,fondo,enemigos,premios)