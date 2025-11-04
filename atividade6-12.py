numero_tabuada = int(input("Digite o número inteiro para ver a tabuada: "))

contador = 1

print(f"\n--- Tabuada do {numero_tabuada} ---")

while contador <= 10:
    resultado = numero_tabuada * contador
    print(f"{numero_tabuada} x {contador} = {resultado}")
    
    contador += 1 

print("Tabuada completa.")