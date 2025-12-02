PADRAO_IDEAL = 50.0
LIMITE_MAXIMO_DESVIO = 10.0

desvios_registrados = []
dias_consecutivos_baixo_padrao = 0

print("--- Análise de Desvio de Qualidade com Alerta de Risco ---")

while True:
    medida_peca = float(input("Digite a Medida da Peça (decimal) ou 0 para sair: "))
    
    if medida_peca == 0:
        break
    
    desvio_absoluto = abs(medida_peca - PADRAO_IDEAL)
    desvios_registrados.append(desvio_absoluto)
    
    if desvio_absoluto > LIMITE_MAXIMO_DESVIO:
        dias_consecutivos_baixo_padrao += 1
        
        if dias_consecutivos_baixo_padrao >= 3:
            print(f"ALERTA MÁXIMO! Produção Paralisada por Risco de Qualidade!")
            break
    else:
        dias_consecutivos_baixo_padrao = 0

print("\n--- Relatório de Qualidade ---\n")

soma_desvios = 0.0

for desvio in desvios_registrados:
    soma_desvios += desvio

if len(desvios_registrados) > 0:
    media_desvio = soma_desvios / len(desvios_registrados)
else:
    media_desvio = 0.0

print(f"Média de Desvio: {media_desvio:.2f}")
print(f"Motivo da Parada: Padrão Ideal = {PADRAO_IDEAL}, Limite Máximo de Desvio = {LIMITE_MAXIMO_DESVIO}")
