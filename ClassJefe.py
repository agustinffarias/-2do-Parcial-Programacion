from config import *
from ClassDisparoJefe import *
import random
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
        self.tiempo_ultimo_quieto = 0
              

    def avanzar(self):
        # Actualizar la posición x de acuerdo con la dirección
        if self.direccion_derecha:
            for lado in self.rectangulos:
                self.rectangulos[lado].x += 2
        else:
            for lado in self.rectangulos:
                self.rectangulos[lado].x -= 2

        # Verificar si el enemigo llegó a los límites y, en ese caso, invertir la dirección
        if self.rectangulo_principal.right >= 1100 or self.rectangulo_principal.left <= 0:
            self.invertir_direccion()

    def invertir_direccion(self):
        # Invertir la dirección del enemigo
        self.direccion_derecha = not self.direccion_derecha
        # Ajustar la posición x para evitar problemas de bucle
        if self.direccion_derecha:
            self.rectangulo_principal.x = 0
        else:
            self.rectangulo_principal.x = 1100 - self.rectangulo_principal.width
        # Invertir la imagen actual
        self.animacion_actual = invertir_imagen(self.animacion_actual)

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.pasos >= largo:
            self.pasos = 0
        pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
        self.pasos += 1

        if self.muriendo and self.pasos == largo and self.vidas == 0: # CAMBIE ESTO
            self.esta_muerto = True
    
    def actualizar_avance(self, pantalla):
        if not self.esta_muerto:
            tiempo_actual = pygame.time.get_ticks()

            # Si han pasado al menos 10 segundos desde la última vez que se quedó quieto
            if tiempo_actual - self.tiempo_ultimo_quieto >= 10000:
                self.quedarse_quieto()
            else:
                # Si no está quieto, anima y avanza
                self.animar(pantalla)
                self.avanzar()
    
    def quedarse_quieto(self):
        # El jefe se queda quieto y lanza proyectiles cada 10 segundos
        self.muriendo = False  # Para evitar que la animación de muerte afecte la animación de quedarse quieto
        self.animacion_actual = [self.animaciones["Quieto"][0]]  # Cambiar a la animación quieta
        self.tiempo_ultimo_quieto = pygame.time.get_ticks()  # Actualizar el tiempo de la última vez que se quedó quieto

        # Lanzar proyectiles al quedarse quieto
        self.lanzar_proyectiles()
        
    def lanzar_proyectiles(self):
        x = None
        margen = 47
        y = self.rectangulo_principal.centery + 10

        if self.que_hace == "Quieto":
            for _ in range(5):  # Lanzar 5 proyectiles al quedarse quieto
                x = random.randint(0, 1100)
                # Cambiar la dirección de los proyectiles hacia abajo (en el eje y)
                self.lista_proyectiles.append(DisparoJefe(x, y, "Caminando", direccion=(0, 1)))
            
    def actualizar_proyectiles(self,pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p=self.lista_proyectiles[i]
            p.actualizar(pantalla)
            
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i = -1
            i += 1
