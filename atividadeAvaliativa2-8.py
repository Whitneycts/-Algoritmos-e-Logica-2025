print("RA: 0220482523005")
print("Nome: Whitney Costa Silva")

valor_glicose = float(input("Informe o valor da sua glicose em jejum: "))

if valor_glicose < 100:
    print("Glicemia normal")
elif 100 <= valor_glicose <= 125:
    print("Pré-diabetes: Risco Moderado")
else:
    print("Diabetes nível alto.")
