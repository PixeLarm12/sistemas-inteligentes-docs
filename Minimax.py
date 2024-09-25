# MiniMax
# Usado em jogos de dois jogadores, o MiniMax avalia o valor de cada estado para o jogador atual e o oponente, assumindo que ambos jogam otimamente.

def minimax(state, depth, is_maximizing):
    if depth == 0 or is_terminal(state):  # Se atingir a profundidade ou um estado final
        return evaluate(state)  # Retorna a avaliação do estado
    
    if is_maximizing:  # Se é o turno do jogador maximizador
        max_eval = float('-inf')  # Inicializa o valor máximo
        for child in get_children(state):  # Explora todos os movimentos possíveis
            eval = minimax(child, depth - 1, False)  # Avalia a jogada do oponente
            max_eval = max(max_eval, eval)  # Seleciona a jogada que maximiza o ganho
        return max_eval
    else:  # Se é o turno do jogador minimizador
        min_eval = float('inf')  # Inicializa o valor mínimo
        for child in get_children(state):  # Explora todos os movimentos possíveis
            eval = minimax(child, depth - 1, True)  # Avalia a jogada do oponente
            min_eval = min(min_eval, eval)  # Seleciona a jogada que minimiza a perda
        return min_eval

# Funções auxiliares não implementadas: is_terminal, evaluate, get_children.

