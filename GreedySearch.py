# Busca Gulosa
# A Busca Gulosa utiliza uma função heurística que estima a distância ao objetivo e sempre escolhe o caminho que parece mais promissor.

def greedy_search(graph, start, goal, heuristic):
    queue = [(start, heuristic[start])]  # Fila com os nós a explorar, ordenada pela heurística
    visited = set()  # Conjunto de nós visitados

    while queue:
        node, _ = queue.pop(0)  # Remove o nó com menor heurística
        if node == goal:  # Verifica se o objetivo foi encontrado
            return True
        visited.add(node)  # Marca o nó como visitado
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, heuristic[neighbor]))  # Adiciona o vizinho à fila
        queue.sort(key=lambda x: x[1])  # Ordena a fila pela heurística
    return False

# Exemplo de uso:
heuristic = {'A': 3, 'B': 2, 'C': 4, 'D': 6, 'E': 0, 'F': 5}  # Heurísticas estimadas para cada nó
print(greedy_search(graph, 'A', 'E', heuristic))  # Saída: True

