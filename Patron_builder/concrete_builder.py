from __future__ import annotations
from builder import Builder
from producto_1 import Producto_1
class ConcreteBuilder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Producto_1()

    @property
    def product(self) -> Producto_1:

        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("ParteA1")

    def produce_part_b(self) -> None:
        self._product.add("ParteB1")

    def produce_part_c(self) -> None:
        self._product.add("ParteC1")