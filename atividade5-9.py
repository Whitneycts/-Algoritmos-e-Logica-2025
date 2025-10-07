soma = 0

for numero in range(5):
    numero =  int(input(f"Digite {numero+1}º: "))
    soma = soma + numero

print(f"O valor total da soma de todos os números é: {soma}")