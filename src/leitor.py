import json
import os
from grafo import Grafo
from modelos import Vertice
from extrator_osm import extrair_dados_malha_viaria

class LeitorJSON:
    @staticmethod
    def carregar_grafo(caminho_nos: str, caminho_arestas: str, bairros_alvo: list = None) -> Grafo:
        if not os.path.exists(caminho_nos) or not os.path.exists(caminho_arestas):
            print("Arquivos de dados não encontrados localmente.")
            print("Iniciando extração automática via API do OpenStreetMap...")
            
            os.makedirs(os.path.dirname(caminho_nos), exist_ok=True)
            
            if not bairros_alvo:
                bairros_alvo = ["Edson Queiroz, Fortaleza, Ceará, Brasil"]
                
            extrair_dados_malha_viaria(bairros_alvo)

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