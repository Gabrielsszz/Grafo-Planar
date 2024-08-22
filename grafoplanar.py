import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman

def detect_communities_girvan_newman(G):
    # Aplica o algoritmo Girvan-Newman
    comp = girvan_newman(G)
    
    # Obter o primeiro nível de divisão (a primeira comunidade encontrada)
    communities = next(comp)
    
    # Converte a lista de comunidades em um dicionário de comunidades
    community_dict = {}
    for i, community in enumerate(communities):
        for node in community:
            community_dict[node] = i

    # Organiza os nós em comunidades
    communities = {}
    for node, comm in community_dict.items():
        communities.setdefault(comm, []).append(node)

    return community_dict  # Retorna o dicionário de comunidade

# Criação do grafo
Graph = nx.Graph()

# Adiciona arestas ao grafo
Graph.add_edge('Clara', 'Maria')
Graph.add_edge('Maria', 'Marta')
Graph.add_edge('Marta', 'Andre')
Graph.add_edge('Andre', 'Marcos')
Graph.add_edge('Marcos', 'Pedro')
Graph.add_edge('Pedro', 'Felipe')
Graph.add_edge('Felipe', 'Alexandre')
Graph.add_edge('Alexandre', 'Gabriela')
Graph.add_edge('Gabriela', 'Lucas')
Graph.add_edge('Lucas', 'Nina')
Graph.add_edge('Nina', 'Pedro') 
Graph.add_edge('Nina', 'Sophia')

# Detectar comunidades
community_dict = detect_communities_girvan_newman(Graph)

# Criar uma lista de cores para cada nó baseado na comunidade
node_colors = [community_dict[node] for node in Graph.nodes()]

# Desenho do grafo
plt.figure(figsize=(10, 8))
plt.axis("off")
np.random.seed(0)
position = nx.spring_layout(Graph)

# Desenho dos nós e arestas
nx.draw_networkx_edges(Graph, pos=position)
nx.draw_networkx_nodes(Graph, pos=position, node_color=node_colors, cmap=plt.cm.viridis, node_size=500, alpha=0.8)
nx.draw_networkx_labels(Graph, pos=position, font_size=18, font_color='white')

# Exibe o grafo
plt.show()
