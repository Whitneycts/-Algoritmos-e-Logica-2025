mensagem = ""

print("--- Repetidor Interativo ---")
print("Digite 'sair' a qualquer momento para encerrar o programa.")

while mensagem != "sair":
 mensagem = input("Digite uma mensagem: ").lower()  

 if mensagem != "sair":
    print(f"Você digitou: {mensagem}")
else:
    print("\nPrograma encerrado. Até logo!")