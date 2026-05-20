import folium
from leitor import LeitorJSON

def gerar_visualizacao():
    print("Carregando o grafo na memória...")
    caminho_nos = 'data/nos.json'
    caminho_arestas = 'data/arestas.json'
    
    grafo = LeitorJSON.carregar_grafo(caminho_nos, caminho_arestas)
    
    if not grafo.vertices:
        print("Erro: O grafo está vazio. Verifique os arquivos JSON.")
        return

    primeiro_vertice = next(iter(grafo.vertices.values()))
    
    print("Renderizando o mapa (isso pode levar alguns segundos)...")
    mapa = folium.Map(location=[primeiro_vertice.lat, primeiro_vertice.lon], zoom_start=15)

    for id_v, vertice in grafo.vertices.items():
        coord_origem = (vertice.lat, vertice.lon)
        
        folium.CircleMarker(
            location=coord_origem, 
            radius=1.5, 
            color='red', 
            fill=True, 
            fill_opacity=1
        ).add_to(mapa)

        for aresta in vertice.arestas:
            destino_vertice = grafo.vertices[aresta.destino]
            coord_destino = (destino_vertice.lat, destino_vertice.lon)
            
            folium.PolyLine(
                [coord_origem, coord_destino], 
                color="blue", 
                weight=2, 
                opacity=0.6
            ).add_to(mapa)

    nome_arquivo = "visualizacao_grafo.html"
    mapa.save(nome_arquivo)
    print(f"Visualização gerada com sucesso! Dê um duplo clique no arquivo '{nome_arquivo}' para abrir no navegador.")

if __name__ == "__main__":
    gerar_visualizacao_inicial()