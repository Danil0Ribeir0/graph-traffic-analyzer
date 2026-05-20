from typing import Dict
from modelos import Vertice, Aresta

class Grafo:
    def __init__(self):
        self.vertices: Dict[int, Vertice] = {}

    def adicionar_vertice(self, vertice: Vertice):
        if vertice.id_vertice not in self.vertices:
            self.vertices[vertice.id_vertice] = vertice

    def adicionar_aresta(self, origem: int, destino: int, peso: float, nome: str, mao_unica: bool):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].adicionar_aresta(Aresta(destino, peso, nome))
            
            if not mao_unica:
                self.vertices[destino].adicionar_aresta(Aresta(origem, peso, nome))