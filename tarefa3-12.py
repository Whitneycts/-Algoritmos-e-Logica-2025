numero_produtos = int(input('Número total de produtos: '))

valor_total_estoque = 0.0
produtos_alto_risco = 0


for i in range(1, numero_produtos + 1):
    preco_unitario = float(input(f'Preço unitário do produto {i}: R$ '))
    quantidade_estoque = int(input(f'Quantidade em estoque do produto {i}: '))
    valor_bruto = preco_unitario * quantidade_estoque
    if quantidade_estoque > 100:
        valor_total_estoque += valor_bruto * 1.05
    elif (preco_unitario > 50.0) and (quantidade_estoque <= 10):
        produtos_alto_risco += 1
        valor_total_estoque += valor_bruto
    else:
        valor_total_estoque += valor_bruto

print('\nValor Total Final do Estoque: R$ {:.2f}'.format(valor_total_estoque))
print('Número de Produtos Classificados como Alto Risco:', produtos_alto_risco)
