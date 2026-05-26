from collections import deque
from typing import Dict, List, Tuple, Optional
from modelos import Vertice, Aresta

class Grafo:
    def __init__(self):
        self.vertices: Dict[int, Vertice] = {}

    def adicionar_vertice(self, vertice: Vertice) -> None:
        if vertice.id not in self.vertices:
            self.vertices[vertice.id] = vertice

    def adicionar_aresta(self, origem: int, destino: int, peso: float, nome: str = "Desconhecido", mao_unica: bool = False) -> None:
        if origem in self.vertices and destino in self.vertices:
            aresta = Aresta(origem, destino, peso, nome, mao_unica)
            self.vertices[origem].adicionar_aresta(aresta)
            
            if not mao_unica:
                aresta_inversa = Aresta(destino, origem, peso, nome, mao_unica)
                self.vertices[destino].adicionar_aresta(aresta_inversa)


    def verificar_conectividade(self) -> Tuple[bool, int, int]:
        if not self.vertices:
            return False, 0, 0
            
        origem = list(self.vertices.keys())[0]
        
        visitados = {origem}
        fila = deque([origem])
        
        while fila:
            u = fila.popleft()
            for aresta in self.vertices[u].arestas:
                v = aresta.destino
                if v not in visitados:
                    visitados.add(v)
                    fila.append(v)
                    
        total_vertices = len(self.vertices)
        total_alcancado = len(visitados)
        
        is_conexo = (total_alcancado == total_vertices)
        return is_conexo, total_alcancado, total_vertices

    def calcular_graus(self, top_n: int = 5) -> List[Tuple[int, int]]:
        graus = {v_id: 0 for v_id in self.vertices}
        
        for v_id, vertice in self.vertices.items():
            graus[v_id] += len(vertice.arestas)
            
            for aresta in vertice.arestas:
                if aresta.destino in graus:
                    graus[aresta.destino] += 1
                    
        def obter_grau_vertice(item: Tuple[int, int]) -> int:
            return item[1]
            
        top_vertices = sorted(graus.items(), key=obter_grau_vertice, reverse=True)
        return top_vertices[:top_n]