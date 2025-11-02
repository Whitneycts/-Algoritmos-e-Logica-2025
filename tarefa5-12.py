numero_total_de_pecas = int(input('Número total de peças a serem inspecionadas: '))

TOLERANCIA = 0.5
TAMANHO_IDEAL = 15.0

soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0

if numero_total_de_pecas <= 0:
    print('O número de peças deve ser um inteiro positivo.')
else:
    i = 1
    while i <= numero_total_de_pecas:
        tamanho = float(input(f'Tamanho medido da peça {i} (cm): '))
        soma_dos_tamanhos += tamanho
        desvio = abs(tamanho - TAMANHO_IDEAL)
        if desvio > TOLERANCIA:
            pecas_fora_tolerancia += 1
        i += 1

    media_tamanho = soma_dos_tamanhos / numero_total_de_pecas

    if pecas_fora_tolerancia == 0:
        print('\nLote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).')
    elif pecas_fora_tolerancia <= 2:
        print('\nLote Aceitável: Pequena correção necessária.')
    else:
        print('\nLote Reprovado: Alta taxa de defeito.')

    print(f'\nMédia de Tamanho das Peças: {media_tamanho:.2f} cm')
    print(f'Quantidade de Peças Fora da Tolerância: {pecas_fora_tolerancia}')

# while: laço que executa um bloco enquanto uma condição for verdadeira.
# Exemplo: 'while condicao:' repete até que condicao seja False.