V_inicial = float(input("Digite o valor inicial do investimento (R$): "))
num_meses = int(input("Digite o número de meses a serem simulados: "))

valor_acumulado = V_inicial
juros_totais = 0.0

for mes in range(1, num_meses + 1):
    taxa = float(input(f"Digite a taxa de crescimento do mês {mes} (em decimal, ex: 0.02 para 2%): "))

    if taxa > 0.015:
        juros = valor_acumulado * taxa
        print(f"→ Mês {mes}: Taxa alta! Juros aplicados normalmente.")
    elif 0.005 <= taxa <= 0.015:
        juros = valor_acumulado * taxa * 0.9
        print(f"→ Mês {mes}: Taxa moderada. Penalidade de 10% aplicada.")
    else:
        juros = 0.0
        print(f"→ Mês {mes}: Taxa muito baixa. Nenhum rendimento obtido.")

    valor_acumulado += juros
    juros_totais += juros

    print(f"   Juros do mês: R${juros:.2f} | Valor acumulado: R${valor_acumulado:.2f}\n")

print("=== RESULTADO FINAL ===")
print(f"Valor Inicial: R${V_inicial:.2f}")
print(f"Valor Final Acumulado: R${valor_acumulado:.2f}")
print(f"Juros Totais Ganhos: R${juros_totais:.2f}")

if juros_totais > (V_inicial * 0.10):
    print("Investimento de Alto Sucesso! (Retorno superior a 10%)")
else:
    print("Investimento Moderado. Retorno abaixo do esperado.")