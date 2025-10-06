print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

C_inicial = float(input("Digite o custo inicial do material: "))
Q = int(input("Digite a quantidade de itens produzidos: "))
Dias = int(input("Digite o número de dias de atraso: "))
Defeito = float(input("Digite o percentual de defeitos (em decimal, ex: 0.05): "))

# Correção de custo base
if Q > 1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp

# Penalidades
if Defeito > 0.10 or Dias > 5:
    print("Penalidade Alta: 20% de redução no lucro.")
    C_final = C_corrigido * 1.25
elif 0.05 <= Defeito <= 0.10 or Dias > 0:
    print("Penalidade Média: 10% de redução no lucro.")
    C_final = C_corrigido * 1.10
else:
    print("Sem penalidade. Custo final apenas com correção.")
    C_final = C_corrigido

print(f"Custo Base Corrigido: {C_corrigido:.2f}")
print(f"Custo Final: {C_final:.2f}")
