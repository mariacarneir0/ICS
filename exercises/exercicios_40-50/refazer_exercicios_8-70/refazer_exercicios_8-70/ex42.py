lista_de_entrada =  ["maçã", "banana", "Kiwi", "Abacate", "uva", ]

for palavra in range(len(lista_de_entrada)):
    palavra_com_mais_de_4_caracteres = lista_de_entrada[palavra]
    if len(palavra_com_mais_de_4_caracteres) > 4:
        print(palavra_com_mais_de_4_caracteres)