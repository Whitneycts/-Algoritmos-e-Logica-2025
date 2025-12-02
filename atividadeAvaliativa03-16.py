nomes = []
rendas = []
status_aprovacao = []

print("--- Avaliação de Renda e Classificação de Status ---")

while True:
    nome = input("Digite o nome do candidato (ou 'fim' para sair): ")
    
    if nome.lower() == "fim":
        break
    
    renda = float(input(f"Digite a renda de {nome}: R$ "))
    
    nomes.append(nome)
    rendas.append(renda)
    
    if renda > 2500.00:
        status_aprovacao.append("Aprovado")
    else:
        status_aprovacao.append("Reprovado")

print("\n--- Análise dos Candidatos ---\n")

soma_rendas_aprovados = 0.0
contador_aprovados = 0

for i in range(len(nomes)):
    print(f"Nome: {nomes[i]} | Renda: R$ {rendas[i]:.2f} | Status: {status_aprovacao[i]}")
    
    if status_aprovacao[i] == "Aprovado":
        soma_rendas_aprovados += rendas[i]
        contador_aprovados += 1

if contador_aprovados > 0:
    media_rendas_aprovados = soma_rendas_aprovados / contador_aprovados
else:
    media_rendas_aprovados = 0.0

print(f"\nVetor de Nomes: {nomes}")
print(f"Vetor de Status: {status_aprovacao}")
print(f"Média das Rendas Aprovadas: R$ {media_rendas_aprovados:.2f}")
