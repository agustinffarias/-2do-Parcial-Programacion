from ClassDisparo import *
from config import *
import pygame
from ClassEnemigo import *

class Personaje: 
    def __init__(self,animaciones,tamaño,pos_x,pos_y,velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        self.que_hace = "Quieto"
        self.contador_pasos = 0 
        self.animacion_actual = self.animaciones[self.que_hace]
        self.desplazamiento_y = 0
        self.potencia_salto = -17
        self.limite_velocidad_salto = 10
        self.gravedad = 1
        self.esta_saltando = False
        self.direccion_derecha = True
        self.direccion_izquierda = False
        self.ultima_direccion = "Derecha"
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        self.vida_actual = 5
        self.inmune = False
        self.puntos = 0
        self.lista_proyectiles = []
        self.tiempo_ultimo_disparo = 0
        
    def actualizar(self, pantalla, plataforma,lista_enemigos):
        match self.que_hace:
            case "Derecha":
                # Lógica para el movimiento a la derecha
                self.caminar(pantalla)
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Derecha"]
                if self.esta_saltando:
                    self.animacion_actual = self.animaciones["Salta_derecha"]
            case "Izquierda":
                # Lógica para el movimiento a la izquierda
                self.caminar(pantalla)
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Izquierda"]
                if self.esta_saltando:
                    self.animacion_actual = self.animaciones["Salta_izquierda"]
            case "Quieto_izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Quieto_izquierda"]              
            case "Salta":
                # Lógica para el salto
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    if self.direccion_derecha:
                        self.animacion_actual = self.animaciones["Salta_derecha"]
                    elif self.direccion_izquierda:
                        self.animacion_actual = self.animaciones["Salta_izquierda"]
            case "Quieto":
                # Lógica para estar quieto
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Quieto"]
        # self.actualizar_proyectiles(pantalla,lista_enemigos=lista_enemigos,self.boss)
        self.aplicar_gravedad(pantalla, plataforma)
        self.animar(pantalla)
        
    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rectangulo_principal)
        self.contador_pasos += 1
        
    def puntaje(self,fuente,PANTALLA):
        mensaje = fuente.render("Puntos: " + str(self.puntos),True,NEGRO)
        PANTALLA.blit(mensaje, (952,30))
        
    
    def caminar(self,pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1
        
        nueva_x = self.rectangulo_principal.x + velocidad_actual
        
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width:
            for lado in self.rectangulos:
                self.rectangulos[lado].x += velocidad_actual
                
    def aplicar_gravedad(self,pantalla,plataforma):
        if self.esta_saltando:
            self.animar(pantalla)
            for lado in self.rectangulos:
                self.rectangulos[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
        
        for piso in plataforma:
            if self.rectangulos["bottom"].colliderect(piso.rectangulos["top"]):
                self.desplazamiento_y = 0
                self.rectangulo_principal.bottom = piso.plataforma["rectangulo"].top
                self.esta_saltando = False
                break
            elif self.rectangulos["top"].colliderect(piso.rectangulos["bottom"]):
                self.desplazamiento_y = 15
                for lado in self.rectangulos:
                    self.rectangulos[lado].top = piso.rectangulos["bottom"].bottom
                    if lado == "bottom":
                        self.rectangulos[lado].top = self.rectangulos["principal"].bottom
            else:
                self.esta_saltando = True
    
    def perder_vida(self, PANTALLA):
        if self.inmune == False:
            if self.vida_actual >= 1:
                self.vida_actual -= 1
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
                self.puntos -= 100
                if self.puntos <= 0:
                    self.puntos = 0
                self.inmune = True
                pygame.time.set_timer(pygame.USEREVENT,1500,1)

    def verificar_colision_enemigo(self, enemigos, PANTALLA):
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Error al inicializar Pygame: {e}")
        for enemigo in enemigos:
            if self.rectangulos["bottom"].colliderect(enemigo.rectangulos["top"]):
                enemigo.muriendo = True
                self.puntos += 200
                enemigo.animacion_actual = enemigo.animaciones["Muriendo"]
                enemigo.animar(PANTALLA)
                if enemigo.rectangulo_principal.y >= PANTALLA.get_height():
                    enemigo.esta_muerto = True
                enemigos.remove(enemigo)
            if self.rectangulos["top"].colliderect(enemigo.rectangulos["bottom"]):
                sonido_ser_golpeado.play(loops=0)
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
                self.perder_vida(PANTALLA)
            elif self.rectangulos["right"].colliderect(enemigo.rectangulos["left"]):
                sonido_ser_golpeado.play(loops=0)
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
                self.perder_vida(PANTALLA)
            elif self.rectangulos["left"].colliderect(enemigo.rectangulos["right"]):
                sonido_ser_golpeado.play(loops=0)
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
                self.perder_vida(PANTALLA)

    def verificar_colision_premio(self, premios, PANTALLA):
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Error al inicializar Pygame: {e}")
        for premio in premios:
            try:
                if self.rectangulos["principal"].colliderect(premio.rectangulo_principal):
                    if not premio.obtenido:
                        premio.que_hace = "obtenido"  # Cambiar la animación actual
                        sonido_agarrar_cereza.play(loops=0)
                        premio.obtenido = True
                        premio.visible = False
                        self.puntos += 50
                        if self.vida_actual <=4:
                            self.vida_actual += 1
                        premios.remove(premio)
            except KeyError:
                print("Error: Clave inexistente en el diccionario.")
                
    def mostrar_pantalla_perdida(self,pantalla):
        imagen_perdida = pygame.image.load("imagenes\game_over.png")
        imagen_perdida = pygame.transform.scale(imagen_perdida,(W,H))
        pantalla.blit(imagen_perdida, (0, 0))
        font = pygame.font.Font(r"fuente\PressStart2P-Regular.ttf", 15)
        mensaje = font.render("Se ha quedado sin vida pero...",True,BLANCO) #####
        mensaje_2 = font.render("Si lo desea, puede seguir jugando",True,BLANCO) #####
        pantalla.blit(mensaje, (250, 400))
        pantalla.blit(mensaje_2, (250, 470))
         
    def mostrar_pantalla_siguiente_nivel(self,pantalla):
        font = pygame.font.Font(r"fuente\PressStart2P-Regular.ttf", 15)
        mensaje = font.render("NIVEL SUPERADO !",True,NEGRO) #####
        pantalla.blit(mensaje, (420, 90))
    
    def lanzar_proyectiles(self):
        x = None
        margen = 47
        y = self.rectangulo_principal.centery + 10
        
        if self.que_hace == "Derecha" or self.que_hace == "Quieto" or self.que_hace == "Salta_derecha":
            x = self.rectangulo_principal.right - margen
        elif self.que_hace == "Izquierda" or self.que_hace == "Quieto_izquierda" or self.que_hace == "Salta_izquierda":
            x = self.rectangulo_principal.left -100 + margen
            
        if x is not None:
            self.lista_proyectiles.append(Disparo(x,y,self.que_hace))
            
    def actualizar_proyectiles(self,pantalla,lista_enemigos,jefe):
        i = 0
        while i < len(self.lista_proyectiles):
            p=self.lista_proyectiles[i]
            p.actualizar(pantalla)
            
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i = -1
            i += 1
            
            for enemigo in lista_enemigos:
                if p.rectangulo.colliderect(enemigo.rectangulo_principal):
                    lista_enemigos.remove(enemigo)
                    
            if jefe is not None:
                for enemigo in jefe:
                    if p.rectangulo.colliderect(enemigo.rectangulo_principal) and enemigo.inmune == False:
                        print(enemigo.vidas)
                        enemigo.vidas -= 1
                        print(enemigo.vidas)
                        enemigo.inmune = True
                        pygame.time.set_timer(pygame.USEREVENT,3000,1)
                        self.lista_proyectiles.remove(p)
                        if enemigo.vidas <=0:
                            jefe.remove(enemigo)
                        
