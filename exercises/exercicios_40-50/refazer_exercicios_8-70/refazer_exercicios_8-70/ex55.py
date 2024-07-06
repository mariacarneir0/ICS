lista_listas = [[3, 5, 1, 7], [10, 2, 8], [6, 9, 4]]

primeira_sublista = lista_listas[0]
menor_numero = primeira_sublista[0]

for numero in primeira_sublista:
    if numero < menor_numero:
        menor_numero = numero

print("O menor número na primeira sublista é:",(menor_numero))