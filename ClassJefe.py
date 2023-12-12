from config import *
from ClassDisparoJefe import *
import random
import pygame 
class Jefe:
    def __init__(self, animaciones,tamaño,x,y,que_hace) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.rectangulo_principal = self.animaciones[que_hace][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.que_hace = que_hace
        self.animacion_actual = self.animaciones[que_hace]
        self.esta_muerto = False
        self.pasos = 0
        self.muriendo = False
        self.velocidad_vertical = 0.1
        self.direccion_derecha = True
        self.rectangulos= obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        self.vidas = 4
        self.es_boss = True
        self.inmune = False
        self.lista_proyectiles = []
        self.tiempo_ultimo_disparo = 0
        
              
    def animar(self,pantalla):
        if self.que_hace == "Quieto":
            pantalla.blit(jefe_acciones["Quieto"][0],self.rectangulo_principal)
            
    def disparar_misiles(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo >= 7000:
            self.lanzar_proyectiles()
            self.tiempo_ultimo_disparo = tiempo_actual

    def lanzar_proyectiles(self):
        x = random.randint(0, 1100)
        y = 0

        for _ in range(10):
            self.lista_proyectiles.append(DisparoJefe(x, y, "Quieto"))
            

    def actualizar_proyectiles(self, pantalla,personaje_principal):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            p.actualizar(pantalla)

            if p.rectangulo.centery > pantalla.get_height():
                self.lista_proyectiles.pop(i)
                i = -1
            i += 1
            
            if p.rectangulo.colliderect(personaje_principal.rectangulo_principal):
                personaje_principal.perder_vida(pantalla)
                self.lista_proyectiles.remove(p)



            
    
    
    
    
    
    
    # def avanzar(self):
    #     # Actualizar la posición x de acuerdo con la dirección
    #     if self.direccion_derecha:
    #         for lado in self.rectangulos:
    #             self.rectangulos[lado].x += 2
    #     else:
    #         for lado in self.rectangulos:
    #             self.rectangulos[lado].x -= 2

    #     # Verificar si el enemigo llegó a los límites y, en ese caso, invertir la dirección
    #     if self.rectangulo_principal.right >= 1100 or self.rectangulo_principal.left <= 0:
    #         self.invertir_direccion()

    # def invertir_direccion(self):
    #     # Invertir la dirección del enemigo
    #     self.direccion_derecha = not self.direccion_derecha
    #     # Ajustar la posición x para evitar problemas de bucle
    #     if self.direccion_derecha:
    #         self.rectangulo_principal.x = 0
    #     else:
    #         self.rectangulo_principal.x = 1100 - self.rectangulo_principal.width
    #     # Invertir la imagen actual
    #     self.animacion_actual = invertir_imagen(self.animacion_actual)

    # def animar(self, pantalla):
    #     if self.que_hace == "Caminando":
    #         largo = len(self.animacion_actual)
    #         if self.pasos >= largo:
    #             self.pasos = 0
    #         pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
    #         self.pasos += 1

    #         if self.muriendo and self.pasos == largo and self.vidas == 0: # CAMBIE ESTO
    #             self.esta_muerto = True
        
    #     if self.que_hace == "Quieto":
    #         if self.tiempo_quieto == 0:
    #             self.tiempo_quieto = pygame.time.get_ticks()  # Iniciar el conteo de tiempo
    #         tiempo_transcurrido = pygame.time.get_ticks() - self.tiempo_quieto
    #         if tiempo_transcurrido < 5000:  # 5000 milisegundos (5 segundos)
    #             pantalla.blit(self.animacion_actual[0], self.rectangulo_principal)
    #         else:
    #             self.lanzar_proyectiles()  # Después de 5 segundos, lanzar proyectiles
    #             self.tiempo_quieto = 0  # Reiniciar el tiempo
 
    
    # def actualizar_avance(self, pantalla):
    #     tiempo_actual = pygame.time.get_ticks()
    #     if tiempo_actual % 10 == 0:
    #         pygame.time.set_timer(pygame.USEREVENT+2,5000,1)
    #     else:
    #         self.animar(pantalla)
    #         self.avanzar()
    
    # def quedarse_quieto(self):
    #     # El jefe se queda quieto y lanza proyectiles cada 10 segundos
    #     self.muriendo = False  # Para evitar que la animación de muerte afecte la animación de quedarse quieto
    #     self.animacion_actual = [self.animaciones["Quieto"][0]]  # Cambiar a la animación quieta
    #     self.tiempo_ultimo_quieto = pygame.time.get_ticks()  # Actualizar el tiempo de la última vez que se quedó quieto

    #     # Lanzar proyectiles al quedarse quieto
    #     self.lanzar_proyectiles()
        
    # def lanzar_proyectiles(self):
    #     x = None
    #     margen = 47
    #     y = self.rectangulo_principal.centery + 10

    #     if self.que_hace == "Quieto":
    #         for _ in range(5):  # Lanzar 5 proyectiles al quedarse quieto
    #             x = random.randint(0, 1100)
    #             # Cambiar la dirección de los proyectiles hacia abajo (en el eje y)
    #             self.lista_proyectiles.append(DisparoJefe(x, y, "Quieto", direccion=(0, 1)))
            
    # def actualizar_proyectiles(self, pantalla):
    #     i = 0
    #     while i < len(self.lista_proyectiles):
    #         p = self.lista_proyectiles[i]
    #         p.actualizar(pantalla)

    #         if p.rectangulo.centery > pantalla.get_height():
    #             self.lista_proyectiles.pop(i)
    #         else:
    #             i += 1
