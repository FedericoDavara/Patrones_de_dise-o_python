from creador import Creador
from producto import Producto_Concreto_1, Producto_Concreto_2

class Creador_Concreto_1(Creador):
    def factory_method(self):
        return Producto_Concreto_1()

class Creador_Concreto_2(Creador):
    def factory_method(self):
        return Producto_Concreto_2()