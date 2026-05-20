from src.leitor import LeitorJSON
from src.visualizador import gerar_visualizacao_inicial

def main():
    print("Iniciando carregamento do Grafo...")
    
    caminho_nos = 'data/nos.json'
    caminho_arestas = 'data/arestas.json'
    
    grafo = LeitorJSON.carregar_grafo(caminho_nos, caminho_arestas)
    
    total_vertices = len(grafo.vertices)
    print(f"Grafo carregado com sucesso! Total de vértices: {total_vertices}")
    
    print("\nGerando visualização do grafo...")
    gerar_visualizacao_inicial()

if __name__ == "__main__":
    main()