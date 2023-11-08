from __future__ import annotations
from typing import Any

class Producto_1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes de productos: {', '.join(self.parts)}", end="")
