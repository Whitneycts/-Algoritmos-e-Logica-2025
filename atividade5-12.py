import random

# Ele utiliza a função 'random.randint(1, 6)' do módulo 'random' para sortear
# um número secreto aleatório entre 1 e 6 (simulando um lançamento de dado).
# Em seguida, entra em um loop 'while' que continua executando
# enquanto o usuário não acertar o número ('while not acertou').
# Dentro do loop, ele solicita o palpite do usuário, verifica se o palpite
# está no intervalo correto (1-6) e, se não estiver, pede um novo palpite.
# A cada palpite válido, incrementa o contador de 'tentativas'.
# Se o 'palpite_usuario' for igual ao 'numero_secreto', a variável 'acertou'
# muda para True, encerrando o loop.
# Por fim, exibe o número secreto e quantas tentativas foram necessárias.

numero_secreto = random.randint(1, 6)
tentativas = 0
acertou = False
palpite_usuario = 0

print("--- Jogo de Adivinhar o Dado ---")
print("Tente adivinhar o número que o dado sorteou (entre 1 e 6).")

while not acertou:
    palpite_usuario = int(input("Seu palpite: "))
    if palpite_usuario < 1 or palpite_usuario > 6:
        print("Palpite fora do intervalo. Tente um número entre 1 e 6.")
        continue

    tentativas += 1

    if palpite_usuario == numero_secreto:
        acertou = True
        print("\n*** Parabéns! Você acertou! ***")
    else:
        print("Errado. Tente novamente.")

print(f"O número sorteado era: {numero_secreto}")
print(f"Você precisou de {tentativas} tentativa(s) para acertar.")