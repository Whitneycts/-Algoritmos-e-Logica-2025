soma_pares = 0
numero_digitado = 1

print("--- Soma de Números Pares ---")
print("Digite números inteiros. Digite 0 para encerrar.")

while numero_digitado != 0:
    numero_digitado = int(input("\nDigite um número inteiro (0 para sair): "))
    
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            soma_pares += numero_digitado
            print(f"Número par {numero_digitado} adicionado à soma!")
        else:
            print(f"Número {numero_digitado} é ímpar - ignorado!")

print(f"\nA soma total dos números pares digitados é: {soma_pares}")
