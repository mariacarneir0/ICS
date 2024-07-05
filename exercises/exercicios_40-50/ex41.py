# Lista de entrada
entrada = ["maçã", "banana", "kiwi", "abacate", "uva"]

# Função para retornar uma lista apenas com as palavras que têm mais de 4 caracteres
def palavras_mais_de_4_caracteres(lista):
    # Inicializa uma lista vazia para armazenar as palavras com mais de 4 caracteres
    palavras_lista = []
    
    # Itera sobre cada palavra na lista de entrada
    for palavra in lista:
        # Verifica se a palavra tem mais de 4 caracteres
        if len(palavra) > 4:
            # Se tiver mais de 4 caracteres, adiciona a palavra à lista de palavras
            palavras_lista.append(palavra)
    
    # Retorna a lista de palavras com mais de 4 caracteres
    return palavras_lista

# Chamamos a função passando a lista de entrada como argumento e armazenamos o resultado em uma variável
saida = palavras_mais_de_4_caracteres(entrada)

# Imprime a lista resultante
print(saida)