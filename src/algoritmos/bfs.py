from collections import deque
from typing import Dict, List, Tuple, Optional
from grafo import Grafo

class BFS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def executar(self, origem: int, destino: int) -> Tuple[Optional[List[int]], Optional[str]]:
        if origem not in self.grafo.vertices or destino not in self.grafo.vertices:
            return None, "Origem ou destino não existem na base de dados."
            
        cor: Dict[int, str] = {no: 'BRANCO' for no in self.grafo.vertices}
        pai: Dict[int, Optional[int]] = {no: None for no in self.grafo.vertices}
     
        cor[origem] = 'CINZA'
        fila = deque([origem])
        encontrou_destino = False

        while fila:
            u = fila.popleft()

            if u == destino:
                encontrou_destino = True
                break

            for aresta in self.grafo.vertices[u].arestas:
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