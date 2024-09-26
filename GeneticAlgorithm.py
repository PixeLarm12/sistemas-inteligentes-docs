# Algoritmo Genético
# Os algoritmos genéticos simulam o processo de evolução, usando seleção, cruzamento e mutação para evoluir soluções ao longo de várias gerações.

import random

# Função de aptidão que avalia a "qualidade" de um indivíduo
def fitness_fn(individual):
    return sum(individual)  # Exemplo simples: soma dos valores do indivíduo

# Função de cruzamento que combina dois pais para criar uma nova criança
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  # Ponto de corte aleatório
    child = parent1[:crossover_point] + parent2[crossover_point:]  # Combina partes dos pais
    return child

# Função de mutação que altera aleatoriamente um gene do indivíduo
def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:  # Aplica mutação com base na taxa de mutação
            individual[i] = random.randint(0, 1)  # Troca o gene por um valor aleatório (0 ou 1)
    return individual

# Algoritmo genético principal
def genetic_algorithm(population, fitness_fn, generations=100, mutation_rate=0.1):
    for generation in range(generations):
        # Ordena a população pela aptidão, do mais apto para o menos apto
        population = sorted(population, key=fitness_fn, reverse=True)
        next_generation = population[:2]  # Mantém os 2 melhores indivíduos

        # Cria novos indivíduos (crianças) até preencher a nova geração
        while len(next_generation) < len(population):
            # Seleciona aleatoriamente dois pais entre os mais aptos
            parent1, parent2 = random.sample(population[:5], 2)
            # Realiza cruzamento e mutação
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_generation.append(child)

        # Atualiza a população com a nova geração
        population = next_generation
        # Imprime a melhor solução a cada geração
        print(f"Geração {generation + 1}: Melhor Indivíduo: {population[0]} Fitness: {fitness_fn(population[0])}")

    # Retorna o melhor indivíduo após todas as gerações
    return population
