# Questão 4 - Resolução

# Faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento.values())

# Percentual dos estados
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

# Mostrar resultados
print("Percentuais de representação do faturamento mensal por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
