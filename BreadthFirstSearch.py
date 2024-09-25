# Busca em Largura (BFS - Breadth First Search)
# A Busca em Largura explora o grafo nível a nível, garantindo encontrar a solução mais próxima do nó inicial.

from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])  # Inicializa a fila com o nó inicial
    visited = set([start])  # Conjunto para manter o controle dos nós visitados
    
    while queue:
        node = queue.popleft()  # Remove o primeiro nó da fila
        if node == goal:  # Verifica se o objetivo foi alcançado
            return True
        # Explora os vizinhos do nó atual
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Marca como visitado
                queue.append(neighbor)  # Adiciona o vizinho à fila
    return False

# Exemplo de uso:
print(bfs(graph, 'A', 'E'))  # Saída: True