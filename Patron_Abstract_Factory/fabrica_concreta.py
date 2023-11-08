from abstract_factory import AbstractFactory
from productos_concretos import CrearProducto1A, CrearProducto1B, CrearProducto2A, CrearProducto2B

class FabricaConcreta1(AbstractFactory):
    def crear_producto_1(self):
        return CrearProducto1A()

    def crear_producto_2(self):
        return CrearProducto1B()

class FabricaConcreta2(AbstractFactory):
    def crear_producto_1(self):
        return CrearProducto2A()

    def crear_producto_2(self):
        return CrearProducto2B()