totalQuestoes = int(input("Informe o número total de questões no quiz: "))

pontuacao_bruta = 0
erros_consecutivos = 0

for i in range(1, totalQuestoes +1):
    pontuacao = float(input(f"Informe a pontuação da questão {i} (0.0 a 10.0): "))

    if pontuacao == 10.0:
        pontuacao_bruta += pontuacao
        erros_consecutivos = 0
        print("Contador de erros zerado.")

    elif pontuacao < 5.0:
        pontuacao_bruta += pontuacao
        erros_consecutivos = 1
        print("Erro contado.")

    else:
        pontuacao_bruta += pontuacao
        erros_consecutivos = 0
        print("Contador de erros zerado.")

print(f"Pontuação Bruta: {pontuacao_bruta:.2f}")
print(f"Erros consecutivos: {erros_consecutivos}")

if pontuacao_bruta > 40 and erros_consecutivos == 0:
    print("Resultado Excelente! Bônus de 10% aplicado.")
    pontuacao_ajustada = pontuacao_bruta * 1.10
elif pontuacao_bruta < 20 or erros_consecutivos > 2:
    print("Resultado Fraco. Penalidade de 15% aplicada.")
    pontuacao_ajustada = pontuacao_bruta * 0.85
else:
    print("Resultado Padrão. Sem bônus ou penalidade.")
    pontuacao_ajustada = pontuacao_bruta

print(f"Pontuação Final Ajustada: {pontuacao_ajustada:.2f}")
