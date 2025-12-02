numero_alunos = int(input("Digite o número de alunos a serem avaliados (máximo 5): "))

if numero_alunos > 5:
    numero_alunos = 5

dados_brutos = []

for i in range(numero_alunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    nota_pratica = int(input(f"Digite a nota do trabalho prático de {nome}: "))
    nota_teorica = int(input(f"Digite a nota da prova teórica de {nome}: "))
    
    dados_brutos.append(nome)
    dados_brutos.append(nota_pratica)
    dados_brutos.append(nota_teorica)

soma_medias = 0.0
alunos_acima_media = 0

print("\n--- Análise de Desempenho dos Alunos ---\n")

for i in range(0, len(dados_brutos), 3):
    nome = dados_brutos[i]
    nota_pratica = float(dados_brutos[i + 1])
    nota_teorica = float(dados_brutos[i + 2])
    
    media = (nota_pratica * 0.6) + (nota_teorica * 0.4)
    soma_medias += media
    
    if media > 7.0:
        alunos_acima_media += 1
        print(f"{nome} - Situação: Excelente (Média: {media:.2f})")
    elif media >= 5.0:
        print(f"{nome} - Situação: Necessita Revisão (Média: {media:.2f})")
    else:
        print(f"{nome} - Situação: Reprovado (Média: {media:.2f})")

media_geral_turma = soma_medias / numero_alunos

print(f"\n--- Resumo Geral ---")
print(f"Média Geral da Turma: {media_geral_turma:.2f}")
print(f"Total de Alunos Acima da Média: {alunos_acima_media}")
