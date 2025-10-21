custo_fixo = 500.00
custo_materia_prima = float(input("Digite o custo da matéria-prima por item (R$): "))


custo_variavel_total = 0

for i in range(1, 101):
    desperdicio = custo_materia_prima * 0.05
    custo_variavel_total += custo_materia_prima + desperdicio

custo_total = custo_fixo + custo_variavel_total

if custo_total < 3000:
    margem = 0.35
elif custo_total <= 5000:
    margem = 0.20
else:
    margem = 0.15

preco_minimo = (custo_total / 100) * (1 + margem)

print(f"Custo total de produção: R$ {custo_total:.2f}")
print(f"Margem de lucro aplicada: {margem*100:.0f}%")
print(f"Preço mínimo de venda por item: R$ {preco_minimo:.2f}")