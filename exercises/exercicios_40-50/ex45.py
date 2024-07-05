# Lista de entrada
entrada = [1, 2, 3, 4, 5]

# Função para retornar uma lista contendo o quadrado dos números ímpares
def quadrado_numeros_impares(lista):
    # Inicializa uma lista vazia para armazenar os quadrados dos números ímpares
    quadrados_impares = []
    
    # Itera sobre cada número na lista de entrada
    for numero in lista:
        # Verifica se o número é ímpar
        if numero % 2 != 0:
            # Se o número for ímpar, calcula o seu quadrado e adiciona à lista de quadrados_impares
            quadrados_impares.append(numero ** 2)
    
    # Retorna a lista contendo os quadrados dos números ímpares
    return quadrados_impares

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = quadrado_numeros_impares(entrada)

# Imprime a lista resultante
print(saida)