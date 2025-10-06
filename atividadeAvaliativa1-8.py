print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

preco_custo = float(input("Informe o preço de custo: "))
preco_venda = float(input("Informe o preço de venda: "))

lucro = preco_venda - preco_custo
margem = (lucro / preco_custo) * 100

if margem > 30:
    print("Margem excelente!")
elif margem >= 10 and margem <= 30:
    print("Margem satisfatória")
else:
    print("Margem baixa: Avaliar preço de venda.")
