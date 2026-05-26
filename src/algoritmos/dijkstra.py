import heapq
from typing import Dict, List, Tuple, Optional

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def executar(self, inicio: int, destino: int, nos_ignorados: set = None) -> Tuple[Optional[List[int]], float]:
        import heapq
from typing import List, Tuple, Optional

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def executar(self, inicio: int, destino: int, nos_ignorados: set = None) -> Tuple[Optional[List[int]], float]:
        if nos_ignorados is None:
            nos_ignorados = set()

        if inicio not in self.grafo.vertices or destino not in self.grafo.vertices:
            return None, float('inf')

        distancias = {no: float('inf') for no in self.grafo.vertices}
        distancias[inicio] = 0.0
        predecessores = {no: None for no in self.grafo.vertices}
        fila_prioridade = [(0.0, inicio)]
        
        while fila_prioridade:
            dist_atual, no_atual = heapq.heappop(fila_prioridade)
            
            if no_atual == destino:
                break
            if dist_atual > distancias[no_atual]:
                continue
                
            for aresta in self.grafo.vertices[no_atual].arestas:
                vizinho = aresta.destino
                if vizinho in nos_ignorados:
                    continue
                    
                nova_dist = distancias[no_atual] + aresta.peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = no_atual
                    heapq.heappush(fila_prioridade, (nova_dist, vizinho))
                        
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
            
        return (caminho[::-1] if distancias[destino] != float('inf') else None), distancias[destino]