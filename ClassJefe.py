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
        self.vidas = 5
        self.es_boss = True
        self.inmune = False
        self.lista_proyectiles = []
        self.tiempo_ultimo_disparo = 0
        self.ubicaciones_random = [(308, 312),(447, 173),(220, 86),(959, 250),(765, 235),(818, 450),(44,450)]
        self.tiempo_cambio_posicion = 0
              
    def animar(self,pantalla):
        """
        Realiza la animación del jefe en la pantalla.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará la animación.

        - Si la acción actual del jefe es "Quieto", muestra la primera imagen de la animación "Quieto" en la posición del rectángulo principal del jefe.
        """
        if self.que_hace == "Quieto":
            pantalla.blit(jefe_acciones["Quieto"][0],self.rectangulo_principal)
            
    def disparar_misiles(self):
        """
        Realiza el disparo de misiles por parte del jefe.

        - Verifica si ha pasado el tiempo suficiente desde el último disparo.
        - Si ha pasado, invoca el método `lanzar_proyectiles`.
        """
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo >= 5000:
            self.lanzar_proyectiles()
            self.tiempo_ultimo_disparo = tiempo_actual

    def lanzar_proyectiles(self):
        """
        Lanza proyectiles (misiles) desde el jefe.

        - Genera coordenadas aleatorias para el lanzamiento de proyectiles.
        - Crea instancias, hasta 12, de la clase DisparoJefe en posiciones aleatorias y las agrega a la lista de proyectiles del jefe.
        """
        x = random.randint(0, 1100)
        y = 0

        for _ in range(12):
            self.lista_proyectiles.append(DisparoJefe(x, y, "Quieto"))
            

    def actualizar_proyectiles(self, pantalla,personaje_principal):
        """
        Actualiza la posición y realiza la animación de los proyectiles lanzados por el jefe.

        Parámetros:
        - pantalla: Superficie de la pantalla donde se dibujará la animación.
        - personaje_principal: Instancia del personaje principal para verificar colisiones.

        - Itera sobre la lista de proyectiles del jefe.
        - Actualiza y muestra cada proyectil en la pantalla.
        - Elimina los proyectiles que salen de la pantalla.
        - Verifica colisiones con el personaje principal y aplica las acciones correspondientes.
        """
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

    def cambiar_posicion(self):
        """
        Cambia la posición del jefe a una ubicación aleatoria predefinida.

        - Selecciona una ubicación aleatoria de la lista de ubicaciones aleatorias y ajusta la posición del jefe.
        """
        self.rectangulo_principal.x, self.rectangulo_principal.y = random.choice(self.ubicaciones_random)
