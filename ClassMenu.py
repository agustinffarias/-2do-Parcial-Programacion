import pygame
from constantes import *

class Menu:
    def __init__(self):
        self.opciones = ["Iniciar Juego", "Modificar Volumen", "Salir"]
        self.opcion_seleccionada = 0
        self.fuente = pygame.font.Font(None, 36)

    def dibujar(self, pantalla):
        pantalla.fill(BLANCO)  # Color de fondo del menú

        for i, opcion in enumerate(self.opciones):
            color = (0, 255, 0) if i == self.opcion_seleccionada else (255, 255, 255)
            texto = self.fuente.render(opcion, True, color)
            x = W // 2 - texto.get_width() // 2
            y = H // 2 - len(self.opciones) * texto.get_height() // 2 + i * 50
            pantalla.blit(texto, (x, y))

    def manejar_evento_teclado(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
            elif evento.key == pygame.K_DOWN:
                self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
            elif evento.key == pygame.K_RETURN:
                if self.opcion_seleccionada == 0:
                    print("Iniciar Juego")
                    # Lógica para iniciar el juego
                elif self.opcion_seleccionada == 1:
                    print("Modificar Volumen")
                    # Lógica para modificar volumen
                elif self.opcion_seleccionada == 2:
                    pygame.quit()
                    quit()