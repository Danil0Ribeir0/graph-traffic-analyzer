from leitor import LeitorJSON
from analises import GerenciadorAnalises

def main():
    print("====================================================")
    print("SISTEMA DE ANÁLISE DE TRÁFEGO E RESILIÊNCIA URBANA")
    print("====================================================")
    
    bairros = [
        "Edson Queiroz, Fortaleza, Ceará, Brasil",
        "Guararapes, Fortaleza, Ceará, Brasil",
        "Cocó, Fortaleza, Ceará, Brasil"
    ]
    
    grafo = LeitorJSON.carregar_grafo('data/nos.json', 'data/arestas.json', bairros)
    print(f"Grafo carregado com sucesso! Estrutura nativa com {len(grafo.vertices)} vértices.")
    
    analisador = GerenciadorAnalises(grafo)
    
    analisador.executar_analise_conectividade()
    analisador.executar_analise_gargalos(top_n=5)
    
    if grafo.vertices:
        pontos_validos = list(grafo.vertices.keys())
        origem_teste = pontos_validos[0]
        destino_teste = pontos_validos[-1]
        analisador.executar_analise_resiliencia(origem_teste, destino_teste)

if __name__ == "__main__":
    main()