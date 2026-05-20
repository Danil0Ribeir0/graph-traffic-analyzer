import json
from grafo import Grafo
from modelos import Vertice

class LeitorJSON:
    @staticmethod
    def carregar_grafo(caminho_nos: str, caminho_arestas: str) -> Grafo:
        grafo = Grafo()

        with open(caminho_nos, 'r', encoding='utf-8') as f:
            nos = json.load(f)
            for no in nos:
                vertice = Vertice(no['id'], no['lat'], no['lon'])
                grafo.adicionar_vertice(vertice)

        with open(caminho_arestas, 'r', encoding='utf-8') as f:
            arestas = json.load(f)
            for aresta in arestas:
                grafo.adicionar_aresta(
                    origem=aresta['origem'],
                    destino=aresta['destino'],
                    peso=aresta['distancia'],
                    nome=aresta['nome'],
                    mao_unica=aresta['mao_unica']
                )

        return grafo