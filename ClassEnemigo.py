from config import *

class Enemigo:
    def __init__(self, animaciones,tamaño,x,y,que_hace) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones,*tamaño)
        self.rectangulo_principal = self.animaciones[que_hace][0].get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.animacion_actual = self.animaciones[que_hace]
        self.esta_muerto = False
        self.pasos = 0
        self.muriendo = False
        self.velocidad_vertical = 0.1
        self.bandera_vuelo = True
        self.es_boss = False
        self.direccion_derecha = True
        self.rectangulos= obtener_rectangulos(self.rectangulo_principal,tamaño[0],tamaño[1])
        
    
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

    
    def volar(self):
        if self.bandera_vuelo:
            for lado in self.rectangulos:
                self.rectangulos[lado].y += -1

            if self.rectangulo_principal.y <= 20:
                self.bandera_vuelo = False
        else:
            for lado in self.rectangulos:
                self.rectangulos[lado].y += 1
                if self.rectangulo_principal.y >= 130:
                    
                    self.bandera_vuelo = True
        
            
    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.pasos >= largo:
            self.pasos = 0
        
        pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
        self.pasos += 1

        if self.muriendo and self.pasos == largo:
            self.esta_muerto = True

    def actualizar_vuelo(self,pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.volar()
    
    def actualizar_avance(self,pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar()
        



