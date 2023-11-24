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
fuente = pygame.font.Font(None, 36)

#Musica:
# pygame.mixer.music.load("recursos\musica_fondo.mp3")  # COPIAR RUTA RELATIVA
# pygame.mixer.music.play(0) # El uno significa que se va a repetir en bucle
# pygame.mixer.music.set_volume(1) #Seteamos el volumen que va a tener la musica de fondo

#ACCIONES PERSONAJE:
acciones = {}
acciones["Quieto"] = personaje_quieto
acciones["Quieto_izquierda"] = personaje_quieto_izquierda
acciones["Derecha"] = personaje_camina_derecha
acciones["Izquierda"] = personaje_camina_izquierda
acciones["Golpeado"] = personaje_golpeado
acciones["Salta_derecha"] = personaje_salta_derecha
acciones["Salta_izquierda"] = personaje_salta_izquierda

# ACCIONES ENEMIGO: 
acciones_enemigo = {}
acciones_enemigo["Volando"] = aguila_vuela
acciones_enemigo["Muriendo"] = enemigo_muriendo
# DOG:
dog_acciones = {}
dog_acciones["Caminando"] = dog_caminando
dog_acciones["Muriendo"] = enemigo_muriendo

# JEFE OSO NIVEL 3:
# jefe_acciones={}
# jefe_acciones["Quieto"] = oso_quieto
# jefe_acciones["Camina_derecha"] = oso_derecha
# jefe_acciones["Camina_izquierda"] = oso_izquierda
animaciones = {}
animaciones["cereza"] = cherry
animaciones["Obtenido"] = agarrar_premio

diccionario_vidas = {
    "Cinco": pygame.transform.scale(vida_llena, (100, 20)),
    "Cuatro": pygame.transform.scale(cuatro_vidas, (100, 20)),
    "Tres": pygame.transform.scale(tres_vidas, (100, 20)),
    "Dos": pygame.transform.scale(dos_vidas, (100, 20)),
    "Una": pygame.transform.scale(una_vida, (100, 20)),
}
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
tiempo_de_juego = 0
while bandera:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        KURAMA.direccion_izquierda = False 
        KURAMA.direccion_derecha = True
        KURAMA.que_hace = "Derecha"
        KURAMA.ultima_direccion = "Derecha"
    elif teclas[pygame.K_LEFT]:
        KURAMA.direccion_derecha = False
        KURAMA.direccion_izquierda = True
        KURAMA.que_hace = "Izquierda"
        KURAMA.ultima_direccion = "Izquierda"
    else:
        if not KURAMA.esta_saltando:
            KURAMA.que_hace = "Quieto"
        if KURAMA.ultima_direccion == "Izquierda":
            KURAMA.que_hace = "Quieto_izquierda"  
    if teclas[pygame.K_SPACE]:
        if not KURAMA.esta_saltando:
            KURAMA.que_hace = "Salta"
            
    PANTALLA.blit(fondo,(0,0))
   
    for plataforma in plataformas: 
        if plataforma != piso_invisible: 
            PANTALLA.blit(plataforma.plataforma["superficie"],plataforma.plataforma["rectangulo"])   
    
    KURAMA.actualizar(PANTALLA,plataformas)
    AGUILA.actualizar_vuelo(PANTALLA)
    AGUILA_dos.actualizar_vuelo(PANTALLA)
    DOG.actualizar_avance(PANTALLA)
    DOG_uno.actualizar_avance(PANTALLA)
    KURAMA.verificar_colision_enemigo(enemigos,PANTALLA)
            
    if obtener_modo():    
        pygame.draw.rect(PANTALLA, BLANCO, KURAMA.rectangulo_principal, 1)
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