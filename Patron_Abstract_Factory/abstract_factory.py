from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def crear_producto_1(self):
        pass

    @abstractmethod
    def crear_producto_2(self):
        pass
    
    