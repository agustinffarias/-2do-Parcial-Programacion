# def verificar_colision_jefe(self,jefe,PANTALLA):
    #     try:
    #         pygame.mixer.init()
    #     except pygame.error as e:
    #         print(f"Error al inicializar Pygame: {e}")
    #     for enemigo in jefe:
    #         if self.rectangulos["bottom"].colliderect(enemigo.rectangulos["top"]):
    #             enemigo.vidas -= 1
    #             enemigo.inmune = True 
    #             pygame.time.set_timer(pygame.USEREVENT,1300,1)
    #             if enemigo.vidas == 0:
    #                 print("HOLA")
    #                 enemigo.muriendo = True
    #                 self.puntos += 1000
    #                 enemigo.animacion_actual = enemigo.animaciones["Muriendo"]
    #                 enemigo.animar(PANTALLA)
    #                 if enemigo.rectangulo_principal.y >= PANTALLA.get_height():
    #                     enemigo.esta_muerto = True
    #                 jefe.remove(enemigo)
    #         if self.rectangulos["top"].colliderect(enemigo.rectangulos["bottom"]):
    #             sonido_ser_golpeado.play(loops=0)
    #             self.que_hace = "Golpeado"
    #             self.animacion_actual = self.animaciones[self.que_hace]
    #             self.animar(PANTALLA)
    #             self.perder_vida(PANTALLA)
    #         elif self.rectangulos["right"].colliderect(enemigo.rectangulos["left"]):
    #             sonido_ser_golpeado.play(loops=0)
    #             self.que_hace = "Golpeado"
    #             self.animacion_actual = self.animaciones[self.que_hace]
    #             self.animar(PANTALLA)
    #             self.perder_vida(PANTALLA)
    #         elif self.rectangulos["left"].colliderect(enemigo.rectangulos["right"]):
    #             sonido_ser_golpeado.play(loops=0)
    #             self.que_hace = "Golpeado"
    #             self.animacion_actual = self.animaciones[self.que_hace]
    #             self.animar(PANTALLA)
    #             self.perder_vida(PANTALLA)