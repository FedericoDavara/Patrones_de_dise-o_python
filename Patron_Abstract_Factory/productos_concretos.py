from productos_abstractos import ProductoAbstractoA, ProductoAbstractoB

class CrearProducto1A(ProductoAbstractoA):
    def funcion_util_a(self):
        return "Resultado 1A en Producto 1A"

class CrearProducto2A(ProductoAbstractoA):
    def funcion_util_a(self):
        return "Resultado 2A en Producto 2A"

class CrearProducto1B(ProductoAbstractoB):
    def funcion_util_b(self):
        return "Resultado 1B en Producto 1B"

class CrearProducto2B(ProductoAbstractoB):
    def funcion_util_b(self):
        return "Resultado 2B en Producto 2B"