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


arquivo_json = 'dados.json'

menor, maior, dias_acima = calcular_faturamento_arquivo(arquivo_json)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima}")
