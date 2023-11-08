from abstract_factory import AbstractFactory
from fabrica_concreta import FabricaConcreta1, FabricaConcreta2

def client_code(factory: AbstractFactory):
    producto_a = factory.crear_producto_1()
    producto_b = factory.crear_producto_2()
    print(f"{producto_a.funcion_util_a()}")
    print(f"{producto_b.funcion_util_b()}")
if __name__ == "__main__":
    factory1 = FabricaConcreta2()
    factory2 = FabricaConcreta1()

    client_code(factory1)
    client_code(factory2)