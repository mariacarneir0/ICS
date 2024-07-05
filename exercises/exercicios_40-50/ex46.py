# Lista de entrada
entrada = [5, 3, 9, 1, 10]

# Função para encontrar e retornar o maior número da lista
def encontrar_maior(lista):
    # Inicializa uma variável com o primeiro elemento da lista
    maior_numero = lista[0]
    
    # Itera sobre cada número na lista de entrada
    for numero in lista:
        # Verifica se o número atual é maior que o maior número atualmente registrado
        if numero > maior_numero:
            # Se o número atual for maior, atualiza o valor do maior número
            maior_numero = numero
    
    # Retorna o maior número encontrado na lista
    return maior_numero

# Chama a função passando a lista de entrada como argumento e armazena o resultado em uma variável
saida = encontrar_maior(entrada)

# Imprime o maior número encontrado
print(saida)