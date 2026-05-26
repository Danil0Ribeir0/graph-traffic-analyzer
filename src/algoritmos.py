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
    def dijkstra(grafo: Grafo, inicio: int, destino: int, nos_ignorados: set = None) -> Tuple[Optional[List[int]], float]:
        if nos_ignorados is None:
            nos_ignorados = set()

        if inicio not in grafo.vertices or destino not in grafo.vertices or inicio in nos_ignorados or destino in nos_ignorados:
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
                
                if vizinho in nos_ignorados:
                    continue
                    
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

    @staticmethod
    def verificar_conectividade(grafo: Grafo) -> Tuple[bool, int, int]:
        if not grafo.vertices:
            return False, 0, 0
            
        origem = list(grafo.vertices.keys())[0]
        
        visitados = {origem}
        fila = deque([origem])
        
        while fila:
            u = fila.popleft()
            for aresta in grafo.vertices[u].arestas:
                v = aresta.destino
                if v not in visitados:
                    visitados.add(v)
                    fila.append(v)
                    
        total_vertices = len(grafo.vertices)
        total_alcancado = len(visitados)
        
        is_conexo = (total_alcancado == total_vertices)
        return is_conexo, total_alcancado, total_vertices

    @staticmethod
    def calcular_graus(grafo: Grafo, top_n: int = 5) -> List[Tuple[int, int]]:
        graus = {v_id: 0 for v_id in grafo.vertices}
        
        for v_id, vertice in grafo.vertices.items():
            graus[v_id] += len(vertice.arestas)
            
            for aresta in vertice.arestas:
                if aresta.destino in graus:
                    graus[aresta.destino] += 1
                    
        def obter_grau(item: Tuple[int, int]) -> int:
            return item[1]
            
        top_vertices = sorted(graus.items(), key=obter_grau, reverse=True)
        
        return top_vertices[:top_n]