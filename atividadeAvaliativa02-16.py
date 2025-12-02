registro_temperaturas = []
dias_criticos = 0

print("--- Análise de Temperaturas Críticas ---")

while True:
    temperatura = float(input("Digite a temperatura em Celsius (0 para sair): "))
    
    if temperatura == 0:
        break
    
    registro_temperaturas.append(temperatura)

print("\n--- Análise das Temperaturas ---\n")

for temp in registro_temperaturas:
    if temp > 30:
        print(f"Alerta Quente! Temperatura: {temp}°C")
        dias_criticos += 1
    elif temp < 10:
        print(f"Alerta Frio! Temperatura: {temp}°C")
        dias_criticos += 1
    else:
        print(f"Temperatura Agradável: {temp}°C")

print(f"\nVetor: {registro_temperaturas}")
print(f"Total de Dias Críticos: {dias_criticos}")
