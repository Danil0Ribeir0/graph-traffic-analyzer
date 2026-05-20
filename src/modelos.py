from typing import List

class Aresta:
    def __init__(self, destino: int, peso: float, nome: str = ""):
        self.destino = destino
        self.peso = peso
        self.nome = nome

class Vertice:
    def __init__(self, id_vertice: int, lat: float, lon: float):
        self.id_vertice = id_vertice
        self.lat = lat
        self.lon = lon
        self.arestas: List[Aresta] = []

    def adicionar_aresta(self, aresta: Aresta):
        self.arestas.append(aresta)