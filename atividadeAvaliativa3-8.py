print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

peso = float(input("Informe o peso da encomenda: "))
distancia = float(input("Informe a distância da entrega: "))

custo_base = (peso * 1.5) + (distancia * 0.25)
custo_final = custo_base

if custo_base > 200:
    custo_final = custo_base * 0.9  # desconto de 10%
    print("Você tem um desconto de 10%")
elif 50 <= custo_base <= 200:
    print("Você não tem nenhum desconto")
else:
    custo_final = custo_base + 5
    print("Taxa de manuseio de R$ 5,00")

print(f"O custo base original é de: {custo_base:.2f}")
print(f"O custo final foi de: {custo_final:.2f}")
