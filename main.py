# Importações dos arquivos com os algoritmos
from AStarSearch import a_star
from BreadthFirstSearch import bfs
from DepthFirstSearch import dfs
from DfsLimited import dfs_limited
from GeneticAlgorithm import genetic_algorithm
from GreedySearch import greedy_search
from IterativeDeepeningDfs import iterative_deepening_dfs
from Minimax import minimax

def main():
    # Exemplo de uso da Busca A*
    print("==== A* Search ====")
    start = 'A'
    goal = 'G'
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 1), ('E', 6)],
        'C': [('F', 5)],
        'D': [('G', 1)],
        'E': [],
        'F': [('G', 2)],
        'G': []
    }
    heuristic = {
        'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 5, 'F': 1, 'G': 0
    }
    path = a_star(graph, heuristic, start, goal)
    print(f"Path found by A*: {path}\n")

    # Exemplo de uso da Busca em Largura (BFS)
    print("==== BFS ====")
    bfs_result = bfs(graph, start, goal)
    print(f"Path found by BFS: {bfs_result}\n")

    # Exemplo de uso da Busca em Profundidade (DFS)
    print("==== DFS ====")
    dfs_result = dfs(graph, start, goal)
    print(f"Path found by DFS: {dfs_result}\n")

    # Exemplo de uso da Busca em Profundidade Limitada
    print("==== DFS Limited ====")
    depth_limit = 3
    dfs_limited_result = dfs_limited(graph, start, goal, depth_limit)
    print(f"Path found by DFS Limited (depth {depth_limit}): {dfs_limited_result}\n")

    # Exemplo de uso da Busca Gulosa
    print("==== Greedy Search ====")
    greedy_result = greedy_search(graph, heuristic, start, goal)
    print(f"Path found by Greedy Search: {greedy_result}\n")

    # Exemplo de uso da Busca em Profundidade Iterativa
    print("==== Iterative Deepening DFS ====")
    iterative_result = iterative_deepening_dfs(graph, start, goal)
    print(f"Path found by Iterative Deepening DFS: {iterative_result}\n")

    # Exemplo de uso do Algoritmo Genético
    print("==== Genetic Algorithm ====")
    # População inicial e fitness simples (exemplo genérico)
    initial_population = [[0, 1, 1, 0, 1], [1, 0, 0, 1, 1], [1, 1, 0, 0, 1]]
    best_individual = genetic_algorithm(initial_population, lambda x: sum(x), generations=10, mutation_rate=0.1)
    print(f"Best individual found by Genetic Algorithm: {best_individual}\n")

    # Exemplo de uso do Minimax
    print("==== Minimax ====")
    # Exemplo de tabuleiro 3x3 de jogo da velha
    state = [
        [0, 1, -1],
        [-1, 1, 0],
        [0, 0, 0]
    ]
    best_value = minimax(state, depth=4, is_maximizing=True)
    print(f"Best value found by Minimax: {best_value}\n")

if __name__ == "__main__":
    main()
