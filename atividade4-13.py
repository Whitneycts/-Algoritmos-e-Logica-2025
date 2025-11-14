cidades = []
NUMERO_CIDADES = 5

print("--- Programa de Leitura de Cidades ---")
print(f"Digite o nome de {NUMERO_CIDADES} cidades:\n")

for i in range(NUMERO_CIDADES):
    cidade = input(f"Digite a cidade {i + 1}: ")
    cidades.append(cidade)

print("\n=== Cidades em Maiúsculas ===\n")
for i in range(len(cidades)):
    cidade_maiuscula = cidades[i].upper()
    print(f"Cidade {i + 1}: {cidade_maiuscula}")
