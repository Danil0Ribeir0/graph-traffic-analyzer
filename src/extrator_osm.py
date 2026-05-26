import osmnx as ox
import json

def extrair_dados_malha_viaria(locais):
    print(f"Baixando dados da malha viária para: {locais}...")
    
    G = ox.graph_from_place(locais, network_type='drive')
    
    print("Processando nós (cruzamentos) e arestas (ruas)...")
    
    nos = []
    for no_id, dados in G.nodes(data=True):
        nos.append({
            "id": no_id,
            "lat": dados['y'],
            "lon": dados['x']
        })
        
    arestas = []
    for origem, destino, dados in G.edges(data=True):
        arestas.append({
            "origem": origem,
            "destino": destino,
            "distancia": round(dados.get('length', 0.0), 2),
            "mao_unica": dados.get('oneway', False),
            "nome": dados.get('name', 'Desconhecido')
        })
        
    with open('nos.json', 'w', encoding='utf-8') as f:
        json.dump(nos, f, ensure_ascii=False, indent=4)
        
    with open('arestas.json', 'w', encoding='utf-8') as f:
        json.dump(arestas, f, ensure_ascii=False, indent=4)
        
    print(f"Extração concluída! {len(nos)} nós e {len(arestas)} arestas salvos.")

if __name__ == "__main__":
    bairros_alvo = [
        "Edson Queiroz, Fortaleza, Ceará, Brasil",
        "Guararapes, Fortaleza, Ceará, Brasil",
        "Cocó, Fortaleza, Ceará, Brasil"
    ]
    
    extrair_dados_malha_viaria(bairros_alvo)