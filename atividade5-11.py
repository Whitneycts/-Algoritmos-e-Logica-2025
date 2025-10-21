print("Cálculo de imposto sobre o volume de vendas de notas fiscais")
quantidade = int(input("Quantidade de notas fiscais a inserir: "))

soma_das_notas = 0.0
for i in range(1, quantidade + 1):
    valor = float(input(f"Valor da nota {i}: R$ "))
    soma_das_notas += valor

if soma_das_notas <= 100.0:
    aliquota = 0.05
elif 1000.0 <= soma_das_notas <= 4999.99:
    aliquota = 0.09
elif 5000.0 <= soma_das_notas <= 14999.99:
    aliquota = 0.12
elif soma_das_notas > 15000.0:
    aliquota = 0.16
else:
    aliquota = 0.05

valor_imposto = soma_das_notas * aliquota

print("\nResumo:")
print(f"Valor total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {int(aliquota * 100)}%")
print(f"Valor total do imposto a pagar: R$ {valor_imposto:.2f}")
