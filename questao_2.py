# Questão 2 - Resolução
def is_fibonacci(num):
    # Preparando a sequência
    a, b = 0, 1

    # Gerando a sequência até que o valor ultrapasse o número informado
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False

# Definindo o número a ser verificado
numero = int(input("Informe um número: "))

# Verificando se o número está na sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
