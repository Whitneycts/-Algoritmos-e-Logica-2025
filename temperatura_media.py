
dias = int(input('Quantidade de dias a analisar: '))
if dias <= 0:
    print('O número de dias deve ser um inteiro positivo.')
else:
    soma_das_temperaturas = 0.0
    for i in range(1, dias + 1):
        temp = float(input(f'Temperatura do dia {i} (°C): '))
        soma_das_temperaturas += temp

    media = soma_das_temperaturas / dias

    if media > 28.0:
        print(f'Média de temperatura: {media:.2f}°C - Clima Quente.')
    elif 18.0 <= media <= 28.0:
        print(f'Média de temperatura: {media:.2f}°C - Clima Agradável.')
    else:
        print(f'Média de temperatura: {media:.2f}°C - Clima Frio.')
