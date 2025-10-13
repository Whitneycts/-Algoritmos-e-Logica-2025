print("Cálculo de Imposto Fixo e Taxa de Serviço sobre vendas")

quantidade_dias = int(input("Quantidade de dias a analisar: "))

vendas_totais = 0.0
for dia in range(1, quantidade_dias + 1):
    valor = float(input(f"Vendas do dia {dia}: R$ "))
    vendas_totais += valor

media_diaria = vendas_totais / quantidade_dias

if media_diaria > 1500.0:
    imposto_fixo = 200.0
else:
    imposto_fixo = 50.0

if vendas_totais > 10000.0:
    taxa_percentual = 0.08
else:
    taxa_percentual = 0.05

valor_taxa = vendas_totais * taxa_percentual
valor_liquido = vendas_totais - valor_taxa - imposto_fixo

print("\nResumo:")
print(f"Valor total das vendas: R$ {vendas_totais:.2f}")
print(f"Imposto fixo aplicado: R$ {imposto_fixo:.2f}")
print(f"Percentual da taxa de serviço: {int(taxa_percentual * 100)}%")
print(f"Valor da taxa de serviço: R$ {valor_taxa:.2f}")
print(f"Valor líquido final: R$ {valor_liquido:.2f}")
