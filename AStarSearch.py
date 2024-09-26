# Busca A*
# O algoritmo A* combina a busca gulosa com o custo acumulado, escolhendo o caminho com o menor valor de f(n)=g(n)+h(n), onde 
# g(n) é o custo real do caminho e h(n) é a heurística.

def a_star(graph, start, goal, heuristic, cost):
    open_list = [(start, 0)]  # Lista de nós a explorar, com o custo total estimado
    g_cost = {start: 0}  # Custo acumulado até cada nó
    came_from = {}  # Para armazenar o caminho

    while open_list:
        # Remove o nó com o menor custo f(n)
        current, _ = open_list.pop(0)

        # Verifica se o objetivo foi alcançado
        if current == goal:
            return True

        # Explora os vizinhos do nó atual
        for neighbor in graph[current]:
            # Calcula o custo do caminho até o vizinho
            temp_g_cost = g_cost[current] + cost[(current, neighbor)]
            
            # Se o vizinho ainda não foi visitado ou encontrou um caminho mais curto
            if neighbor not in g_cost or temp_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = temp_g_cost  # Atualiza o custo acumulado
                f_cost = temp_g_cost + heuristic[neighbor]  # Calcula o custo total f(n)
                open_list.append((neighbor, f_cost))  # Adiciona o vizinho à lista de exploração
                came_from[neighbor] = current  # Armazena de onde veio o vizinho

        # Ordena a lista pelo custo f(n)
        open_list.sort(key=lambda x: x[1])

    # Se a lista estiver vazia e o objetivo não foi alcançado
    return False

# Exemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'D'): 3,
    ('B', 'E'): 1,
    ('C', 'F'): 4
}

print(a_star(graph, 'A', 'E', heuristic, cost))  # Saída: True


