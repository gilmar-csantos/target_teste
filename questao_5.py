# Questão 5 - Resolução

# Fazendo a função
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida  # Adiciona o caractere à frente da nova string
    return string_invertida

# String de exemplo
entrada = "Hello, World!"

# Inverter a string
resultado = inverter_string(entrada)

# Mostrar resultado
print(f"String original: {entrada}")
print(f"String invertida: {resultado}")
