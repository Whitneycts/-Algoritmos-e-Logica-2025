gastos_semanais = []
continuar = "sim"

while continuar == "sim":
    valor_gasto = float(input("Digite o valor do gasto do dia (R$): "))
    gastos_semanais.append(valor_gasto)
    continuar = input("Deseja continuar? (sim/não): ")

soma_total = 0.0

for i in range(len(gastos_semanais)):
    soma_total = soma_total + gastos_semanais[i]

print(f"\nVetor: {gastos_semanais}")
print(f"Gasto Total da Semana: R$ {soma_total:.2f}")
