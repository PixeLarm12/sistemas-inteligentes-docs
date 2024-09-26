# MiniMax
# Usado em jogos de dois jogadores, o MiniMax avalia o valor de cada estado para o jogador atual e o oponente, assumindo que ambos jogam otimamente.

# Função que verifica se o estado é terminal (exemplo para jogo da velha)
def is_terminal(state):
    # Exemplo simples: se todos os espaços estão preenchidos, o jogo termina
    return all(x != 0 for row in state for x in row)

# Função de avaliação que calcula o valor do estado (heurística)
# Exemplo: Avalia o número de 1s menos o número de -1s no tabuleiro
def evaluate(state):
    score = 0
    for row in state:
        score += sum(row)
    return score

# Função que gera os possíveis movimentos (filhos) a partir de um estado
def get_children(state, is_maximizing):
    children = []
    symbol = 1 if is_maximizing else -1  # 1 para o jogador maximizador, -1 para o minimizador
    
    # Para cada célula vazia (0), cria um novo estado possível
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:  # Verifica se a célula está vazia
                new_state = [row[:] for row in state]  # Copia o estado atual
                new_state[i][j] = symbol  # Preenche com o símbolo do jogador atual
                children.append(new_state)
    return children

# Função principal do Minimax
def minimax(state, depth, is_maximizing):
    if depth == 0 or is_terminal(state):  # Se atingir profundidade máxima ou estado final
        return evaluate(state)  # Retorna a avaliação do estado
    
    if is_maximizing:  # Jogador maximizador
        max_eval = float('-inf')  # Inicializa o valor máximo
        for child in get_children(state, is_maximizing):  # Explora todos os movimentos
            eval = minimax(child, depth - 1, False)  # Avalia do ponto de vista do minimizador
            max_eval = max(max_eval, eval)  # Atualiza o valor máximo
        return max_eval
    else:  # Jogador minimizador
        min_eval = float('inf')  # Inicializa o valor mínimo
        for child in get_children(state, is_maximizing):  # Explora todos os movimentos
            eval = minimax(child, depth - 1, True)  # Avalia do ponto de vista do maximizador
            min_eval = min(min_eval, eval)  # Atualiza o valor mínimo
        return min_eval

# Exemplo de uso: Tabuleiro 3x3 de jogo da velha (1 = maximizador, -1 = minimizador, 0 = vazio)
initial_state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Chamando o algoritmo Minimax com profundidade 4, começando pelo jogador maximizador
best_value = minimax(initial_state, depth=4, is_maximizing=True)
print("Valor do melhor movimento:", best_value)