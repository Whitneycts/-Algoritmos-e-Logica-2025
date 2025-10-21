salario_base = 800.00
limite_falhas = 1
soma_produtividade = 0.0
contagem_falhas = 0

for dia in range(1, 6):
    P_dia = float(input(f"Digite a produtividade do dia {dia} (0 a 100): "))
    soma_produtividade += P_dia
    if P_dia < 60:
        contagem_falhas += 1
        print("Falha registrada neste dia.")
    else:
        print("Dia produtivo.")

produtividade_media = soma_produtividade / 5

print("\n=== RELATÓRIO SEMANAL ===")
print(f"Produtividade Média: {produtividade_media:.2f}")
print(f"Total de Falhas: {contagem_falhas}")

if produtividade_media > 80 and contagem_falhas <= limite_falhas:
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    pagamento_final = salario_base * 1.10
elif 60 <= produtividade_media <= 80 or contagem_falhas > limite_falhas:
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    pagamento_final = salario_base * 0.95
else:
    print("Penalidade Severa: Pagamento reduzido em 25%.")
    pagamento_final = salario_base * 0.75

print(f"Pagamento Final: R${pagamento_final:.2f}")