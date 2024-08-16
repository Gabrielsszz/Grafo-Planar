import networkx as nx

def detect_communities(G, min_size, density_threshold):
    """Detecta comunidades em um grafo utilizando o método de densidade.

    Args:
        G: O grafo de entrada.
        min_size: O tamanho mínimo de uma comunidade.
        density_threshold: O limiar de densidade para considerar duas comunidades como uma única comunidade.

    Returns:
        Um dicionário onde as chaves são os nós e os valores são os IDs das comunidades.
    """

    communities = {node: i for i, node in enumerate(G.nodes)}  # Inicializa cada nó como uma comunidade diferente

    while True:
        merged = False
        for node1 in G.nodes:
            for node2 in G.neighbors(node1):
                if communities[node1] != communities[node2]:
                    community1 = [n for n in G.nodes if communities[n] == communities[node1]]
                    community2 = [n for n in G.nodes if communities[n] == communities[node2]]
                    if len(community1) >= min_size and len(community2) >= min_size:
                        density = nx.density(G.subgraph(community1 | community2))
                        if density > density_threshold:
                            new_community = max(communities.values()) + 1
                            for node in community1 | community2:
                                communities[node] = new_community
                            merged = True
                            break
                if merged:
                    break
            if merged:
                break
        if not merged:
            break

    return communities
