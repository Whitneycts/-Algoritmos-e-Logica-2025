print("Controle de Gastos com Combustível")

quantidade_dias = int(input("Quantidade de dias de viagem: "))

total_km_percorridos = 0.0
for dia in range(1, quantidade_dias + 1):
    km = float(input(f"Quilômetros percorridos no dia {dia}: "))
    total_km_percorridos += km

# Consumo e custos
consumo_km_por_litro = 12.0
total_litros = total_km_percorridos / consumo_km_por_litro
preco_litro = 4.80
custo_total = total_litros * preco_litro

# Avaliação do custo
if custo_total > 500.0:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")

print(f"Total de KM percorridos: {total_km_percorridos:.2f} km")
print(f"Custo total com combustível: R$ {custo_total:.2f}")
