from leitor import LeitorJSON
from visualizador import gerar_visualizacao
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

if __name__ == "__main__":
    main()