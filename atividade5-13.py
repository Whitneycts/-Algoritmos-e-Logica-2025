# Definimos o tamanho fixo do nosso vetor
# Essa constante define quantas notas serão lidas e armazenadas
TAMANHO_VETOR = 5

# ============================================================
# 1. PRÉ-ALOCAÇÃO DO VETOR (Reserva de Memória)
# ============================================================
# [0.0] * TAMANHO_VETOR cria uma lista com 5 posições, todas inicializadas com 0.0
# Exemplo: [0.0, 0.0, 0.0, 0.0, 0.0]
# Isso simula a alocação de memória em linguagens como C/Java
vetor_notas = [0.0] * TAMANHO_VETOR

# soma_notas: acumulador que armazenará a soma de todas as notas
soma_notas = 0.0

# media: variável que armazenará o resultado final (soma / quantidade)
media = 0.0

print("--- Entrada de 5 Notas ---")
print("Você digitará 5 notas que serão armazenadas em um vetor.\n")

# ============================================================
# PRIMEIRO FOR: LEITURA E ARMAZENAMENTO DAS NOTAS
# ============================================================
# Este laço se repete 5 vezes (i = 0, 1, 2, 3, 4)
# Cada iteração lê uma nota e a armazena no vetor
for i in range(TAMANHO_VETOR):
    # Solicitamos a nota do usuário
    # i+1 é usado apenas para exibir 'Nota 1', 'Nota 2', etc. (amigável)
    # [i] mostra a posição real no vetor (0, 1, 2, 3, 4)
    nota = float(input(f"Digite a Nota {i + 1} (Posição [{i}]): "))
    
    # Atribuímos a nota lida diretamente ao índice i do vetor
    # Exemplo: vetor_notas[0] = 7.5 (na primeira iteração)
    # Isso é exatamente como funciona em C/Java: vetor[i] = valor
    vetor_notas[i] = nota

print("\n--- Processamento dos Dados ---")

# ============================================================
# SEGUNDO FOR: SOMA E ACUMULAÇÃO
# ============================================================
# Este laço percorre novamente o vetor, desta vez para somar todos os valores
# Usamos o índice 'i' para acessar cada elemento: vetor_notas[i]
for i in range(TAMANHO_VETOR):
    # Acessamos o elemento na posição i e adicionamos ao acumulador
    # Exemplo: soma_notas = 0.0 + 7.5 = 7.5 (primeira iteração)
    #          soma_notas = 7.5 + 8.0 = 15.5 (segunda iteração)
    soma_notas = soma_notas + vetor_notas[i]

# ============================================================
# CÁLCULO FINAL DA MÉDIA
# ============================================================
# Verificamos se TAMANHO_VETOR é maior que 0 para evitar divisão por zero
if TAMANHO_VETOR > 0:
    # Dividimos a soma total pelo número de notas
    # Exemplo: 38.5 / 5 = 7.7
    media = soma_notas / TAMANHO_VETOR

# ============================================================
# EXIBIÇÃO DOS RESULTADOS
# ============================================================
print(f"Vetor de Notas Registrado: {vetor_notas}")
print(f"Soma Total das Notas: {soma_notas:.2f}")
print(f"Média Final da Turma: {media:.2f}")
print("\n--- Programa Finalizado ---")
