numero_lotes = int(input('Número de Lotes de Produção a serem simulados: '))

if numero_lotes <= 0:
    print('O número de lotes deve ser um inteiro positivo.')
else:
    CUSTO_FIXO_POR_LOTE = 100.00
    lista_custos_por_lote = []


    for i in range(numero_lotes):
        unidades = int(input(f'Unidades produzidas no lote {i+1}: '))
        if unidades > 50:
            C_var_unidade = 1.50
        elif 20 <= unidades <= 50:
            C_var_unidade = 2.00
        else:
            C_var_unidade = 3.00
        Custo_Lote = CUSTO_FIXO_POR_LOTE + (unidades * C_var_unidade)
        lista_custos_por_lote.append(Custo_Lote)


    Preco_Base_Venda = 5.00
    lucro_total_acumulado = 0.0
    lotes_com_lucro_alto = 0


    for idx, Custo_Lote in enumerate(lista_custos_por_lote):
        Receita = 50 * Preco_Base_Venda
        Lucro = Receita - Custo_Lote
        lucro_total_acumulado += Lucro
        if Lucro > 100.0:
            lotes_com_lucro_alto += 1
            print(f'Lote {idx+1} Aprovado: Lucro Alto.')
        elif Lucro > 0.0:
            print(f'Lote {idx+1} Aceitável: Lucro Mínimo.')
        else:
            print(f'Lote {idx+1} Reprovado: Prejuízo.')
            

    print('\n--- Resultado da Simulação ---')
    print(f'Lucro Total Acumulado: R$ {lucro_total_acumulado:.2f}')
    print(f'Quantidade de Lotes com Lucro Alto: {lotes_com_lucro_alto}')
