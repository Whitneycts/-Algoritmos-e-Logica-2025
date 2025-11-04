simbolo = input("Digite um caractere ou símbolo (ex: *, #, -): ")

repetir = "sim" 

print("\n--- Gerador de Linhas Ativado ---")

while repetir == "sim":
    print(simbolo * 20)
    resposta_usuario = input("Deseja ver outra linha? (Digite SIM para continuar): ")

    repetir = resposta_usuario.lower()

print("Gerador encerrado. Obrigado!")