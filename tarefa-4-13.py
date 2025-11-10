soma_pares = 0
soma_impares = 0
numero_digitado = 1

print("--- Soma Separada de Números Pares e Ímpares ---")
print("Digite números inteiros. Digite 0 para encerrar.")

while numero_digitado != 0:
    numero_digitado = int(input("\nDigite um número inteiro (0 para sair): "))
    
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            soma_pares += numero_digitado
            print(f"Número par {numero_digitado} adicionado à soma de pares!")
        else:
            soma_impares += numero_digitado
            print(f"Número ímpar {numero_digitado} adicionado à soma de ímpares!")

print("\n=== Resultados Finais ===")
print(f"A soma total dos números pares é: {soma_pares}")
print(f"A soma total dos números ímpares é: {soma_impares}")
