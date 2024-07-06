def reverte_lista(lista_de_entrada):
    contador = len(lista_de_entrada) -1
    Lista_auxiliar = []

    while contador >=0:
       numero = lista_de_entrada[contador]
       Lista_auxiliar.append(numero)
       contador = contador -1

    return Lista_auxiliar

Lista_revertida = reverte_lista([1, 2, 3, 4, 5])
print(Lista_revertida)