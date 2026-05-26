from typing import Dict, List, Tuple, Optional
from grafo import Grafo

class DFS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def executar(self, origem: int, destino: int) -> Tuple[Optional[List[int]], Optional[int]]:
        if origem not in self.grafo.vertices or destino not in self.grafo.vertices:
            return None, None

        cor: Dict[int, str] = {v: 'BRANCO' for v in self.grafo.vertices}
        pai: Dict[int, Optional[int]] = {v: None for v in self.grafo.vertices}
        
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
            
            for aresta in self.grafo.vertices[v].arestas:
                w = aresta.destino
                if cor[w] == 'BRANCO':
                    cor[w] = 'CINZA' 
                    pai[w] = v
                    pilha.append(w)
            
            cor[v] = 'PRETO'
        
        return None, None