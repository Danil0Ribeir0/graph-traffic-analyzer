import folium
from leitor import LeitorJSON
from algoritmos import AnalisadorGrafo

def gerar_visualizacao_analitica():
    print("Iniciando renderização analítica das camadas...")
    grafo = LeitorJSON.carregar_grafo('../data/nos.json', '../data/arestas.json')
    
    if not grafo.vertices:
        return

    id_origem = list(grafo.vertices.keys())[0]
    id_destino = list(grafo.vertices.keys())[-1]
    
    caminho_original, _ = AnalisadorGrafo.dijkstra(grafo, id_origem, id_destino)
    
    area_bloqueada = set()
    if caminho_original:
        no_critico = caminho_original[len(caminho_original) // 2]
        area_bloqueada.add(no_critico)
        for aresta in grafo.vertices[no_critico].arestas:
            area_bloqueada.add(aresta.destino)
            
    caminho_novo, _ = AnalisadorGrafo.dijkstra(grafo, id_origem, id_destino, area_bloqueada)

    inicio = grafo.vertices[id_origem]
    mapa = folium.Map(location=[inicio.lat, inicio.lon], zoom_start=14, tiles="CartoDB positron")

    fg_base = folium.FeatureGroup(name="Malha Viária Base", show=True)
    fg_bloqueio = folium.FeatureGroup(name="Área Interditada (Bairro Z)", show=True)
    fg_rota_original = folium.FeatureGroup(name="Rota Original", show=False) # Inicia desligada para não poluir
    fg_rota_nova = folium.FeatureGroup(name="Rota de Desvio (Resiliência)", show=True)

    for id_v, vertice in grafo.vertices.items():
        coord_origem = (vertice.lat, vertice.lon)
        for aresta in vertice.arestas:
            coord_destino = (grafo.vertices[aresta.destino].lat, grafo.vertices[aresta.destino].lon)
            folium.PolyLine([coord_origem, coord_destino], color="gray", weight=1, opacity=0.3).add_to(fg_base)

    if caminho_original:
        coords_originais = [(grafo.vertices[no].lat, grafo.vertices[no].lon) for no in caminho_original]
        folium.PolyLine(coords_originais, color="blue", weight=4, opacity=0.8, dash_array="10").add_to(fg_rota_original)

    for no_id in area_bloqueada:
        v = grafo.vertices[no_id]
        folium.CircleMarker(location=(v.lat, v.lon), radius=6, color='red', fill=True, fill_opacity=0.9).add_to(fg_bloqueio)

    if caminho_novo:
        coords_novas = [(grafo.vertices[no].lat, grafo.vertices[no].lon) for no in caminho_novo]
        folium.PolyLine(coords_novas, color="green", weight=5, opacity=1).add_to(fg_rota_nova)

    folium.Marker([inicio.lat, inicio.lon], popup="Origem", icon=folium.Icon(color="green")).add_to(mapa)
    folium.Marker([grafo.vertices[id_destino].lat, grafo.vertices[id_destino].lon], popup="Destino", icon=folium.Icon(color="black")).add_to(mapa)

    fg_base.add_to(mapa)
    fg_bloqueio.add_to(mapa)
    fg_rota_original.add_to(mapa)
    fg_rota_nova.add_to(mapa)
    
    folium.LayerControl().add_to(mapa)

    mapa.save("visualizacao_analitica.html")
    print("Mapa analítico com camadas gerado em: visualizacao_analitica.html")

if __name__ == "__main__":
    gerar_visualizacao_analitica()