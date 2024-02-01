from config import *
import random
class Enemigo:
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
        self.es_boss = False
        self.bandera_vuelo = True
        self.direccion_derecha = True
        self.rectangulos= obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
              
    def avanzar(self):
        """
        Avanza la posición del enemigo en la dirección actual.

        - Si el enemigo se mueve hacia la derecha, incrementa la posición x de sus rectángulos.
        - Si el enemigo se mueve hacia la izquierda, decrementa la posición x de sus rectángulos.

        Si el enemigo llega a los límites de la pantalla, invierte su dirección.
        """
        if self.direccion_derecha:
            for lado in self.rectangulos:
                self.rectangulos[lado].x += 2
        else:
            for lado in self.rectangulos:
                self.rectangulos[lado].x -= 2

        # Verifica si el enemigo llegó a los límites e invierte la dirección
        if self.rectangulo_principal.right >= 1100 or self.rectangulo_principal.left <= 0:
            self.invertir_direccion()

    def invertir_direccion(self):
        """
        Invierte la dirección del enemigo.

        - Cambia la dirección horizontal del enemigo.
        - Ajusta la posición x del rectángulo principal y de las imágenes.
        - Invierte la imagen actual del enemigo.
        """
        self.direccion_derecha = not self.direccion_derecha
        if self.direccion_derecha:
            self.rectangulo_principal.x = 0
        else:
            self.rectangulo_principal.x = 1100 - self.rectangulo_principal.width
        # Invertir la imagen actual
        self.animacion_actual = invertir_imagen(self.animacion_actual)

    def volar(self):
        """
        Hace que el enemigo realice un movimiento de vuelo.

        - Si la bandera de vuelo es True, mueve los rectángulos hacia arriba.
        - Si la posición y del enemigo es menor o igual a 20, cambia la bandera de vuelo a False.
        - Si la bandera de vuelo es False, mueve los rectángulos hacia abajo.
        - Si la posición y del enemigo es mayor o igual a 160, cambia la bandera de vuelo a True.
        """
        if self.bandera_vuelo:
            for lado in self.rectangulos:
                self.rectangulos[lado].y += -1

            if self.rectangulo_principal.y <= 20:
                self.bandera_vuelo = False
        else:
            for lado in self.rectangulos:
                self.rectangulos[lado].y += 1
                if self.rectangulo_principal.y >= 160:
                    
                    self.bandera_vuelo = True
    
    def animar(self, pantalla):
        """
        Realiza la animación del enemigo en la pantalla.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará la animación.

        - Muestra la imagen actual del enemigo en la posición del rectángulo principal.
        - Incrementa el contador de pasos para la animación.

        Si el enemigo está en proceso de morir y se completa la animación, marca al enemigo como muerto.
        """
        largo = len(self.animacion_actual)
        if self.pasos >= largo:
            self.pasos = 0
        
        pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
        self.pasos += 1

        if self.muriendo and self.pasos == largo:
            self.esta_muerto = True

    def actualizar_vuelo(self,pantalla):
        """
        Actualiza la posición y realiza la animación del enemigo en modo vuelo.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará la animación.

        - Si el enemigo no está muerto, realiza la animación y actualiza la posición de vuelo.
        """
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.volar()
    
    def actualizar_avance(self,pantalla):
        """
        Actualiza la posición y realiza la animación del enemigo en modo avance.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará la animación.

        - Si el enemigo no está muerto, realiza la animación y avanza la posición horizontal.
        """
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar()
            

        
        
        
        
        


