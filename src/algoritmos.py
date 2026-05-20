import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional
from grafo import Grafo

class AnalisadorGrafo:
    
    @staticmethod
    def bfs(grafo: Grafo, origem: int, destino: int) -> Tuple[Optional[List[int]], Optional[str]]:
        if origem not in grafo.vertices or destino not in grafo.vertices:
            return None, "Origem ou destino não existem na base de dados."
            
        cor: Dict[int, str] = {no: 'BRANCO' for no in grafo.vertices}
        pai: Dict[int, Optional[int]] = {no: None for no in grafo.vertices}
     
        cor[origem] = 'CINZA'
        fila = deque([origem])
        encontrou_destino = False

        while fila:
            u = fila.popleft()

            if u == destino:
                encontrou_destino = True
                break

            for aresta in grafo.vertices[u].arestas:
                v = aresta.destino
                if cor[v] == 'BRANCO':
                    cor[v] = 'CINZA'
                    pai[v] = u
                    fila.append(v)
            
            cor[u] = 'PRETO'

        if encontrou_destino:
            caminho = []
            atual = destino
            
            while atual is not None:
                caminho.append(atual)
                atual = pai[atual]
                
            caminho.reverse()
            return caminho, None
            
        return None, "Não existe rota disponível entre os pontos informados."

    @staticmethod
    def dfs_iterativo(grafo: Grafo, origem: int, destino: int) -> Tuple[Optional[List[int]], Optional[int]]:
        if origem not in grafo.vertices or destino not in grafo.vertices:
            return None, None

        cor: Dict[int, str] = {v: 'BRANCO' for v in grafo.vertices}
        pai: Dict[int, Optional[int]] = {v: None for v in grafo.vertices}
        
        pilha = [origem]
        cor[origem] = 'CINZA' 
        
        while pilha:
            v = pilha.pop()
            
            if v == destino:
                caminho = []
                atual = destino
                while atual is not None:
                    caminho.append(atual)
                    atual = pai[atual]
                caminho.reverse()
                distancia = len(caminho) - 1
                return caminho, distancia
            
            for aresta in grafo.vertices[v].arestas:
                w = aresta.destino
                if cor[w] == 'BRANCO':
                    cor[w] = 'CINZA' 
                    pai[w] = v
                    pilha.append(w)
            
            cor[v] = 'PRETO'
        
        return None, None

    @staticmethod
    def dijkstra(grafo: Grafo, inicio: int, destino: int) -> Tuple[Optional[List[int]], float]:
        if inicio not in grafo.vertices or destino not in grafo.vertices:
            return None, float('inf')

        distancias: Dict[int, float] = {no: float('inf') for no in grafo.vertices}
        distancias[inicio] = 0.0
        predecessores: Dict[int, Optional[int]] = {no: None for no in grafo.vertices}
        
        fila_prioridade = [(0.0, inicio)]
        
        while fila_prioridade:
            dist_atual, no_atual = heapq.heappop(fila_prioridade)
            
            if no_atual == destino:
                break
                
            if dist_atual > distancias[no_atual]:
                continue
                
            for aresta in grafo.vertices[no_atual].arestas:
                vizinho = aresta.destino
                peso = aresta.peso
                
                nova_dist = distancias[no_atual] + peso
                
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    predecessores[vizinho] = no_atual
                    heapq.heappush(fila_prioridade, (nova_dist, vizinho))
                        
        if distancias[destino] == float('inf'):
            return None, float('inf')

        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
            
        return caminho[::-1], distancias[destino]