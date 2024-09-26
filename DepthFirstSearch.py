# Busca em Profundidade (DFS - Depth First Search)
# A Busca em Profundidade explora o grafo avançando o máximo possível por cada ramificação antes de retroceder. 
# Funciona bem para grafos com soluções mais profundas.

def dfs(graph, start, goal, visited=None):
    if visited is None:  # Inicializa o conjunto de visitados na primeira chamada
        visited = set()
    visited.add(start)  # Marca o nó atual como visitado
    
    if start == goal:  # Verifica se o objetivo foi encontrado
        return True
    
    # Explora os vizinhos não visitados
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Chama recursivamente para continuar explorando o caminho
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

# Exemplo de uso:
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
# print(dfs(graph, 'A', 'E'))  # Saída: True

