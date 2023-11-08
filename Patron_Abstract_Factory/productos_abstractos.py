from abc import ABC, abstractmethod

class ProductoAbstractoA(ABC):
    @abstractmethod
    def funcion_util_a(self):
        pass

class ProductoAbstractoB(ABC):
    @abstractmethod
    def funcion_util_b(self):
        pass