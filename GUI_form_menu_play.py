from GUI.GUI_buttom_image import *
from GUI.GUI_form import Form
from GUI_form_contenedor_nivel import *
from ManejadorNiveles import *

class FormMenuPlay(Form):
    def __init__(self,screen,x,y,w,h,color_background,color_border,active,path_image):
        super().__init__(screen,x,y,w,h,color_background,color_border,active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self.btn_level_uno =  Button_Image(screen=self._slave,
                                           master_x=x,
                                           master_y=y,
                                           x=50,
                                           y=120,
                                           w=100,
                                           h=50,
                                           path_image=r"GUI\recursos\1.png",
                                           onclick=self.entrar_nivel,
                                           onclick_param="nivel_uno",
                                           color_border="black")

        self.btn_level_dos =  Button_Image(screen=self._slave,
                                           master_x=x,
                                           master_y=y,
                                           x=50,
                                           y=220,
                                           w=100,
                                           h=50,
                                           path_image=r"GUI\recursos\2.png",
                                           onclick=self.entrar_nivel,
                                           onclick_param="nivel_dos",
                                           color_border="black")
        self.btn_level_tres =  Button_Image(screen=self._slave,
                                           master_x=x,
                                           master_y=y,
                                           x=50,
                                           y=320,
                                           w=100,
                                           h=50,
                                           path_image=r"GUI\recursos\3.png",
                                           onclick=self.entrar_nivel,
                                           onclick_param="nivel_tres",
                                           color_border="black")
        
        self.btn_home = Button_Image(screen=self._slave,
                                           master_x=x,
                                           master_y=y,
                                           x=450,
                                           y=490,
                                           w=35,
                                           h=35,
                                           path_image=r"GUI\recursos\casita.png",
                                           onclick=self.btn_home_click,
                                           onclick_param="",
                                           color_border="black")
        self.lista_widgets.append(self.btn_level_uno)
        self.lista_widgets.append(self.btn_level_dos)
        self.lista_widgets.append(self.btn_level_tres)
        self.lista_widgets.append(self.btn_home)

    def on(self,parametro):
        print("Hola",parametro)
        
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._slave.fill(self._color_background)

    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.lista_widgets.append(frm_contenedor_nivel)
        self.show_dialog(frm_contenedor_nivel)
        
    def btn_home_click(self,param):
        self.end_dialog()