from abc import ABC, abstractmethod

class Creador(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        producto = self.factory_method()
        return f"Creando el {producto.operation()}"