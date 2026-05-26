from leitor import LeitorJSON
from algoritmos import AnalisadorGrafo

def main():
    print("Iniciando carregamento do Grafo...")
    
    caminho_nos = 'data/nos.json'
    caminho_arestas = 'data/arestas.json'
    
    grafo = LeitorJSON.carregar_grafo(caminho_nos, caminho_arestas)
    
    total_vertices = len(grafo.vertices)
    print(f"Grafo carregado com sucesso! Total de vértices: {total_vertices}")

    id_origem = list(grafo.vertices.keys())[0] 
    id_destino = list(grafo.vertices.keys())[-1]

    print("Calculando Rota mais curta...")
    caminho, distancia_metros = AnalisadorGrafo.dijkstra(grafo, id_origem, id_destino)

    if caminho:
        print(f"Sucesso! A rota possui {distancia_metros:.2f} metros.")
        print(f"Nós percorridos: {len(caminho)}")
    else:
        print("Nenhum caminho encontrado.")

    print("\n--- ANÁLISE 1: CONECTIVIDADE ---")
    is_conexo, alcancados, total = AnalisadorGrafo.verificar_conectividade(grafo)
    if is_conexo:
        print(f"A malha viária é totalmente conexa! Todos os {total} cruzamentos estão interligados.")
    else:
        print(f"Atenção: A malha possui áreas isoladas. Foram alcançados apenas {alcancados} de {total} cruzamentos.")

    print("\n--- ANÁLISE 2: 5 MAIS CRUZAMENTOS CRÍTICOS ---")
    top_cruzamentos = AnalisadorGrafo.calcular_graus(grafo, top_n=5)
    for i, (id_v, grau) in enumerate(top_cruzamentos, 1):
        print(f"{i}º Lugar -> ID: {id_v} | Total de vias conectadas (Grau): {grau}")

    print("\n--- ANÁLISE 3: RESILIÊNCIA E VULNERABILIDADE (Simulação de Interdição) ---")
    id_origem = list(grafo.vertices.keys())[0] 
    id_destino = list(grafo.vertices.keys())[-1]

    caminho_original, dist_original = AnalisadorGrafo.dijkstra(grafo, id_origem, id_destino)
    
    if caminho_original:
        print(f"1. Rota Original calculada: {dist_original:.2f} metros ({len(caminho_original)} cruzamentos).")
        
        meio_do_caminho = len(caminho_original) // 2
        no_critico = caminho_original[meio_do_caminho]
        
        area_bloqueada = {no_critico}
        for aresta in grafo.vertices[no_critico].arestas:
            area_bloqueada.add(aresta.destino)
            
        print(f"2. Evento Crítico! Interditando o cruzamento {no_critico} e seus arredores ({len(area_bloqueada)} cruzamentos bloqueados).")
        
        caminho_novo, dist_nova = AnalisadorGrafo.dijkstra(grafo, id_origem, id_destino, nos_ignorados=area_bloqueada)
        
        if caminho_novo:
            aumento_metros = dist_nova - dist_original
            print(f"3. Rota de Desvio encontrada: {dist_nova:.2f} metros.")
            print(f"-> IMPACTO NA REDE: O trajeto aumentou em {aumento_metros:.2f} metros devido ao desvio.")
        else:
            print("-> IMPACTO NA REDE: COLAPSO. A área bloqueada era uma ponte vital. Origem e destino ficaram isolados.")

if __name__ == "__main__":
    main()