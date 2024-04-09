from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.elementos: List[Elemento] = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        for elem in self.elementos:
            if elem == elemento:
                return True
        return False

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto: "Conjunto"):
        for elem in otro_conjunto.elementos:
            if not self.contiene(elem):
                self.agregar_elemento(elem)

    def __add__(self, otro_conjunto: "Conjunto"):
        resultado = Conjunto(f"{self.nombre} + {otro_conjunto.nombre}")
        resultado.elementos.extend(self.elementos)
        for elem in otro_conjunto.elementos:
            if not resultado.contiene(elem):
                resultado.agregar_elemento(elem)
        return resultado

    @staticmethod
    def intersectar(conjunto1: "Conjunto", conjunto2: "Conjunto") -> "Conjunto":
        resultado = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elem in conjunto1.elementos:
            if conjunto2.contiene(elem) and not resultado.contiene(elem):
                resultado.agregar_elemento(elem)
        return resultado

    def __str__(self) -> str:
        elementos_str = ", ".join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"