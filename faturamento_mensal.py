import json

def calcular_faturamento_arquivo(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamento_filtrado = [dia["valor"] for dia in dados if dia["valor"] > 0]
    
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    dias_acima_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

def calcular_percentual_faturamento():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    total_faturamento = sum(faturamento_estados.values())
    
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}
    
    return percentuais


arquivo_json = 'dados.json'

menor, maior, dias_acima = calcular_faturamento_arquivo(arquivo_json)
percentuais = calcular_percentual_faturamento()

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima}")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
