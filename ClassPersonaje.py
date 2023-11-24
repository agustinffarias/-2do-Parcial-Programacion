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
        self.potencia_salto = -20
        self.limite_velocidad_salto = 10
        self.gravedad = 1
        self.esta_saltando = False
        self.direccion_derecha = True
        self.direccion_izquierda = False
        self.ultima_direccion = "Derecha"
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        self.vida_actual = 5

    def actualizar(self, pantalla, plataforma):
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
        self.aplicar_gravedad(pantalla, plataforma)
        self.animar(pantalla)
        
    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rectangulo_principal)
        self.contador_pasos += 1

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
            else:
                self.esta_saltando = True

    def muere(self):
        if self.vida_actual == 0:
            pygame.quit()        
    
    def verificar_colision_enemigo(self, enemigos, PANTALLA):
        for enemigo in enemigos:
            if self.rectangulos["bottom"].colliderect(enemigo.rectangulos["top"]):
                enemigo.muriendo = True
                enemigo.animacion_actual = enemigo.animaciones["Muriendo"]
                enemigo.animar(PANTALLA)
                if enemigo.rectangulo_principal.y >= PANTALLA.get_height():
                    enemigo.esta_muerto = True
                enemigos.remove(enemigo)
            if self.rectangulos["top"].colliderect(enemigo.rectangulos["bottom"]):
                self.vida = -1
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
            if (self.rectangulos["right"]).colliderect(enemigo.rectangulos["left"]):
                self.vida = -1
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
            if (self.rectangulos["left"]).colliderect(enemigo.rectangulos["right"]):
                self.vida = -1
                self.que_hace = "Golpeado"
                self.animacion_actual = self.animaciones[self.que_hace]
                self.animar(PANTALLA)
    def animar_golpe(self):
        pass
    def muere(self):
        if self.vida_actual == 0:
            pygame.quit()       
        
    def perder_vida(self):
        pass
    def verificar_colision_plataforma(self):
        pass
    
    def verificar_colision_premio(self,premios,PANTALLA):
        for premio in premios:
            if self.rectangulo_principal.colliderect(premio.rectangulo_principal):
                premio.animacion_actual = premio.animaciones["Obtenido"]
                premio.animar(PANTALLA)
        
        
    