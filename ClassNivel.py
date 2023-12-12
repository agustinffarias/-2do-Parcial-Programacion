import pygame
from GUI.GUI_form import *
from config import *
from modo import *
from ClassEnemigo import *
from ClassPersonaje import *
from ClassPlataformas import *
from ClassPremio import * 
from constantes import *
from ClassJefe import *


import re
class Nivel(Form):
    def __init__(self,pantalla,personaje_principal,lista_plataformas,img_fondo,lista_enemigos,lista_premios,boss = None):
        self._slave = pantalla
        self.KURAMA = personaje_principal
        self.lista_plataformas = lista_plataformas
        self.img_fondo = img_fondo
        self.lista_enemigos = lista_enemigos
        self.lista_premios = lista_premios
        self.fuente = pygame.font.Font("fuente\PressStart2P-Regular.ttf", 12)
        self.boss = boss


    def update(self,lista_eventos):
        self.leer_eventos(lista_eventos,self._slave)
        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rectangulos(self._slave)
        
    def leer_eventos(self,lista_eventos,pantalla):
        global juego_pausado, tiempo_inicio_pausa,tiempo_pausado
        for event in lista_eventos:    
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_TAB:
                    cambiar_modo()
                if event.key == pygame.K_m:                
                    cambiar_estado_musica(self._slave)
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
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print(event.pos)
            elif event.type == pygame.USEREVENT:
                self.KURAMA.inmune = False
                for enemigo in self.boss:
                    enemigo.inmune = False
            elif event.type == pygame.USEREVENT+1:
                nuevo_enemigo = Enemigo(dog_acciones, (80, 50), (random.randrange(H))-100, 555, que_hace="Caminando")
                nuevo_enemigo1 = Enemigo(acciones_enemigo,(50,50),(random.randrange(W))-100,80,que_hace="Volando")
                self.lista_enemigos.append(nuevo_enemigo)
                self.lista_enemigos.append(nuevo_enemigo1)
            elif event.type == pygame.USEREVENT+2:
                self.boss.que_hace = "Quieto"
                self.boss.tiempo_quieto = 0  
        if juego_pausado:
            self._slave.blit(pausa, (585, 10))
            pygame.display.update()

    def leer_inputs(self):
        boton = pygame.key.get_pressed()
        if boton[pygame.K_RIGHT]:
            self.KURAMA.direccion_izquierda = False 
            self.KURAMA.direccion_derecha = True
            self.KURAMA.que_hace = "Derecha"
            self.KURAMA.ultima_direccion = "Derecha"
        elif boton[pygame.K_LEFT]:
            self.KURAMA.direccion_derecha = False
            self.KURAMA.direccion_izquierda = True
            self.KURAMA.que_hace = "Izquierda"
            self.KURAMA.ultima_direccion = "Izquierda"
        else:
            if not self.KURAMA.esta_saltando:
                self.KURAMA.que_hace = "Quieto"
            if self.KURAMA.ultima_direccion == "Izquierda":
                self.KURAMA.que_hace = "Quieto_izquierda"  
        if boton[pygame.K_SPACE]:
            if not self.KURAMA.esta_saltando:
                self.KURAMA.que_hace = "Salta"
        
        if boton[pygame.K_f]:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.KURAMA.tiempo_ultimo_disparo >= 500:
                self.KURAMA.lanzar_proyectiles()
                self.KURAMA.tiempo_ultimo_disparo = tiempo_actual

    def dibujar_rectangulos(self,pantalla):
        if obtener_modo():    
            for rect in self.KURAMA.rectangulos:
                pygame.draw.rect(self._slave, BLANCO, self.KURAMA.rectangulos[rect], 1)
            
            for plataforma in self.lista_plataformas:
                for rect in plataforma.rectangulos:
                    pygame.draw.rect(self._slave, BLANCO, plataforma.rectangulos[rect], 1)

            for enemigo in self.lista_enemigos:
                for rect in enemigo.rectangulos:
                    pygame.draw.rect(self._slave, BLANCO, enemigo.rectangulos[rect], 1)
            
            for premio in self.lista_premios:
                for rect in premio.rectangulos:
                    pygame.draw.rect(self._slave, BLANCO, premio.rectangulos[rect], 1)
        
    def actualizar_pantalla(self):
        if self.KURAMA.vida_actual > 0:
            if not juego_pausado:    
                tiempo = int(pygame.time.get_ticks() / 1000) +1 
                texto = self.fuente.render("Tiempo: " +  str(tiempo),True,NEGRO) 
                self._slave.blit(self.img_fondo,(0,0))    
                self._slave.blit(texto,(950,10))
                if self.KURAMA.vida_actual >=1:
                    self._slave.blit(diccionario_vidas[str(self.KURAMA.vida_actual)], (470, 15))
                actualizar_icono_musica(self._slave)
                self.KURAMA.puntaje(self.fuente,self._slave)

                for plataforma in self.lista_plataformas: 
                    if plataforma.visible: 
                        self._slave.blit(plataforma.plataforma["superficie"],plataforma.plataforma["rectangulo"])   
                
                for premio in self.lista_premios:
                    premio.dibujar(self._slave)
                
                    
                    
                self.KURAMA.actualizar(self._slave,self.lista_plataformas,lista_enemigos=self.lista_enemigos)
                for enemigo in self.lista_enemigos:
                    if not re.match(r'^[A-Za-z]+$', enemigo.que_hace):
                        raise ValueError("El formato de 'que_hace' solo debe contener letras.")
                    if enemigo.que_hace == "Volando":
                        enemigo.actualizar_vuelo(self._slave)
                    if enemigo.que_hace == "Caminando":
                        enemigo.actualizar_avance(self._slave)
                    if enemigo.que_hace == "Quieto":
                        enemigo.animar(self._slave)
                    if (tiempo % 15 == 0):
                        pygame.time.set_timer(pygame.USEREVENT+1,1500,1)
                    
                # if self.boss != None:
                #     for enemigo in self.boss:
                #         if enemigo.que_hace == "Caminando":
                #             enemigo.actualizar_avance(self._slave)
                
                if self.boss is not None and len(self.boss) > 0:
                    if self.boss[0].que_hace == "Quieto" and self.boss[0].esta_muerto == False:
                        self.boss[0].animar(self._slave)
                        
                        tiempo_actual = pygame.time.get_ticks()
                        if tiempo_actual - self.boss[0].tiempo_ultimo_disparo >= 10000:  # 10 segundos en milisegundos
                            self.boss[0].lanzar_proyectiles()
                            self.boss[0].tiempo_ultimo_disparo = tiempo_actual
                        
                        self.boss[0].actualizar_proyectiles(self._slave,self.KURAMA)
                
                if (tiempo % 15 == 0):
                    self.KURAMA.perder_vida(PANTALLA=self._slave)
                self.KURAMA.actualizar_proyectiles(self._slave,self.lista_enemigos,self.boss)
                self.KURAMA.verificar_colision_enemigo(self.lista_enemigos,self._slave)
                self.KURAMA.verificar_colision_premio(self.lista_premios,self._slave)
                # if self.boss != None:
                #     self.KURAMA.verificar_colision_jefe(self.boss,self._slave)
                self.KURAMA.puntaje(self.fuente,self._slave)
        
            if len(self.lista_premios) <= 0:
                self.KURAMA.mostrar_pantalla_siguiente_nivel(self._slave)
            
        
        else:
            self.KURAMA.mostrar_pantalla_perdida(self._slave)
                
            
        
        