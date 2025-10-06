print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

P = float(input("Informe o valor inicial do investimento: "))
T = int(input("Informe o prazo do investimento em meses: "))

if T < 6:
    J = 0.005
elif 6 <= T <= 12:
    J = 0.008
else:
    J = 0.012

Rendimento_Total = P * J * T

print(f"Taxa de juros aplicada: {J * 100:.2f}% ao mês")
print(f"Rendimento total obtido: R$ {Rendimento_Total:.2f}")
