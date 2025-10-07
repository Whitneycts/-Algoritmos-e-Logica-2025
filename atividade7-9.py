qtdeProdutos = int(input("Digite a quantidade de produtos diferentes que vai usar: "))
total_da_compra = 0.0

for i in range(qtdeProdutos):
   preco = float(input(f"Informe o preço do {i + 1}° produto: "))
   total_da_compra = total_da_compra + preco

print(f"O total a pagar é: R$ {total_da_compra:.2f}")
