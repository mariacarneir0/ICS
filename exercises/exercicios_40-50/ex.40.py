[12:11, 5/31/2024] Naju 🤍: # Lista de entrada
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Função para retornar uma lista apenas com os números pares
def numeros_pares(lista):
    # Inicializa uma lista vazia para armazenar os números pares
    numeros_pares_lista = []
    
    # Itera sobre cada número na lista de entrada
    for numero in lista:
        # Verifica se o número é par (ou seja, se o resto da divisão por 2 é zero)
        if numero % 2 == 0:
            # Se for par, adiciona o número à lista de números pares
            numeros_pares_lista.append(numero)
    
    # Retorna a lista de números pares
    return numeros_pares_lista

# Chamamos a função passando a lista de entrada como argumento e armazenamos o resultado em uma variável
saida = numeros_pares(entrada)


