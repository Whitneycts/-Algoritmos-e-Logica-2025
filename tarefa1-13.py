numero_vendedores = int(input('Número total de vendedores a serem avaliados: '))


if numero_vendedores <= 0:
    print('O número de vendedores deve ser um inteiro positivo.')
else:
    pontuacao_total_equipe = 0.0
    vendedores_acima_meta = 0
    botoes_alerta_ativados = 0


    for i in range(1, numero_vendedores + 1):
        pontuacao = int(input(f'Pontuação final do vendedor {i} (0-100): '))
        pontuacao_total_equipe += pontuacao
        if pontuacao >= 90:
            vendedores_acima_meta += 1
        elif pontuacao < 50:
            botoes_alerta_ativados += 1

    media_equipe = pontuacao_total_equipe / numero_vendedores
    bonus_base_total = numero_vendedores * 500.00


    if (media_equipe > 80) and (botoes_alerta_ativados == 0):
        FMB = 1.20
    elif (vendedores_acima_meta > (numero_vendedores / 2)) or (70 <= media_equipe <= 80):
        FMB = 1.05
    elif botoes_alerta_ativados > 1:
        FMB = 0.80
    else:
        FMB = 1.00



    Valor_Final_Total = bonus_base_total * FMB


    print('\n--- Resultado da Avaliação ---')
    print(f'Média de Pontuação da Equipe: {media_equipe:.2f}')
    print(f'Número de Alertas (botões ativados): {botoes_alerta_ativados}')
    print(f'Valor Final Total a Pagar: R$ {Valor_Final_Total:.2f}')
