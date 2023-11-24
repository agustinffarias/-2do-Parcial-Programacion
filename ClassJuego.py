import pygame
from constantes import *
from pygame.locals import *
from config import *
from ClassPersonaje import *
from modo import *
from ClassPlataformas import *
from ClassEnemigo import *
from ClassPremio import *

pygame.init()
RELOJ = pygame.time.Clock() 
PANTALLA = pygame.display.set_mode((W,H))
fondo = pygame.transform.scale(fondo,(W,H))
pygame.display.set_caption("Terremoto")
pygame.display.set_icon(icono)
pygame.font.init()
fuente = pygame.font.Font("fuente\PressStart2P-Regular.ttf", 12)

#Musica:
# pygame.mixer.music.load("recursos\musica_fondo.mp3")  # COPIAR RUTA RELATIVA
# pygame.mixer.music.play(0) # El uno significa que se va a repetir en bucle
# pygame.mixer.music.set_volume(1) #Seteamos el volumen que va a tener la musica de fondo

# ANIMACIONES DEL JUEGO:
KURAMA = Personaje(acciones,(35,50),100,550,4)
AGUILA = Enemigo(acciones_enemigo,(50,50),175,100,que_hace="Volando")
AGUILA_dos = Enemigo(acciones_enemigo,(50,50),660,30,que_hace="Volando")
DOG = Enemigo(dog_acciones,(80,50),800,555,que_hace="Caminando")
DOG_uno = Enemigo(dog_acciones,(80,50),200,555,que_hace="Caminando")
enemigos = [AGUILA,DOG,DOG_uno,AGUILA,AGUILA_dos]
#PLATAFORMAS:
plataformas =[piso_invisible,casa,plataforma_uno,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,
              plataforma_seis,plataforma_siete,plataforma_ocho,plataforma_nueve,plataforma_diez,puerta,craneo_left,
              craneo_casa]
bandera = True
while bandera:
    RELOJ.tick(FPS)
    tiempo = int(pygame.time.get_ticks() / 1000) +1
    texto = fuente.render("Tiempo: " +  str(tiempo),True,NEGRO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    
    boton = pygame.key.get_pressed()
    if boton[pygame.K_d]:
        KURAMA.direccion_izquierda = False 
        KURAMA.direccion_derecha = True
        KURAMA.que_hace = "Derecha"
        KURAMA.ultima_direccion = "Derecha"
    elif boton[pygame.K_a]:
        KURAMA.direccion_derecha = False
        KURAMA.direccion_izquierda = True
        KURAMA.que_hace = "Izquierda"
        KURAMA.ultima_direccion = "Izquierda"
    else:
        if not KURAMA.esta_saltando:
            KURAMA.que_hace = "Quieto"
        if KURAMA.ultima_direccion == "Izquierda":
            KURAMA.que_hace = "Quieto_izquierda"  
    if boton[pygame.K_SPACE]:
        if not KURAMA.esta_saltando:
            KURAMA.que_hace = "Salta"  
    
    #BLITEOS:
    PANTALLA.blit(fondo,(0,0))    
    PANTALLA.blit(texto,(950,30))
    
    
    for plataforma in plataformas: 
        if plataforma.visible: 
            PANTALLA.blit(plataforma.plataforma["superficie"],plataforma.plataforma["rectangulo"])   
    
    #ACTUALIZACIONES:
    KURAMA.actualizar(PANTALLA,plataformas)
    AGUILA.actualizar_vuelo(PANTALLA)
    AGUILA_dos.actualizar_vuelo(PANTALLA)
    DOG.actualizar_avance(PANTALLA)
    DOG_uno.actualizar_avance(PANTALLA)
    KURAMA.verificar_colision_enemigo(enemigos,PANTALLA)
    
    #MODO DEBUG:
    if obtener_modo():    
        for rect in KURAMA.rectangulos:
            pygame.draw.rect(PANTALLA, BLANCO, KURAMA.rectangulos[rect], 1)
        
        for plataforma in plataformas:
            for rect in plataforma.rectangulos:
                pygame.draw.rect(PANTALLA, BLANCO, plataforma.rectangulos[rect], 1)

        for enemigo in enemigos:
            for rect in enemigo.rectangulos:
                pygame.draw.rect(PANTALLA, BLANCO, enemigo.rectangulos[rect], 1)
                
    pygame.display.update()    
pygame.quit()