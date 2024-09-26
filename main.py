import random

from AStarSearch import a_star
from BreadthFirstSearch import bfs
from DepthFirstSearch import dfs
from DfsLimited import dfs_limited
from IterativeDeepeningDfs import iterative_deepening_dfs
from GeneticAlgorithm import genetic_algorithm, fitness_fn
from GreedySearch import greedy_search
from Minimax import minimax

# Graph creation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic creation
heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

# Creation of node costs (between each other)
cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'D'): 3,
    ('B', 'E'): 1,
    ('C', 'F'): 4
}

# Calling the algorithm A*
start_node = 'A'
goal_node = 'E'

result = a_star(graph, start_node, goal_node, heuristic, cost)

if result:
    print(f"\n[A*] Caminho encontrado de {start_node} até {goal_node}")
else:
    print(f"\n[A*] Nenhum caminho encontrado de {start_node} até {goal_node}")

# Calling the algorithm Busca em Largura (BFS - Breadth First Search)
found = bfs(graph, start_node, goal_node)

if found:
    print(f"\n[Busca em Largura (BFS - Breadth First Search)] Caminho encontrado de {start_node} até {goal_node} com BFS.")
else:
    print(f"\n[Busca em Largura (BFS - Breadth First Search)] Nenhum caminho encontrado de {start_node} até {goal_node} com BFS.")

# Calling the algorithm Busca em Profundidade (DFS - Depth First Search)
found = dfs(graph, start_node, goal_node)

if found:
    print(f"\n[Busca em Profundidade (DFS - Depth First Search)] Caminho encontrado de {start_node} até {goal_node} com DFS.")
else:
    print(f"\n[Busca em Profundidade (DFS - Depth First Search)] Nenhum caminho encontrado de {start_node} até {goal_node} com DFS.")

# Calling the algorithm Busca em Profundidade Limitada
found = dfs_limited(graph, start_node, goal_node, 2)

if found:
    print(f"\n[Busca em Profundidade Limitada] Caminho encontrado de {start_node} até {goal_node} com DFS Limitado.")
else:
    print(f"\n[Busca em Profundidade Limitada] Nenhum caminho encontrado de {start_node} até {goal_node} com DFS Limitado.")

# Calling the algorithm Busca em Profundidade Iterativa
found = iterative_deepening_dfs(graph, start_node, goal_node, 3)

if found:
    print(f"\n[Busca em Profundidade Iterativa] Caminho encontrado de {start_node} até {goal_node}.")
else:
    print(f"\n[Busca em Profundidade Iterativa] Nenhum caminho encontrado de {start_node} até {goal_node}.")

# Algoritmo Genético
# Defining population list of individuals, each one being an list with 0s and 1s
population = [
    [random.randint(0, 1) for _ in range(5)] for _ in range(10)  # 10 individuals with 5 genes
]

# Defining number of generations and mutation tax rate
generations = 20
mutation_rate = 0.1

best_population = genetic_algorithm(population, fitness_fn, generations, mutation_rate)

# Showing best individual after processment
best_individual = best_population[0]
print(f"\n[Algoritmo Genético] Melhor indivíduo final: {best_individual} Fitness: {fitness_fn(best_individual)}")

# Busca Gulosa
# Creating graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Defining heuristic for each node (distance to target estimation) 
heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 0,  # Target
    'F': 5
}

# Defining start node and target node
start = 'A'
goal = 'E'

result = greedy_search(graph, start, goal, heuristic)

# Showing result
if result:
    print(f"\n[Busca Gulosa] Caminho encontrado de {start} até {goal}!")
else:
    print(f"\n[Busca Gulosa] Nenhum caminho encontrado de {start} até {goal}.")

# Minimax
# Example: Board 3x3 of tic tac toe (1 = maximazer, -1 = minimazer, 0 = null)
initial_state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Calling Minimax with depth of 4, starting with maximazer player
best_value = minimax(initial_state, depth=4, is_maximizing=True)

# Showing best movement
print(f"\n[Minimax] Valor do melhor movimento: {best_value}")