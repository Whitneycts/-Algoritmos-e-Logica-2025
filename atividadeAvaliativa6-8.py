print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

R_investimento = float(input("Digite o retorno do investimento (%): ")) / 100
R_livre = float(input("Digite a taxa livre de risco (%): ")) / 100
Sigma = float(input("Digite o desvio-padrão da volatilidade (%): ")) / 100

if Sigma == 0:
    Sharp = 0
else:
    Sharp = (R_investimento - R_livre) / Sigma

Spread = R_investimento - R_livre

if Sharp > 1.5 and Spread > 0.05:
    classificacao = "Investimento Excelente: Alta performance ajustada ao risco."
elif (0.5 <= Sharp <= 1.5) or (Spread > 0.02):
    classificacao = "Investimento Bom: Risco e retorno moderados."
elif Sharp < 0.5 and R_investimento > 0:
    classificacao = "Investimento Aceitável: Retorno positivo, mas risco alto para o ganho."
else:
    classificacao = "Investimento Ruim: Não recomendado."

print(f"\nSharpe Ratio: {Sharp:.2f}")
print(f"Classificação Final: {classificacao}")
