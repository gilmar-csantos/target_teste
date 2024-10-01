# Questão 3 - Resolução
import json

# Carregando arquivo JSON
def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

# Calculando o menor, maior faturamento e dias acima da média
def calcular_faturamento(dados):
    # Filtra os dias com valor maior que zero (dias úteis)
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    # Ignorando os diass sem faturamento
    if not faturamentos:
        return 0, 0, 0

    # Cálculos de menor e maior dia
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Cálculos de média mensal
    media_faturamento = sum(faturamentos) / len(faturamentos)

    # Cálculo faturamento acima da média
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

# Carregando dados usando o caminho do arquivo (estava em outra pasta)
dados_faturamento = carregar_faturamento('C:/Users/ADM/OneDrive/Área de Trabalho/projetos/estagio/dados.json')

# Cálculos finais
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

# Mostrar resultados
print(f"Menor valor de faturamento: {menor:.2f}")
print(f"Maior valor de faturamento: {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
