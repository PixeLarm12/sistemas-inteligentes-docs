# Busca em Profundidade Iterativa
# Aplica a busca em profundidade repetidamente, aumentando o limite de profundidade a cada iteração.

from DfsLimited import dfs_limited

def iterative_deepening_dfs(graph, start, goal, max_depth):
    # Aumenta o limite de profundidade em cada iteração
    for depth in range(max_depth):
        if dfs_limited(graph, start, goal, depth):  # Chama a DFS limitada
            return True
    return False

# Exemplo de uso:
# print(iterative_deepening_dfs(graph, 'A', 'E', 3))  # Saída: True
