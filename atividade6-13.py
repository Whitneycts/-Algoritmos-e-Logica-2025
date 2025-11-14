lista_notas = []
NUMERO_NOTAS = 5

for i in range(NUMERO_NOTAS):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    lista_notas.append(nota)

for i in range(len(lista_notas)):
    print(f"A nota na posição [{i}] é: {lista_notas[i]}")

