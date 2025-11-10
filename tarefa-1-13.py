import random

numero_secreto = random.randint(1, 10)
acertou = False
tentativas = 0

print("--- Jogo de Adivinhar o número ---")
print("Tente adivinhar o número de 1 a 10")

while not acertou:
    palpite_usuario = int(input("Seu palpite: "))
    tentativas += 1
    
    if palpite_usuario == numero_secreto:
        acertou = True
        print("\nParabéns, você acertou!")
    elif palpite_usuario > numero_secreto:
        print("Seu palpite foi muito alto. Tente um número menor.")
    else:
        print("Seu palpite foi muito baixo. Tente um número maior.")

print(f"\nJogo finalizado! O número secreto era {numero_secreto}")
print(f"Você acertou em {tentativas} tentativas!")