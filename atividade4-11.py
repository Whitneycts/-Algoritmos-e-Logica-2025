num_meses = int(input("Digite o número total de meses a serem analisados: "))

consumo_total_kwh = 0.0
valor_total_pago = 0.0

for mes in range(1, num_meses + 1):
    consumo_kwh = float(input(f"Digite o consumo em kWh do mês {mes}: "))

    if consumo_kwh <= 100:
        tarifa = 0.55
    elif consumo_kwh <= 200:
        tarifa = 0.70
    else:
        tarifa = 0.95

    custo_mensal = consumo_kwh * tarifa

    consumo_total_kwh += consumo_kwh
    valor_total_pago += custo_mensal

    print(f"Mês {mes}: Consumo = {consumo_kwh:.2f} kWh | Tarifa = R${tarifa:.2f} | Custo = R${custo_mensal:.2f}")

media_mensal = consumo_total_kwh / num_meses

print("\n=== RELATÓRIO FINAL ===")
print(f"Consumo Total: {consumo_total_kwh:.2f} kWh")
print(f"Valor Total Pago: R${valor_total_pago:.2f}")
print(f"Média Mensal de Consumo: {media_mensal:.2f} kWh")

if media_mensal > 180:
    print("Alerta! O consumo médio está elevado. Sugerir medidas de economia.")
else:
    print("Consumo médio dentro dos limites normais.")