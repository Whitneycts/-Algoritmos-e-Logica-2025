SENHA_CORRETA = "python123"
tentativas_erradas = 0
senha_digitada = ""  # Inicializa a variável para garantir que o loop comece

print("\n--- Sistema de Login ---")

while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == SENHA_CORRETA:
        print(f"\nSenha válida! Acesso concedido.")       
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")

# O programa termina aqui após o while
print ("Total de entradas erradas", tentativas_erradas)

#Porque a variável senha_digitada começa com vazio "":

#Ela garante que a condição do laço de repetição while
#  seja verdadeira na primeira vez que o programa a verifica 
# "" é diferente de "python123". Isso força o programa
#  a entrar no loop e pedir a senha para o usuário, 
# evitando que o código trave antes de começar.