simbolo = input("Digite um símbolo (ex: #, *): ")

quantidade =  int(input("Digite a quantidade de vezes que o símbolo deve se repetir: "))

print("\n--- Padrão Gerado ---")
for i in range(quantidade):
    print(simbolo)

print("-----------------------")