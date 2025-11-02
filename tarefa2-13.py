numero_total_de_pecas = int(input('Número total de peças no lote: '))

CUSTO_FIXO_INSPECAO = 150.00
CUSTO_RETRABALHO_CRITICO = 25.00
erros_criticos = 0
erros_leves = 0
custo_variavel_rejeicao = 0.0


if numero_total_de_pecas <= 0:
    print('O número de peças deve ser um inteiro positivo.')
else:
    for i in range(1, numero_total_de_pecas + 1):
        nivel_defeito = int(input(f'Nível de defeito da peça {i} (0-10): '))
        if nivel_defeito > 8:
            erros_criticos += 1
            custo_variavel_rejeicao += CUSTO_RETRABALHO_CRITICO
        elif 3 <= nivel_defeito <= 8:
            erros_leves += 1
        else:
            print('Peça Aprovada.')


    Taxa_Rejeicao = (erros_criticos / numero_total_de_pecas) * 100
    Custo_Final = CUSTO_FIXO_INSPECAO + custo_variavel_rejeicao


    if (Taxa_Rejeicao > 10) and (erros_leves > 5):
        classificacao = 'LOTE REPROVADO! Alta taxa de defeito e muitos erros leves.'
    elif (erros_criticos > 2) or (Taxa_Rejeicao > 20):
        classificacao = 'LOTE CRÍTICO! Necessário reavaliação total.'
    else:
        classificacao = 'LOTE APROVADO! Custos sob controle.'


    print('\n--- Resultado da Inspeção ---')
    print(f'Taxa de Rejeição: {Taxa_Rejeicao:.2f}%')
    print(f'Custo Final Total (inspeção + retrabalho): R$ {Custo_Final:.2f}')
    print('Classificação do Lote:', classificacao)
