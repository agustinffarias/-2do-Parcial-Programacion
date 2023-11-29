from ClassNivel_dos import *
from ClassNivel_uno import *
from ClassNivel_tres import *


class Manejador_niveles():
    def __init__(self,pantalla):
        self.pantalla = pantalla 
        self.niveles = {"Nivel_uno": Nivel_uno,
                        "Nivel_dos":Nivel_dos,
                        "Nivel_tres":Nivel_tres}
    
    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self.niveles)