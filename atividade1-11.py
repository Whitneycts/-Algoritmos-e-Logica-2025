numeroLimite =  int(input("Digite um número inteiro positivo: "))

soma_dos_quadrados = 0

for i in range(1, numeroLimite +1):
    quadrado =  i **2

    if i % 3 == 0:
        print(f"{i} é múltiplo de 3.")
    elif i % 2 == 0:
        soma_dos_quadrados += quadrado
        print(f"{i} é par. Quadrado acumulado.")
    else:
        print(f"{i} é ímpar. Ignorado.")

print(f"O valor final da soma dos quadrados é: {soma_dos_quadrados}")