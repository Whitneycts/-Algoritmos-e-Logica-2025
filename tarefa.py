print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

pureza_lote = float(input("Informe a pureza do lote em (%): "))
massa_total = float(input("Informe a massa total (kg): "))
taxa_contaminacao = float(input("Informe a taxa de contaminação (%): "))

FD = (pureza_lote * 100) - (taxa_contaminacao * 50)

if massa_total > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if FD > 90 and pureza_lote > 0.98:
    classificacao = "Classificação: PREMIUM (Venda Imediata)"
    P_final_kg = P_base * 1.50

elif 70 <= FD <= 90 and taxa_contaminacao < 0.05:
    classificacao = "Classificação: PADRÃO (Venda Normal)"
    P_final_kg = P_base * 1.10

elif FD < 70 or pureza_lote < 0.90:
    classificacao = "Classificação: REPROVADO (Descarte ou Re-processamento)"
    P_final_kg = P_base * 0.25

else:
    classificacao = "Classificação: ACEITÁVEL (Margem Mínima)"
    P_final_kg = P_base * 0.90

Preco_Total_Final = P_final_kg * massa_total

print(f"\n{classificacao}")
print(f"Preço Base por kg: R$ {P_base:.2f}")
print(f"Preço Final por kg: R$ {P_final_kg:.2f}")
print(f"Preço Final Total do lote: R$ {Preco_Total_Final:.2f}")

aaa

