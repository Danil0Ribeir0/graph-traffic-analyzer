from typing import List, Tuple, Optional
from grafo import Grafo
from algoritmos import AnalisadorGrafo

class GerenciadorAnalises:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def executar_analise_conectividade(self) -> None:
        print("\n--- ANÁLISE 1: CONECTIVIDADE DA MALHA ---")
        is_conexo, alcancados, total = AnalisadorGrafo.verificar_conectividade(self.grafo)
        if is_conexo:
            print(f"Resultado: A malha viária é totalmente conexa! Todos os {total} cruzamentos estão interligados.")
        else:
            print(f"Resultado: Atenção! A malha possui áreas isoladas estruturalmente.")
            print(f"Foram alcançados apenas {alcancados} de um total de {total} cruzamentos cadastrados.")

    def executar_analise_gargalos(self, top_n: int = 5) -> None:
        print(f"\n--- ANÁLISE 2: TOP {top_n} CRUZAMENTOS CRÍTICOS (GRAU) ---")
        top_cruzamentos = AnalisadorGrafo.calcular_graus(self.grafo, top_n=top_n)
        for i, (id_v, grau) in enumerate(top_cruzamentos, 1):
            print(f"{i}º Lugar -> Cruzamento ID: {id_v} | Vias Conectadas: {grau}")

    def executar_analise_resiliencia(self, id_origem: int, id_destino: int) -> None:
        print("\n--- ANÁLISE 3: RESILIÊNCIA E SIMULAÇÃO DE INTERDIÇÃO ---")
        
        caminho_original, dist_original = AnalisadorGrafo.dijkstra(self.grafo, id_origem, id_destino)
        
        if not caminho_original:
            print("Erro: Não foi possível estabelecer uma rota base entre os nós informados.")
            return
            
        print(f"1. Rota Original estável: {dist_original:.2f} metros ({len(caminho_original)} cruzamentos).")
        
        meio = len(caminho_original) // 2
        no_critico = caminho_original[meio]
        
        area_bloqueada = {no_critico}
        for aresta in self.grafo.vertices[no_critico].arestas:
            area_bloqueada.add(aresta.destino)
            
        print(f"2. Simulação: Evento crítico bloqueou o nó {no_critico} e arredores ({len(area_bloqueada)} cruzamentos fechados).")
        
        caminho_novo, dist_nova = AnalisadorGrafo.dijkstra(self.grafo, id_origem, id_destino, nos_ignorados=area_bloqueada)
        
        if caminho_novo:
            aumento = dist_nova - dist_original
            print(f"3. Rota Alternativa traçada: {dist_nova:.2f} metros.")
            print(f"-> Impacto: O trajeto sofreu um acréscimo de {aumento:.2f} metros devido ao desvio.")
        else:
            print("-> Impacto: COLAPSO DE FLUXO. A zona interditada isolou a origem do destino.")