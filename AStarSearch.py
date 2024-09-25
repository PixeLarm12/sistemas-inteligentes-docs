# Busca A*
# O algoritmo A* combina a busca gulosa com o custo acumulado, escolhendo o caminho com o menor valor de f(n)=g(n)+h(n), onde 
# g(n) é o custo real do caminho e h(n) é a heurística.

def a_star(graph, start, goal, heuristic, cost):
    open_list = [(start, 0)]  # Lista de nós a explorar, com o custo total estimado
    g_cost = {start: 0}  # Custo acumulado até cada nó
    
    while open_list:
        current, _ = open_list.pop(0)  # Remove o nó com o menor custo f(n)
        
        if current == goal:  # Verifica se o objetivo foi alcançado
            return True
        
        for neighbor in graph[current]:
            temp_g_cost = g_cost[current] + cost[(current, neighbor)]  # Calcula o custo do caminho até o vizinho
            if neighbor not in g_cost or temp_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = temp_g_cost  # Atualiza o custo acumulado
                f_cost = temp_g_cost + heuristic[neighbor]  # Calcula o custo total f(n)
                open_list.append((neighbor, f_cost))  # Adiciona o vizinho à lista de exploração
        open_list.sort(key=lambda x: x[1])  # Ordena a lista pelo custo f(n)
    return False

# Exemplo de uso:
# cost = {('A', 'B'): 1, ('A', 'C'): 2, ('B', 'D'): 3, ('B', 'E'): 1, ('C', 'F'): 4}
# print(a_star(graph, 'A', 'E', heuristic, cost))  # Saída: True

