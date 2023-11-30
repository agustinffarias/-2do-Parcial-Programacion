import pygame
from config import *
from modo import *
from ClassEnemigo import *
from ClassPersonaje import *
from ClassPlataformas import *
from ClassPremio import * 
from constantes import *
import re
class Nivel():
    def __init__(self,pantalla,personaje_principal,lista_plataformas,img_fondo,lista_enemigos,lista_premios):
        self.pantalla = pantalla
        self.personaje_principal = personaje_principal
        self.lista_plataformas = lista_plataformas
        self.img_fondo = img_fondo
        self.lista_enemigos = lista_enemigos
        self.lista_premios = lista_premios
        self.fuente = pygame.font.Font("fuente\PressStart2P-Regular.ttf", 12)

    
    def update(self,lista_eventos):
        self.leer_eventos(lista_eventos,self.pantalla)
        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rectangulos(self.pantalla)
        
    def leer_eventos(self,lista_eventos,pantalla):
        global juego_pausado, tiempo_inicio_pausa,tiempo_pausado
        for event in lista_eventos:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()
                if event.key == pygame.K_m:                
                    cambiar_estado_musica(self.pantalla)
                if event.key == pygame.K_RETURN:
                    if juego_pausado:
                        juego_pausado = False
                        tiempo_transcurrido_desde_pausa = pygame.time.get_ticks() - tiempo_inicio_pausa
                        tiempo_pausado += tiempo_transcurrido_desde_pausa
                        pygame.mixer.music.unpause() 
                    else:
                        juego_pausado = True
                        tiempo_inicio_pausa = pygame.time.get_ticks()
                        pygame.mixer.music.pause() 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            elif event.type == pygame.USEREVENT:
                self.personaje_principal.inmune = False
            # elif event.type == pygame.USEREVENT+1 :
                
        if juego_pausado:
            self.pantalla.blit(pausa, (585, 10))
            pygame.display.update()

    def leer_inputs(self):
        boton = pygame.key.get_pressed()
        if boton[pygame.K_RIGHT]:
            self.personaje_principal.direccion_izquierda = False 
            self.personaje_principal.direccion_derecha = True
            self.personaje_principal.que_hace = "Derecha"
            self.personaje_principal.ultima_direccion = "Derecha"
        elif boton[pygame.K_LEFT]:
            self.personaje_principal.direccion_derecha = False
            self.personaje_principal.direccion_izquierda = True
            self.personaje_principal.que_hace = "Izquierda"
            self.personaje_principal.ultima_direccion = "Izquierda"
        else:
            if not self.personaje_principal.esta_saltando:
                self.personaje_principal.que_hace = "Quieto"
            if self.personaje_principal.ultima_direccion == "Izquierda":
                self.personaje_principal.que_hace = "Quieto_izquierda"  
        if boton[pygame.K_SPACE]:
            if not self.personaje_principal.esta_saltando:
                self.personaje_principal.que_hace = "Salta" 

    def dibujar_rectangulos(self,pantalla):
        if obtener_modo():    
            for rect in self.personaje_principal.rectangulos:
                pygame.draw.rect(self.pantalla, BLANCO, self.personaje_principal.rectangulos[rect], 1)
            
            for plataforma in self.lista_plataformas:
                for rect in plataforma.rectangulos:
                    pygame.draw.rect(self.pantalla, BLANCO, plataforma.rectangulos[rect], 1)

            for enemigo in self.lista_enemigos:
                for rect in enemigo.rectangulos:
                    pygame.draw.rect(self.pantalla, BLANCO, enemigo.rectangulos[rect], 1)
            
            for premio in self.lista_premios:
                for rect in premio.rectangulos:
                    pygame.draw.rect(self.pantalla, BLANCO, premio.rectangulos[rect], 1)

    def actualizar_pantalla(self):
        if not juego_pausado:    
            tiempo = int(pygame.time.get_ticks() / 1000) +1 
            texto = self.fuente.render("Tiempo: " +  str(tiempo),True,NEGRO) 
            self.pantalla.blit(self.img_fondo,(0,0))    
            self.pantalla.blit(texto,(950,10))
            self.pantalla.blit(diccionario_vidas[str(self.personaje_principal.vida_actual)], (470, 15))
            actualizar_icono_musica(self.pantalla)
            self.personaje_principal.puntaje(self.fuente,self.pantalla)
            
            
            for plataforma in self.lista_plataformas: 
                if plataforma.visible: 
                    self.pantalla.blit(plataforma.plataforma["superficie"],plataforma.plataforma["rectangulo"])   
            
            for premio in self.lista_premios:
                premio.dibujar(self.pantalla)
                
            KURAMA.actualizar(self.pantalla,self.lista_plataformas)
            for enemigo in self.lista_enemigos:
                if not re.match(r'^[A-Za-z]+$', enemigo.que_hace):
                    raise ValueError("El formato de 'que_hace' solo debe contener letras.")
                if enemigo.que_hace == "Volando":
                    enemigo.actualizar_vuelo(self.pantalla)
                if enemigo.que_hace == "Caminando":
                    enemigo.actualizar_avance(self.pantalla)
                if enemigo.que_hace == "Quieto":
                    enemigo.animar(self.pantalla)
                    
            KURAMA.verificar_colision_enemigo(self.lista_enemigos,self.pantalla)
            KURAMA.verificar_colision_premio(self.lista_premios,self.pantalla)
            KURAMA.puntaje(self.fuente,self.pantalla)
        
        