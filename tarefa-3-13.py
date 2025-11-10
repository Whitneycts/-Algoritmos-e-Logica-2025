contador_pares = 0
contador_impares = 0
numero_digitado = 1

print("--- Contador de Números Pares e Ímpares ---")
print("Digite números inteiros. Digite 0 para encerrar.")

while numero_digitado != 0:
    numero_digitado = int(input("\nDigite um número inteiro (0 para sair): "))
    
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            contador_pares += 1
            print(f"Número {numero_digitado} é par - contabilizado!")
        else:
            contador_impares += 1
            print(f"Número {numero_digitado} é ímpar - contabilizado!")

# Exibindo os resultados finais
print("\n=== Resultados Finais ===")
print(f"O total de números pares digitados é: {contador_pares}")
print(f"O total de números ímpares digitados é: {contador_impares}")
