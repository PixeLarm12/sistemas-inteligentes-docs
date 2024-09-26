# Busca em Profundidade Limitada
# Similar à busca em profundidade, mas com uma profundidade máxima limitada para evitar explorar níveis muito profundos desnecessariamente.

def dfs_limited(graph, start, goal, limit, depth=0):
    if start == goal:  # Verifica se o objetivo foi encontrado
        return True
    if depth >= limit:  # Verifica se o limite de profundidade foi alcançado
        return False
    
    # Explora os vizinhos do nó atual
    for neighbor in graph[start]:
        # Chama recursivamente com o incremento da profundidade
        if dfs_limited(graph, neighbor, goal, limit, depth + 1):
            return True
    return False