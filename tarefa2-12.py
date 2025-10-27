numero_de_dias = int(input('Número de dias a analisar: '))
if numero_de_dias <= 0:
    print('O número de dias deve ser um inteiro positivo.')
else:
    producao_total = 0
    dias_acima_da_meta = 0
    meta_diaria = 50

    for dia in range(1, numero_de_dias + 1):
        producao_dia = int(input(f'Produção do dia {dia}: '))
        producao_total += producao_dia
        if producao_dia >= meta_diaria:
            dias_acima_da_meta += 1

    media_diaria = producao_total / numero_de_dias

    if (media_diaria > 60) and (dias_acima_da_meta >= 4):
        print('\nBÔNUS MÁXIMO! (15% sobre a produção total).')
        bonus = producao_total * 0.15
    elif (media_diaria > 50) or (dias_acima_da_meta >= 3):
        print('\nBÔNUS PARCIAL! (5% sobre a produção total).')
        bonus = producao_total * 0.05
    else:
        print('\nSem Bônus. Metas de produtividade não foram atingidas.')
        bonus = 0.0

    print('\n--- Resultado da Análise ---')
    print(f'Média Diária de Produção: {media_diaria:.2f} unidades')
    print(f'Dias acima da meta ({meta_diaria}): {dias_acima_da_meta} de {numero_de_dias}')
    print(f'Produção Total: {producao_total} unidades')
    print(f'Valor do Bônus: R$ {bonus:.2f}')
