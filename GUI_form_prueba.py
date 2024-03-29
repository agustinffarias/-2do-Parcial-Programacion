import pygame
import json
from pygame.locals import *
from constantes import *
from GUI.GUI_buttom import *
from GUI.GUI_slider import *
from GUI.GUI_textbox import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_buttom_image import *
from GUI_form_score_menu import *
from GUI_form_menu_play import *

class FormPrueba(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        
        self.resultados = []
        self.flag_player = True
        self.volumen = 0.2 
        pygame.mixer.init()
        pygame.mixer.music.load(r"sonidos\fondo_nivel_2.mp3")
        pygame.mixer.music.play(-1)


        ##COMPLETAR
        #master y slave refiere a que un formulario depende de otro, y esto puede repetise
        self.txt_nombre = TextBox(self._slave, x,y, 275,25,400,50,"gray", "white", NEGRO, "blue", 5, r"fuente\PressStart2P-Regular.ttf", 35,"black")
        
        self.btn_play = Button(self._slave, x , y,
                            100,100,100,50, 
                            NARANJA, plata, 
                            self.btn_play_click,#on clik espera una funcion
                            "hola", "Pausa", r"fuente\PressStart2P-Regular.ttf", 15, "white")

        self.slider_volumen = Slider(self._slave, x,y, 100,300,500,10, self.volumen,gris_oscuro, "white")
        
        porcentaje_volumen= f"{self.volumen * 100}%" 
        #CAMBIAR POR UNA IMAGEN MEJOR ! ! ! 
        self.label_volumen = Label(self._slave, 650, 190, 100,50, porcentaje_volumen,"Comic Sans MS", 15, "white", r"GUI\recursos\Table.png")#

        # FORMULARIO DE TRANSICION
        #CAMBIAR POR UNA IMAGEN MEJOR ! ! ! 
        self.btn_tabla = Button_Image(self._slave, x, y,225,100,50,50,r"GUI\recursos\Menu_BTN.png", self.btn_tabla_click, "")
        
        self.btn_niveles = Button_Image(self._slave,x,y,300,100,120,50,r"GUI\recursos\level.jpg",self.mostrar_niveles, "")
        

        #HAY QUE AGRAGAR EL WIDGET A LA LISTA PARA QUE SE VEA 
        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla )
        self.lista_widgets.append(self.btn_niveles)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)#POLIMORFISMO (CADA WIDGET SE ACTUALIZA DE MANERA DIFERENTE)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
    def mostrar_niveles(self,param):
        form_niveles = FormMenuPlay(screen = self._master,
                                x = 250,
                                y = 25,
                                w = 500,
                                h = 550,
                                color_background = "green",
                                color_border = "gold",
                                active = True,
                                path_image= r"GUI\recursos\Window.png")
        self.render()
        self.show_dialog(form_niveles)
    
    def btn_play_click(self, param):
        if self.flag_player:
            pygame.mixer.music.pause()
            self.btn_play._color_background = plata
            self.btn_play.set_text("Play") #metodo de la clase
        else:
            pygame.mixer.music.unpause()#si pusiera play se reinicia
            self.btn_play._color_background = NARANJA
            self.btn_play.set_text("Pause") #metodo de la clase
        
        self.flag_player = not self.flag_player #niega

    def btn_tabla_click(self, param):
        
        archivo = open()

        # Crea y muestra el nuevo formulario con los resultados actualizados
        nuevo_form = FormMenuScore(
            screen=self._master,
            x=250,
            y=25,
            w=500,
            h=550,
            color_background="green",
            color_border="gold",
            active=True,
            path_image=r"GUI\recursos\Window.png",
            scoreboard=self.resultados,
            margen_x=10,
            margen_y=100,
            espacio=10,
        )

        self.show_dialog(nuevo_form)