qtdeAlunos = int(input("Informe a quantidade de alunos na turma: "))
soma_das_notas = 0

for i in range(qtdeAlunos):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    soma_das_notas=soma_das_notas + nota


media = soma_das_notas / qtdeAlunos
print(f"A a media da turma é: {media} ")
