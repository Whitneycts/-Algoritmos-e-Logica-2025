quantidade_dias = int(input('Quantidade total de dias a serem analisados: '))

if quantidade_dias <= 0:
    print('O número de dias deve ser um inteiro positivo.')
else:
    soma_das_temperaturas = 0.0
    for i in range(1, quantidade_dias + 1):
        temperatura = float(input(f'Temperatura do dia {i} (°C): '))
        soma_das_temperaturas += temperatura

    media = soma_das_temperaturas / quantidade_dias


    if media > 28.0:
        print('Média de temperatura: Clima Quente.')
    elif 18.0 <= media <= 28.0:
        print('Média de temperatura: Clima Agradável.')
    else:
        print('Média de temperatura: Clima Frio.')

    print(f'Média final da temperatura do período: {media:.2f}°C')
